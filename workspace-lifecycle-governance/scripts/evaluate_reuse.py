#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
evaluate_reuse.py - 项目创建 vs 存量复用阶梯决策器 (Project Reuse-Ladder Evaluator)
Evaluates new demands against the 4-level Reuse Ladder and 4 standalone project hard gates.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def scan_existing_projects(vibe_coding_dir: Path) -> List[str]:
    """Scan existing projects in Vibe_Coding to detect potential reuse candidates."""
    if not vibe_coding_dir.exists() or not vibe_coding_dir.is_dir():
        return []
    projects = []
    for item in vibe_coding_dir.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            projects.append(item.name)
    return projects

def evaluate_reuse_ladder(
    demand_title: str,
    demand_desc: str,
    target_tech: str = "",
    has_cli_tool: bool = False,
    matches_existing_repo: str = "",
    is_meta_skill: bool = False,
    gate_independent_mental: bool = True,
    gate_runtime_incompatible: bool = False,
    gate_no_reference_pattern: bool = True,
    gate_poc_verified: bool = False
) -> Dict[str, Any]:
    """Evaluate demand against the 4-tier ladder."""

    # Level 1: Zero-code / existing tool
    if has_cli_tool:
        return {
            "title": demand_title,
            "decision_level": "Level 1: 现有工具/标准协议直接解决 (Zero Code)",
            "action": "USE_EXISTING_TOOL",
            "target_workspace": "None (直接配置系统工具/CLI/MCP)",
            "rationale": "该需求已有现成标准 CLI、MCP Server 或内置工具可完全覆盖，无需编写或新建任何代码仓库。",
            "gate_audit": None
        }

    # Level 3: Meta-skill / agent governance
    if is_meta_skill or "skill" in demand_title.lower() or "治理" in demand_title or "机制" in demand_title:
        return {
            "title": demand_title,
            "decision_level": "Level 3: 自研母体技能/机制扩展 (Author-Skills)",
            "action": "AUTHOR_SKILLS_EXTENSION",
            "target_workspace": "Author-Skills/",
            "rationale": "该需求属于跨工作区生命周期治理、Agent 规则进化或元机制，归属母体技能仓库。",
            "gate_audit": None
        }

    # Level 2: Existing Repo Extension
    if matches_existing_repo:
        return {
            "title": demand_title,
            "decision_level": "Level 2: 现有项目模块/插件扩展 (Repo Extension)",
            "action": "EXTEND_EXISTING_REPO",
            "target_workspace": f"Vibe_Coding/{matches_existing_repo}",
            "rationale": f"该需求与现有项目 `{matches_existing_repo}` 共享技术栈、用户群或运行宿主，应作为该项目的一个 Module / Package / Adapter 进行扩展，严禁碎片化建库。",
            "gate_audit": None
        }

    # Level 4: Standalone Project Hard Gate Audit
    gates = [
        {"gate": "1. 独立用户心智 (Independent Product Mental Model)", "passed": gate_independent_mental, "desc": "是否具有完全独立的产品形态与生命周期"},
        {"gate": "2. 运行时物理隔离 (Runtime Incompatibility)", "passed": gate_runtime_incompatible, "desc": "技术栈或运行宿主是否存在物理冲突 (如 GUI vs Daemon)"},
        {"gate": "3. 外部参考库查重 (Reference Check)", "passed": gate_no_reference_pattern, "desc": "已在 Reference_Coding 中确认无现成可用模式"},
        {"gate": "4. 最小 PoC 验证通过 (PoC Verified)", "passed": gate_poc_verified, "desc": "核心机制已在 Learning_Labs 或最小原型中验证通过"}
    ]

    all_gates_pass = all(g["passed"] for g in gates)

    if all_gates_pass:
        return {
            "title": demand_title,
            "decision_level": "Level 4: 独立立项资格审查通过 (New Standalone Project)",
            "action": "CREATE_NEW_PROJECT",
            "target_workspace": f"Vibe_Coding/<new-repo-name>",
            "rationale": "同时满足独立立项全部 4 大硬门禁，正式授权在 Vibe_Coding 中建立独立项目仓库，并需立即执行 /project-guard init 植入规范。",
            "gate_audit": gates
        }
    else:
        failed_gates = [g["gate"] for g in gates if not g["passed"]]
        return {
            "title": demand_title,
            "decision_level": "REJECTED (未达独立立项门禁)",
            "action": "RECONSIDER_OR_POC",
            "target_workspace": "My_Learning/ 或 归并至存量项目",
            "rationale": f"未满足独立立项门禁: {', '.join(failed_gates)}。建议先在 My_Learning 登记或在 Learning_Labs 做最小原型验证。",
            "gate_audit": gates
        }

def print_reuse_report(report: Dict[str, Any]):
    """Print formatted reuse evaluation report."""
    print("=========================================================================================")
    print("        Workspace Lifecycle Governance: Project Reuse-Ladder Decision Report            ")
    print("=========================================================================================")
    print(f"评估需求标题 : {report['title']}")
    print(f"阶梯判定结论 : {report['decision_level']}")
    print(f"目标流转工作区: {report['target_workspace']}")
    print(f"判定决策理由 : {report['rationale']}")
    print("-----------------------------------------------------------------------------------------")

    if report["gate_audit"]:
        print("独立立项 4 大硬门禁逐项核验结果:")
        for idx, g in enumerate(report["gate_audit"], 1):
            status_str = "[PASS]" if g["passed"] else "[FAIL / UNVERIFIED]"
            print(f"  {idx}. {g['gate']:<45} : {status_str} ({g['desc']})")
        print("-----------------------------------------------------------------------------------------")

    print("=========================================================================================")

def main():
    parser = argparse.ArgumentParser(description="Evaluate a demand against the 4-tier Reuse Ladder.")
    parser.add_argument("--title", "-t", required=True, help="Demand title")
    parser.add_argument("--desc", "-d", default="", help="Demand description")
    parser.add_argument("--tech", default="", help="Proposed tech stack")
    parser.add_argument("--match-repo", "-m", default="", help="Name of existing repo if related")
    parser.add_argument("--cli-tool", action="store_true", help="Can be solved with existing CLI / MCP tool")
    parser.add_argument("--meta-skill", action="store_true", help="Is a meta governance skill / agent rule")
    parser.add_argument("--runtime-isolated", action="store_true", help="Runtime is physically incompatible with existing repos")
    parser.add_argument("--poc-done", action="store_true", help="PoC has been verified")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON format")
    args = parser.parse_args()

    report = evaluate_reuse_ladder(
        demand_title=args.title,
        demand_desc=args.desc,
        target_tech=args.tech,
        has_cli_tool=args.cli_tool,
        matches_existing_repo=args.match_repo,
        is_meta_skill=args.meta_skill,
        gate_runtime_incompatible=args.runtime_isolated,
        gate_poc_verified=args.poc_done
    )

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_reuse_report(report)

if __name__ == "__main__":
    main()
