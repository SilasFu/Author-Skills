#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
doctor.py - 全项目健康诊断与防腐编排器 (Unified Project Doctor & Health Auditor)
Executes deterministic audits for line counts, design drift, blackbox state, and compiler verification.
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path
from typing import Dict, Any, Tuple

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Import sibling audit modules
try:
    from audit_sprawl import audit_sprawl
    from audit_design_drift import audit_design_drift
except ImportError:
    script_dir = Path(__file__).parent
    sys.path.append(str(script_dir))
    from audit_sprawl import audit_sprawl
    from audit_design_drift import audit_design_drift

def detect_project_compiler(root_dir: Path) -> Tuple[str, str]:
    """Detect package manager and verification command."""
    if (root_dir / "pnpm-lock.yaml").exists():
        return "pnpm", "pnpm typecheck" if (root_dir / "tsconfig.json").exists() else "pnpm build"
    elif (root_dir / "package-lock.json").exists():
        return "npm", "npm run typecheck" if (root_dir / "tsconfig.json").exists() else "npm run build"
    elif (root_dir / "yarn.lock").exists():
        return "yarn", "yarn typecheck" if (root_dir / "tsconfig.json").exists() else "yarn build"
    elif (root_dir / "Cargo.toml").exists():
        return "cargo", "cargo check"
    elif (root_dir / "pyproject.toml").exists() or (root_dir / "requirements.txt").exists():
        return "python", "pytest" if (root_dir / "tests").exists() else "python -m compileall ."
    elif (root_dir / "go.mod").exists():
        return "go", "go vet ./..."
    return "unknown", ""

def check_blackbox_state(root_dir: Path) -> Dict[str, Any]:
    """Check for suspicious private blackbox memories or uncommitted drift."""
    blackbox_patterns = [".antigravity", ".cursor-private", ".claude-memory", ".local_storage"]
    found = []
    for p in blackbox_patterns:
        if (root_dir / p).exists():
            found.append(p)
    return {
        "passed": len(found) == 0,
        "violations": found
    }

def run_compiler_check(root_dir: Path, check_cmd: str) -> Dict[str, Any]:
    """Run native compiler / typecheck if command is available."""
    if not check_cmd:
        return {"checked": False, "passed": True, "output": "未探测到自动化编译命令或跳过"}

    try:
        res = subprocess.run(
            check_cmd,
            cwd=str(root_dir),
            shell=True,
            capture_output=True,
            text=True,
            timeout=120
        )
        passed = (res.returncode == 0)
        output = res.stdout if passed else (res.stderr or res.stdout)
        return {
            "checked": True,
            "passed": passed,
            "command": check_cmd,
            "output": output.strip()[:500] if output else ""
        }
    except Exception as e:
        return {
            "checked": True,
            "passed": False,
            "command": check_cmd,
            "output": f"Execution error: {str(e)}"
        }

def run_doctor(root_dir: Path, max_lines: int = 200, run_compile: bool = True) -> Dict[str, Any]:
    """Run full doctor audit suite."""
    sprawl_res = audit_sprawl(root_dir, max_lines=max_lines)
    drift_res = audit_design_drift(root_dir)
    blackbox_res = check_blackbox_state(root_dir)
    pkg_type, check_cmd = detect_project_compiler(root_dir)

    compile_res = run_compiler_check(root_dir, check_cmd) if run_compile else {"checked": False, "passed": True, "output": "Skipped"}

    all_passed = (
        len(sprawl_res) == 0 and
        len(drift_res) == 0 and
        blackbox_res["passed"] and
        compile_res["passed"]
    )

    return {
        "target": str(root_dir),
        "overall_pass": all_passed,
        "project_type": pkg_type,
        "sprawl": {
            "count": len(sprawl_res),
            "passed": len(sprawl_res) == 0,
            "details": sprawl_res
        },
        "drift": {
            "count": len(drift_res),
            "passed": len(drift_res) == 0,
            "details": drift_res[:10]
        },
        "blackbox": blackbox_res,
        "compiler": compile_res
    }

def print_health_card(report: Dict[str, Any]):
    """Render a structured health card."""
    sprawl_str = "[PASS] (0 违规)" if report["sprawl"]["passed"] else f"[FAIL] ({report['sprawl']['count']} 文件 > 200 行)"
    drift_str = "[PASS] (0 违规)" if report["drift"]["passed"] else f"[WARN] ({report['drift']['count']} 处野颜色)"
    blackbox_str = "[PASS] (Pure SSOT)" if report["blackbox"]["passed"] else f"[FAIL] (存在黑盒暗状态)"
    compiler_str = "[PASS] (0 Errors)" if report["compiler"]["passed"] else f"[FAIL] (编译/类型报错)"

    print("===============================================================")
    print("        Project Guard Doctor Health Card (全项目健康诊断报告)   ")
    print("===============================================================")
    print(f"  * 单文件健康度 (<= 200 lines)  : {sprawl_str}")
    print(f"  * 设计 Token 遵从度           : {drift_str}")
    print(f"  * 黑盒暗状态检查              : {blackbox_str}")
    print(f"  * 编译器/类型自检             : {compiler_str}")
    print("===============================================================")

    if not report["overall_pass"]:
        print("\n[待自愈与修复清单]:")
        if not report["sprawl"]["passed"]:
            print(f"1. 巨石代码: 共 {report['sprawl']['count']} 个文件超标，需进行 UI/Hook/Type 垂直切片。")
        if not report["drift"]["passed"]:
            print(f"2. 设计漂移: 共 {report['drift']['count']} 处硬编码颜色，需收敛至 DESIGN.md 语义 Token。")
        if not report["compiler"]["passed"]:
            print(f"3. 编译报错: {report['compiler'].get('command', 'unknown')} 校验未通过，请查看编译器错误。")
    else:
        print("\n[结果] 项目健康状态极佳，符合所有工程与设计硬门禁！")

def main():
    parser = argparse.ArgumentParser(description="Run complete Project Guard health audit.")
    parser.add_argument("--path", "-p", default=".", help="Target directory (default: current directory)")
    parser.add_argument("--max-lines", "-m", type=int, default=200, help="Max lines per file (default: 200)")
    parser.add_argument("--skip-compile", action="store_true", help="Skip running build/typecheck command")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    root_path = Path(args.path).resolve()
    if not root_path.exists():
        print(f"Error: Path '{root_path}' does not exist.", file=sys.stderr)
        sys.exit(1)

    report = run_doctor(root_path, max_lines=args.max_lines, run_compile=not args.skip_compile)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_health_card(report)

    sys.exit(0 if report["overall_pass"] else 1)

if __name__ == "__main__":
    main()
