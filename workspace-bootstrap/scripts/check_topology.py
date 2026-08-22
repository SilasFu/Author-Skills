#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_topology.py - 工作区生态 6 大 Bank 拓扑健康扫描器 (Workspace Topology Auditor)
Scans 6 workspace banks, checks directory existence, git status, and environment variables.
"""

import os
import sys
import json
import subprocess
import argparse
from pathlib import Path
from typing import Dict, Any, List

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

WORKSPACE_BANKS = [
    {"name": "Idea Hub (灵感总控)", "dir": "Idea_Hub", "alt_dir": None, "key": "idea_hub", "desc": "灵感提出、评估与跨区派发总控中枢"},
    {"name": "Memory Bank (权威记忆)", "dir": "MY_Memories", "alt_dir": None, "key": "memory_bank", "desc": "只读/高置信度画像、偏好、边界与规范"},
    {"name": "Project Bank (自建代码)", "dir": "Vibe_Coding", "alt_dir": None, "key": "project_bank", "desc": "自研产品与生产级开发工作区"},
    {"name": "Learning Bank (知识学习)", "dir": "My_Learning", "alt_dir": None, "key": "learning_bank", "desc": "技术盲区登记、研究计划与系统知识沉淀"},
    {"name": "Reference Bank (外部参考)", "dir": "Reference_Coding", "alt_dir": None, "key": "reference_bank", "desc": "第三方开源项目与优秀实践参考源码 (严格只读)"},
    {"name": "Author Skills (自研技能)", "dir": "Author-Skills", "alt_dir": "Vibe_Coding/Author-Skills", "key": "author_skills", "desc": "个人原创与深度定制的 Agent 技能源码母体"}
]

def check_git_status(dir_path: Path) -> Dict[str, Any]:
    """Check Git status of a workspace bank."""
    if not (dir_path / ".git").exists():
        return {"is_git": False, "remote": "", "clean": True}

    try:
        remote_res = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(dir_path),
            capture_output=True,
            text=True,
            timeout=5
        )
        remote_url = remote_res.stdout.strip() if remote_res.returncode == 0 else ""

        status_res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(dir_path),
            capture_output=True,
            text=True,
            timeout=5
        )
        clean = (len(status_res.stdout.strip()) == 0) if status_res.returncode == 0 else True

        return {
            "is_git": True,
            "remote": remote_url,
            "clean": clean
        }
    except Exception:
        return {"is_git": True, "remote": "unknown", "clean": True}

def audit_topology(root_dir: Path) -> Dict[str, Any]:
    """Audit the complete 6-bank workspace topology."""
    banks_status = []
    all_exist = True

    for bank in WORKSPACE_BANKS:
        target_path = root_dir / bank["dir"]
        actual_path = target_path
        exists = target_path.exists() and target_path.is_dir()

        # Check alternative directory (e.g., Vibe_Coding/Author-Skills)
        if not exists and bank.get("alt_dir"):
            alt_path = root_dir / bank["alt_dir"]
            if alt_path.exists() and alt_path.is_dir():
                actual_path = alt_path
                exists = True

        if not exists:
            all_exist = False

        git_info = check_git_status(actual_path) if exists else {"is_git": False, "remote": "", "clean": False}

        status_tag = "ACTIVE" if exists else "MISSING"
        if exists and git_info["is_git"] and not git_info["clean"]:
            status_tag = "DIRTY (有修改)"

        display_rel = actual_path.relative_to(root_dir).as_posix() if exists else bank["dir"]

        banks_status.append({
            "key": bank["key"],
            "name": bank["name"],
            "dir_name": display_rel,
            "path": str(actual_path),
            "exists": exists,
            "status": status_tag,
            "git": git_info,
            "desc": bank["desc"]
        })

    env_root = os.environ.get("AI_WORKSPACE_ROOT", "")
    env_memories = os.environ.get("MY_MEMORIES_PATH", "")

    return {
        "root_dir": str(root_dir),
        "all_exist": all_exist,
        "env_vars": {
            "AI_WORKSPACE_ROOT": env_root,
            "MY_MEMORIES_PATH": env_memories,
            "root_matches": (Path(env_root).resolve() == root_dir.resolve()) if env_root else False
        },
        "banks": banks_status
    }

def print_topology_card(report: Dict[str, Any]):
    """Render a structured topology health card."""
    print("=========================================================================================")
    print(f"             Workspace Topology Status Report (6 大工作区拓扑巡检报告)                  ")
    print("=========================================================================================")
    print(f"工作区根目录 (Root): {report['root_dir']}")
    env_match = "[MATCH]" if report["env_vars"]["root_matches"] else "[UNSET / MISMATCH]"
    print(f"环境变量配置 (Env) : AI_WORKSPACE_ROOT={report['env_vars']['AI_WORKSPACE_ROOT'] or '未设置'} {env_match}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{'工作区角色 (Bank)':<26} | {'相对路径':<24} | {'存在状态':<10} | {'Git 状态':<20}")
    print("-----------------------------------------------------------------------------------------")

    for b in report["banks"]:
        exist_str = "[OK] 存在" if b["exists"] else "[X] 缺失"
        git_str = "Git: " + ("Clean" if b["git"]["clean"] else "Dirty (有修改)") if b["git"]["is_git"] else "非 Git"
        print(f"{b['name']:<26} | {b['dir_name']:<24} | {exist_str:<10} | {git_str:<20}")

    print("=========================================================================================")

    if not report["all_exist"]:
        print("\n[待修复项]: 存在缺失的工作区目录，建议运行 `python setup_topology.py --root-dir <path>` 进行自动自举。")
    else:
        print("\n[结果] 6 大工作区拓扑完整，物理隔离与链路正常！")

def main():
    parser = argparse.ArgumentParser(description="Audit workspace 6-bank topology.")
    parser.add_argument("--root-dir", "-r", default=None, help="Root directory containing the 6 workspace banks")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    if args.root_dir:
        root_path = Path(args.root_dir).resolve()
    elif os.environ.get("AI_WORKSPACE_ROOT"):
        root_path = Path(os.environ["AI_WORKSPACE_ROOT"]).resolve()
    else:
        current = Path(".").resolve()
        if (current.parent / "MY_Memories").exists() or (current.parent / "Idea_Hub").exists():
            root_path = current.parent
        elif (current.parent.parent / "MY_Memories").exists() or (current.parent.parent / "Idea_Hub").exists():
            root_path = current.parent.parent
        else:
            root_path = current.parent

    report = audit_topology(root_path)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_topology_card(report)

    sys.exit(0 if report["all_exist"] else 1)

if __name__ == "__main__":
    main()
