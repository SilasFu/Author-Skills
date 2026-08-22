#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
audit_sprawl.py - 毫秒级代码巨石与行数超标扫描器 (Line Count & Sprawl Auditor)
Universal deterministic file size auditor across all languages and frameworks.
"""

import os
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
    "target", ".next", ".nuxt", ".output", ".venv", "venv", "env",
    "__pycache__", ".pytest_cache", ".gemini", ".idea", ".vscode",
    "vendor", "coverage", "bin", "obj", ".turbo", ".cache"
}

DEFAULT_EXTENSIONS = {
    ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte",
    ".py", ".rs", ".go", ".java", ".c", ".cpp", ".h", ".hpp",
    ".cs", ".rb", ".php", ".swift", ".kt"
}

def count_file_lines(file_path: Path) -> int:
    """Accurately count lines of code in a file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def audit_sprawl(
    root_dir: Path,
    max_lines: int = 200,
    ignore_dirs: set = None,
    allowed_exts: set = None
) -> List[Dict[str, Any]]:
    """Scan directory for files exceeding max_lines."""
    if ignore_dirs is None:
        ignore_dirs = DEFAULT_IGNORE_DIRS
    if allowed_exts is None:
        allowed_exts = DEFAULT_EXTENSIONS

    violations = []

    for root, dirs, files in os.walk(root_dir):
        # In-place modify dirs to skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs and not d.startswith(".")]

        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in allowed_exts:
                line_count = count_file_lines(file_path)
                if line_count > max_lines:
                    rel_path = file_path.relative_to(root_dir).as_posix()
                    violations.append({
                        "path": rel_path,
                        "lines": line_count,
                        "excess": line_count - max_lines,
                        "suggestion": "垂直切片: 拆分为 Component (UI) + Hook/Service (逻辑) + Types (类型契约)"
                    })

    # Sort descending by line count
    violations.sort(key=lambda x: x["lines"], reverse=True)
    return violations

def main():
    parser = argparse.ArgumentParser(description="Audit codebase for sprawling files exceeding line count threshold.")
    parser.add_argument("--path", "-p", default=".", help="Target workspace root path (default: current directory)")
    parser.add_argument("--max-lines", "-m", type=int, default=200, help="Maximum allowed lines per file (default: 200)")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    root_path = Path(args.path).resolve()
    if not root_path.exists():
        print(f"Error: Target path '{root_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    violations = audit_sprawl(root_path, max_lines=args.max_lines)

    if args.json:
        print(json.dumps({
            "target": str(root_path),
            "max_lines": args.max_lines,
            "violation_count": len(violations),
            "violations": violations
        }, ensure_ascii=False, indent=2))
    else:
        print(f"=== Project Guard Sprawl Audit (Threshold: <= {args.max_lines} lines) ===")
        print(f"Target Directory: {root_path}")
        if not violations:
            print(f"[PASS] 完美！未发现超过 {args.max_lines} 行的文件。")
        else:
            print(f"[FAIL] 发现 {len(violations)} 个文件超过 {args.max_lines} 行限制：\n")
            for idx, item in enumerate(violations, 1):
                print(f"  {idx}. {item['path']} -> {item['lines']} lines (+{item['excess']} 超标)")
                print(f"     建议: {item['suggestion']}")
            print("\n行动建议: 请使用 vertical slicing 重构，拆分 UI、Hook 与 Type 契约。")

    sys.exit(0 if not violations else 1)

if __name__ == "__main__":
    main()
