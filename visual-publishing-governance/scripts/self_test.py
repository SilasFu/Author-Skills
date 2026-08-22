#!/usr/bin/env python3
"""Run deterministic regression tests for visual publishing governance."""

from __future__ import annotations

import json
import struct
import tempfile
import zlib
from pathlib import Path

from audit_outputs import audit_outputs
from compare_layout import compare_layouts
from validate_visual_job import validate_manifest


def write_png(path: Path, width: int, height: int) -> None:
    def chunk(kind: bytes, payload: bytes) -> bytes:
        return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)

    row = b"\x00" + (b"\xff\xff\xff\xff" * width)
    raw = row * height
    header = struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0)
    path.write_bytes(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header) + chunk(b"IDAT", zlib.compress(raw)) + chunk(b"IEND", b""))


def main() -> int:
    checks: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="visual-governance-") as temporary:
        root = Path(temporary)
        (root / "specs").mkdir()
        (root / "final").mkdir()
        (root / "render").mkdir()
        for name in ("reference.png", "content.md", "avatar.png", "identity.png", "watermark.png"):
            (root / name).write_text("fixture", encoding="utf-8")

        approved = {
            "version": "1.0",
            "status": "approved",
            "canvas": {"width": 16, "height": 16},
            "default_tolerance_px": 1,
            "allow_extra_elements": False,
            "elements": [{"id": "title", "box": [1, 1, 8, 3]}],
        }
        actual = {**approved, "status": "actual"}
        for name, payload in (("cover.layout.json", approved), ("body.layout.json", approved), ("actual.layout.json", actual)):
            (root / "specs" / name).write_text(json.dumps(payload), encoding="utf-8")

        manifest = {
            "version": "1.0",
            "project": {"title": "fixture", "content_sources": ["content.md"]},
            "canvas": {"width": 16, "height": 16, "format": "png"},
            "composition_lock": {"status": "approved", "reference_files": ["reference.png"]},
            "assets": [
                {"id": "reference", "path": "reference.png", "role": "reference-layout", "embed": False},
                {"id": "content", "path": "content.md", "role": "content-source", "embed": False},
                {"id": "avatar", "path": "avatar.png", "role": "avatar", "embed": True},
                {"id": "identity", "path": "identity.png", "role": "identity-info", "embed": False},
                {"id": "watermark", "path": "watermark.png", "role": "watermark-sample", "embed": False},
            ],
            "identity": {"display_name": "Fixture", "avatar_asset_id": "avatar"},
            "requirements": {"require_cover": True, "minimum_body_pages": 1},
            "pages": [
                {"id": "cover", "kind": "cover", "layout_contract": "specs/cover.layout.json", "output_file": "cover.png"},
                {"id": "body", "kind": "body", "layout_contract": "specs/body.layout.json", "output_file": "body.png"},
            ],
            "copy": {"target_characters": 100, "tolerance_characters": 30},
            "render_sources": ["render/source.svg"],
            "forbidden_text": ["公众号 ·"],
            "output": {"directory": "final", "expected_images": ["cover.png", "body.png"]},
        }
        manifest_path = root / "visual-job.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        (root / "render" / "source.svg").write_text("<svg>clean</svg>", encoding="utf-8")
        write_png(root / "final" / "cover.png", 16, 16)
        write_png(root / "final" / "body.png", 16, 16)

        checks.append({"name": "valid job", "passed": validate_manifest(manifest_path, True)["passed"]})
        checks.append({"name": "layout within tolerance", "passed": compare_layouts(root / "specs" / "cover.layout.json", root / "specs" / "actual.layout.json")["passed"]})
        checks.append({"name": "clean outputs", "passed": audit_outputs(manifest_path)["passed"]})

        invalid = json.loads(json.dumps(manifest))
        invalid["assets"][3]["embed"] = True
        invalid_path = root / "invalid-job.json"
        invalid_path.write_text(json.dumps(invalid), encoding="utf-8")
        checks.append({"name": "identity screenshot rejected", "passed": not validate_manifest(invalid_path)["passed"]})

        missing_role = json.loads(json.dumps(manifest))
        missing_role["assets"] = [asset for asset in missing_role["assets"] if asset["role"] != "content-source"]
        missing_role_path = root / "missing-role-job.json"
        missing_role_path.write_text(json.dumps(missing_role), encoding="utf-8")
        checks.append({"name": "unclassified content source rejected", "passed": not validate_manifest(missing_role_path, True)["passed"]})

        unapproved_contract = json.loads(json.dumps(approved))
        unapproved_contract["status"] = "draft"
        (root / "specs" / "body.layout.json").write_text(json.dumps(unapproved_contract), encoding="utf-8")
        checks.append({"name": "unapproved page contract rejected", "passed": not validate_manifest(manifest_path, True)["passed"]})
        (root / "specs" / "body.layout.json").write_text(json.dumps(approved), encoding="utf-8")

        drifted = {**actual, "elements": [{"id": "title", "box": [4, 1, 8, 3]}]}
        drifted_path = root / "specs" / "drifted.layout.json"
        drifted_path.write_text(json.dumps(drifted), encoding="utf-8")
        checks.append({"name": "layout drift rejected", "passed": not compare_layouts(root / "specs" / "cover.layout.json", drifted_path)["passed"]})

        write_png(root / "final" / "old-draft.png", 16, 16)
        checks.append({"name": "extra draft rejected", "passed": not audit_outputs(manifest_path)["passed"]})
        (root / "final" / "old-draft.png").unlink()
        (root / "render" / "source.svg").write_text("<svg>公众号 · watermark</svg>", encoding="utf-8")
        checks.append({"name": "forbidden watermark rejected", "passed": not audit_outputs(manifest_path)["passed"]})

        (root / "qrcode.png").write_text("qr_fixture", encoding="utf-8")
        preset_manifest = {
            "version": "1.0",
            "project": {"title": "preset_fixture", "content_sources": ["content.md"]},
            "canvas": {"width": 16, "height": 16, "format": "png"},
            "composition_lock": {"status": "approved", "preset_name": "social_series_tech_blue"},
            "assets": [
                {"id": "content", "path": "content.md", "role": "content-source", "embed": False},
                {"id": "avatar", "path": "avatar.png", "role": "avatar", "embed": True},
                {"id": "qr", "path": "qrcode.png", "role": "qr-code", "embed": True},
            ],
            "identity": {"display_name": "Fixture", "avatar_asset_id": "avatar", "qr_code_asset_id": "qr"},
            "requirements": {"require_cover": True, "minimum_body_pages": 1},
            "pages": [
                {"id": "cover", "kind": "cover", "layout_contract": "specs/cover.layout.json", "output_file": "cover.png"},
                {"id": "body", "kind": "body", "layout_contract": "specs/body.layout.json", "output_file": "body.png"},
            ],
            "copy": {"target_characters": 100, "tolerance_characters": 30},
            "render_sources": ["render/source.svg"],
            "forbidden_text": ["公众号 ·"],
            "output": {"directory": "final", "expected_images": ["cover.png", "body.png"]},
        }
        preset_manifest_path = root / "preset-job.json"
        preset_manifest_path.write_text(json.dumps(preset_manifest), encoding="utf-8")
        checks.append({"name": "preset job with qr valid", "passed": validate_manifest(preset_manifest_path, True)["passed"]})

    passed = all(bool(check["passed"]) for check in checks)
    print(json.dumps({"passed": passed, "checks": checks}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
