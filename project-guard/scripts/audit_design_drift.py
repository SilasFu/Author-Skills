#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_design_drift.py - 前端设计漂移与野样式扫描器 (Design Drift & Wild Style Auditor)
Universal design token compliance checker for React, Vue, Svelte, and CSS.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

DEFAULT_IGNORE_DIRS = {
    ".git", ".svn", ".hg", "node_modules", "dist", "build", "out",
    "target", ".next", ".nuxt", ".output", ".venv", "vendor"
}

UI_EXTENSIONS = {
    ".tsx", ".jsx", ".vue", ".svelte", ".css", ".scss", ".less", ".html"
}

HEX_COLOR_PATTERN = re.compile(r'(?<![&a-zA-Z0-9_-])#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{8}|[A-Fa-f0-9]{3})\b')
RGB_PATTERN = re.compile(r'\brgba?\s*\([^)]+\)')

def audit_design_drift(root_dir: Path, ignore_dirs: set = None) -> List[Dict[str, Any]]:
    """Scan UI files for hardcoded colors and design token violations."""
    if ignore_dirs is None:
        ignore_dirs = DEFAULT_IGNORE_DIRS

    drift_items = []

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith(".")]

        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in UI_EXTENSIONS:
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                except Exception:
                    continue

                for line_idx, line in enumerate(lines, 1):
                    stripped = line.strip()
                    if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
                        continue

                    for match in HEX_COLOR_PATTERN.finditer(line):
                        hex_val = match.group(0)
                        rel_path = file_path.relative_to(root_dir).as_posix()
                        drift_items.append({
                            "path": rel_path,
                            "line": line_idx,
                            "match": hex_val,
                            "snippet": stripped[:120],
                            "issue": "Hardcoded Hex Color (野颜色)",
                            "suggestion": "替换为 DESIGN.md 中定义的语义 Token 类 (如 text-muted-foreground, bg-background, border-border)"
                        })

                    for match in RGB_PATTERN.finditer(line):
                        rgb_val = match.group(0)
                        rel_path = file_path.relative_to(root_dir).as_posix()
                        drift_items.append({
                            "path": rel_path,
                            "line": line_idx,
                            "match": rgb_val,
                            "snippet": stripped[:120],
                            "issue": "Hardcoded RGB/RGBA Color (野颜色)",
                            "suggestion": "替换为 DESIGN.md 中定义的语义 Token 或透明度工具类"
                        })

    return drift_items

def main():
    parser = argparse.ArgumentParser(description="Audit codebase for design drift and unmanaged wild styles.")
    parser.add_argument("--path", "-p", default=".", help="Target workspace root path (default: current directory)")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    root_path = Path(args.path).resolve()
    if not root_path.exists():
        print(f"Error: Target path '{root_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    drifts = audit_design_drift(root_path)

    if args.json:
        print(json.dumps({
            "target": str(root_path),
            "drift_count": len(drifts),
            "drifts": drifts
        }, ensure_ascii=False, indent=2))
    else:
        print(f"=== Project Guard Design Drift Audit ===")
        print(f"Target Directory: {root_path}")
        if not drifts:
            print("[PASS] 完美！未发现硬编码十六进制色值或野样式。")
        else:
            print(f"[FAIL] 发现 {len(drifts)} 处潜在的设计规范漂移与野颜色：\n")
            for idx, item in enumerate(drifts[:20], 1):
                print(f"  {idx}. {item['path']}:{item['line']} -> {item['match']} ({item['issue']})")
                print(f"     代码: {item['snippet']}")
                print(f"     建议: {item['suggestion']}")
            if len(drifts) > 20:
                print(f"\n  ... 以及另外 {len(drifts) - 20} 处违规。")
            print("\n行动建议: 请依据 DESIGN.md 统一收敛为语义 Token。")

    sys.exit(0 if not drifts else 1)

if __name__ == "__main__":
    main()
