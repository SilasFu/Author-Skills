#!/usr/bin/env python3
"""Deterministic HTML to High-Res Image Renderer using native Headless Edge / Chrome."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BROWSER_PATHS = [
    Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
    Path(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"),
]


def find_headless_browser() -> Path | None:
    for path in BROWSER_PATHS:
        if path.exists():
            return path
    which_edge = shutil.which("msedge")
    if which_edge:
        return Path(which_edge)
    which_chrome = shutil.which("chrome")
    if which_chrome:
        return Path(which_chrome)
    return None


def render_html_to_png(html_path: Path, output_png_path: Path, width: int = 1440, height: int = 1920) -> bool:
    browser = find_headless_browser()
    if not browser:
        print("[FAIL] No Chromium-based browser (Edge or Chrome) found on system.", file=sys.stderr)
        return False

    output_png_path.parent.mkdir(parents=True, exist_ok=True)
    file_url = html_path.resolve().as_uri()

    cmd = [
        str(browser),
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size={width},{height}",
        f"--screenshot={output_png_path.resolve()}",
        file_url,
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
        if output_png_path.exists() and output_png_path.stat().st_size > 0:
            return True
        print(f"[FAIL] Browser render produced empty output. stderr: {result.stderr}", file=sys.stderr)
        return False
    except Exception as exc:
        print(f"[FAIL] Render error: {exc}", file=sys.stderr)
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_file", type=Path, help="Path to input HTML file")
    parser.add_argument("output_png", type=Path, help="Path to output PNG file")
    parser.add_argument("--width", type=int, default=1440, help="Canvas width (default: 1440)")
    parser.add_argument("--height", type=int, default=1920, help="Canvas height (default: 1920)")
    args = parser.parse_args()

    if not args.html_file.exists():
        print(f"[FAIL] HTML file not found: {args.html_file}", file=sys.stderr)
        return 1

    success = render_html_to_png(args.html_file, args.output_png, args.width, args.height)
    if success:
        print(f"[PASS] Rendered pixel-perfect image: {args.output_png} ({args.width}x{args.height})")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
