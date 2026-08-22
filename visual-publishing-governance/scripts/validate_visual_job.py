#!/usr/bin/env python3
"""Validate a visual publishing job manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ALLOWED_ROLES = {
    "reference-layout",
    "content-source",
    "avatar",
    "qr-code",
    "brand-logo",
    "identity-info",
    "illustration",
    "watermark-sample",
}
EMBEDDABLE_ROLES = {"avatar", "illustration", "qr-code", "brand-logo"}
NON_EMBEDDABLE_ROLES = ALLOWED_ROLES - EMBEDDABLE_ROLES


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def _validate_contract(path: Path, canvas: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        contract = _load_json(path)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        return [f"cannot read approved layout contract: {exc}"]
    if contract.get("status") != "approved":
        errors.append("layout contract status must be approved")
    if contract.get("canvas") != {"width": canvas.get("width"), "height": canvas.get("height")}:
        errors.append("layout contract canvas must match the visual job canvas")
    elements = contract.get("elements")
    if not isinstance(elements, list) or not elements:
        errors.append("layout contract must contain at least one element")
        return errors
    element_ids: set[str] = set()
    for index, element in enumerate(elements):
        element_id = element.get("id")
        box = element.get("box")
        if not element_id or element_id in element_ids:
            errors.append(f"elements[{index}].id must be present and unique")
        else:
            element_ids.add(element_id)
        if not isinstance(box, list) or len(box) != 4 or not all(isinstance(value, (int, float)) for value in box):
            errors.append(f"elements[{index}].box must contain four numbers")
            continue
        x, y, width, height = box
        if x < 0 or y < 0 or width <= 0 or height <= 0:
            errors.append(f"elements[{index}].box must have non-negative position and positive size")
        elif x + width > canvas.get("width", 0) or y + height > canvas.get("height", 0):
            errors.append(f"elements[{index}].box must stay inside the canvas")
    return errors


def validate_manifest(path: Path, check_paths: bool = False) -> dict[str, Any]:
    data = _load_json(path)
    base = path.parent
    errors: list[str] = []

    def fail(location: str, message: str) -> None:
        errors.append(f"{location}: {message}")

    canvas = data.get("canvas", {})
    width, height = canvas.get("width"), canvas.get("height")
    if not isinstance(width, int) or width <= 0:
        fail("canvas.width", "must be a positive integer")
    if not isinstance(height, int) or height <= 0:
        fail("canvas.height", "must be a positive integer")
    if canvas.get("format") not in {"png", "svg"}:
        fail("canvas.format", "must be png or svg")

    lock = data.get("composition_lock", {})
    if lock.get("status") != "approved":
        fail("composition_lock.status", "must be approved before production")
    preset_name = lock.get("preset_name")
    references = lock.get("reference_files", [])
    if not preset_name and (not isinstance(references, list) or not references):
        fail("composition_lock", "must specify preset_name or at least one reference file in reference_files")

    assets = data.get("assets", [])
    if not isinstance(assets, list):
        assets = []
        fail("assets", "must be a list")
    asset_ids: set[str] = set()
    asset_roles: dict[str, str] = {}
    asset_paths: dict[str, str] = {}
    for index, asset in enumerate(assets):
        location = f"assets[{index}]"
        asset_id = asset.get("id")
        role = asset.get("role")
        if not asset_id or asset_id in asset_ids:
            fail(f"{location}.id", "must be present and unique")
        else:
            asset_ids.add(asset_id)
            asset_roles[asset_id] = role
        if role not in ALLOWED_ROLES:
            fail(f"{location}.role", f"must be one of {sorted(ALLOWED_ROLES)}")
        if not isinstance(asset.get("embed"), bool):
            fail(f"{location}.embed", "must be true or false")
        elif role in NON_EMBEDDABLE_ROLES and asset["embed"] is not False:
            fail(f"{location}.embed", f"role {role!r} is source metadata or exclusion evidence")
        asset_path = asset.get("path")
        if not isinstance(asset_path, str) or not asset_path:
            fail(f"{location}.path", "must be present")
        elif asset_path in asset_paths:
            fail(f"{location}.path", f"already classified as {asset_paths[asset_path]!r}")
        else:
            asset_paths[asset_path] = role
            if check_paths and not (base / asset_path).resolve().exists():
                fail(f"{location}.path", "file does not exist")

    identity = data.get("identity", {})
    avatar_id = identity.get("avatar_asset_id")
    if avatar_id and asset_roles.get(avatar_id) != "avatar":
        fail("identity.avatar_asset_id", "must point to an asset with role avatar")
    qr_code_id = identity.get("qr_code_asset_id")
    if qr_code_id and asset_roles.get(qr_code_id) != "qr-code":
        fail("identity.qr_code_asset_id", "must point to an asset with role qr-code")
    logo_id = identity.get("brand_logo_asset_id")
    if logo_id and asset_roles.get(logo_id) != "brand-logo":
        fail("identity.brand_logo_asset_id", "must point to an asset with role brand-logo")

    pages = data.get("pages", [])
    if not isinstance(pages, list) or not pages:
        pages = []
        fail("pages", "must contain at least one page")
    page_ids: set[str] = set()
    page_outputs: set[str] = set()
    cover_count = 0
    body_count = 0
    for index, page in enumerate(pages):
        location = f"pages[{index}]"
        page_id = page.get("id")
        output_file = page.get("output_file")
        if not page_id or page_id in page_ids:
            fail(f"{location}.id", "must be present and unique")
        else:
            page_ids.add(page_id)
        if not output_file or output_file in page_outputs:
            fail(f"{location}.output_file", "must be present and unique")
        else:
            page_outputs.add(output_file)
        cover_count += page.get("kind") == "cover"
        body_count += page.get("kind") == "body"
        contract = page.get("layout_contract")
        if not contract:
            fail(f"{location}.layout_contract", "is required")
        elif check_paths:
            contract_path = (base / contract).resolve()
            if not contract_path.exists():
                fail(f"{location}.layout_contract", "file does not exist")
            else:
                for error in _validate_contract(contract_path, canvas):
                    fail(f"{location}.layout_contract", error)

    requirements = data.get("requirements", {})
    if requirements.get("require_cover", True) and cover_count != 1:
        fail("pages", "must contain exactly one cover")
    minimum_body = requirements.get("minimum_body_pages", 1)
    if not isinstance(minimum_body, int) or body_count < minimum_body:
        fail("pages", f"must contain at least {minimum_body} body page(s)")

    expected = data.get("output", {}).get("expected_images", [])
    if set(expected) != page_outputs:
        fail("output.expected_images", "must exactly match page output_file values")

    copy = data.get("copy", {})
    target = copy.get("target_characters")
    tolerance = copy.get("tolerance_characters")
    if not isinstance(target, int) or target <= 0:
        fail("copy.target_characters", "must be a positive integer")
    if not isinstance(tolerance, int) or tolerance < 0:
        fail("copy.tolerance_characters", "must be a non-negative integer")

    if check_paths:
        for index, reference in enumerate(references):
            if not (base / reference).resolve().exists():
                fail(f"composition_lock.reference_files[{index}]", "file does not exist")
            if asset_paths.get(reference) != "reference-layout":
                fail(f"composition_lock.reference_files[{index}]", "must map to one asset with role reference-layout")
        for index, source in enumerate(data.get("project", {}).get("content_sources", [])):
            if not (base / source).resolve().exists():
                fail(f"project.content_sources[{index}]", "file does not exist")
            if asset_paths.get(source) != "content-source":
                fail(f"project.content_sources[{index}]", "must map to one asset with role content-source")

    return {"passed": not errors, "manifest": str(path.resolve()), "errors": errors}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = validate_manifest(args.manifest.resolve(), args.check_paths)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        report = {"passed": False, "manifest": str(args.manifest), "errors": [str(exc)]}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("[PASS] visual job is production-ready" if report["passed"] else "[FAIL] visual job")
        for error in report["errors"]:
            print(f"- {error}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
