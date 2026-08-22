#!/usr/bin/env python3
"""Compare an actual layout contract with its approved reference contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def compare_layouts(expected_path: Path, actual_path: Path) -> dict[str, Any]:
    expected = _load(expected_path)
    actual = _load(actual_path)
    errors: list[str] = []
    measurements: list[dict[str, Any]] = []
    if expected.get("status") != "approved":
        errors.append("expected contract is not approved")
    if expected.get("canvas") != actual.get("canvas"):
        errors.append("canvas differs from approved contract")

    expected_elements = {item["id"]: item for item in expected.get("elements", [])}
    actual_elements = {item["id"]: item for item in actual.get("elements", [])}
    default_tolerance = expected.get("default_tolerance_px", 0)
    for element_id, expected_item in expected_elements.items():
        actual_item = actual_elements.get(element_id)
        if actual_item is None:
            errors.append(f"missing element: {element_id}")
            continue
        expected_box = expected_item.get("box", [])
        actual_box = actual_item.get("box", [])
        if len(expected_box) != 4 or len(actual_box) != 4:
            errors.append(f"invalid box for element: {element_id}")
            continue
        delta = [abs(float(a) - float(b)) for a, b in zip(expected_box, actual_box)]
        tolerance = expected_item.get("tolerance_px", default_tolerance)
        passed = max(delta) <= tolerance
        measurements.append(
            {"id": element_id, "delta": delta, "max_delta": max(delta), "tolerance": tolerance, "passed": passed}
        )
        if not passed:
            errors.append(f"{element_id} drifted by {max(delta):g}px (tolerance {tolerance}px)")

    if not expected.get("allow_extra_elements", False):
        extras = sorted(set(actual_elements) - set(expected_elements))
        for element_id in extras:
            errors.append(f"unexpected element: {element_id}")
    return {"passed": not errors, "errors": errors, "measurements": measurements}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("expected", type=Path)
    parser.add_argument("actual", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = compare_layouts(args.expected.resolve(), args.actual.resolve())
    except (OSError, ValueError, json.JSONDecodeError, KeyError) as exc:
        report = {"passed": False, "errors": [str(exc)], "measurements": []}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("[PASS] layout is within tolerance" if report["passed"] else "[FAIL] layout drift")
        for error in report["errors"]:
            print(f"- {error}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

