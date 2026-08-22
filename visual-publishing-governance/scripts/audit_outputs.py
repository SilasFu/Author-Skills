#!/usr/bin/env python3
"""Audit final visual outputs against a visual job manifest."""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".svg"}


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _image_size(path: Path) -> tuple[int, int]:
    if path.suffix.lower() == ".png":
        with path.open("rb") as handle:
            header = handle.read(24)
        if header[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"invalid PNG: {path.name}")
        return struct.unpack(">II", header[16:24])
    if path.suffix.lower() == ".svg":
        text = path.read_text(encoding="utf-8", errors="replace")[:4096]
        width = re.search(r'\bwidth=["\']([0-9.]+)', text)
        height = re.search(r'\bheight=["\']([0-9.]+)', text)
        if width and height:
            return int(float(width.group(1))), int(float(height.group(1)))
    raise ValueError(f"dimension reader does not support {path.suffix}: {path.name}")


def audit_outputs(manifest_path: Path, output_override: Path | None = None) -> dict[str, Any]:
    data = _load(manifest_path)
    base = manifest_path.parent
    output_dir = output_override or (base / data.get("output", {}).get("directory", "final"))
    expected = set(data.get("output", {}).get("expected_images", []))
    errors: list[str] = []
    if not output_dir.exists():
        return {"passed": False, "errors": [f"output directory missing: {output_dir}"], "files": []}

    images = {item.name: item for item in output_dir.iterdir() if item.is_file() and item.suffix.lower() in IMAGE_SUFFIXES}
    missing = sorted(expected - set(images))
    extra = sorted(set(images) - expected)
    errors.extend(f"missing output: {name}" for name in missing)
    errors.extend(f"unexpected output: {name}" for name in extra)

    canvas = data.get("canvas", {})
    expected_size = (canvas.get("width"), canvas.get("height"))
    dimensions: dict[str, list[int]] = {}
    for name in sorted(expected & set(images)):
        try:
            size = _image_size(images[name])
            dimensions[name] = list(size)
            if size != expected_size:
                errors.append(f"{name} has size {size}, expected {expected_size}")
        except ValueError as exc:
            errors.append(str(exc))

    forbidden = [str(item).casefold() for item in data.get("forbidden_text", []) if str(item)]
    for source in data.get("render_sources", []):
        source_path = (base / source).resolve()
        if not source_path.exists():
            errors.append(f"render source missing: {source}")
            continue
        text = source_path.read_text(encoding="utf-8", errors="replace").casefold()
        for token in forbidden:
            if token in text:
                errors.append(f"forbidden text {token!r} found in render source {source}")

    return {
        "passed": not errors,
        "output_directory": str(output_dir.resolve()),
        "files": sorted(images),
        "dimensions": dimensions,
        "errors": errors,
        "visual_qa_required": "Raster OCR and clipping require original-resolution visual inspection.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = audit_outputs(args.manifest.resolve(), args.output_dir.resolve() if args.output_dir else None)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        report = {"passed": False, "errors": [str(exc)], "files": []}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("[PASS] final output set is clean" if report["passed"] else "[FAIL] output audit")
        for error in report["errors"]:
            print(f"- {error}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

