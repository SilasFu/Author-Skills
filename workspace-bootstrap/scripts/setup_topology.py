#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup_topology.py - 6 大工作区生态初始化与自举器 (Workspace Topology Bootstrapper)
Scaffolds missing banks, injects seed templates, and sets persistent environment variables.
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Any

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REQUIRED_BANKS = [
    "Idea_Hub",
    "MY_Memories",
    "Vibe_Coding",
    "My_Learning",
    "Reference_Coding",
    "Author-Skills"
]

def set_persistent_env(name: str, value: str) -> bool:
    """Set persistent user-level environment variable cross-platform."""
    if sys.platform == "win32":
        try:
            # Use PowerShell to set user-level environment variable
            cmd = f'[Environment]::SetEnvironmentVariable("{name}", "{value}", "User")'
            subprocess.run(["powershell", "-NoProfile", "-Command", cmd], check=True, capture_output=True)
            return True
        except Exception:
            return False
    else:
        # Unix: append to ~/.bashrc or ~/.zshrc if not already present
        try:
            home = Path.home()
            profile = home / (".zshrc" if (home / ".zshrc").exists() else ".bashrc")
            export_line = f'export {name}="{value}"\n'
            existing = profile.read_text(encoding="utf-8") if profile.exists() else ""
            if export_line not in existing:
                with open(profile, "a", encoding="utf-8") as f:
                    f.write(f"\n# AI Workspace Bootstrap\n{export_line}")
            return True
        except Exception:
            return False

def scaffold_topology(root_dir: Path, template_dir: Path) -> Dict[str, Any]:
    """Create missing banks and seed baseline templates and rules."""
    root_dir.mkdir(parents=True, exist_ok=True)
    created_banks = []
    existing_banks = []
    injected_rules = []

    claude_template = template_dir / "claude_pointer.template.md"
    claude_content = claude_template.read_text(encoding="utf-8") if claude_template.exists() else "# CLAUDE.md\nStrictly follows AGENTS.md\n"

    bank_template_map = {
        "Idea_Hub": "bank_agents_idea_hub.template.md",
        "MY_Memories": "bank_agents_memories.template.md",
        "Vibe_Coding": "bank_agents_vibe_coding.template.md",
        "My_Learning": "bank_agents_learning.template.md",
        "Reference_Coding": "bank_agents_reference.template.md"
    }

    for bank_name in REQUIRED_BANKS:
        bank_path = root_dir / bank_name
        if bank_path.exists():
            existing_banks.append(bank_name)
        else:
            bank_path.mkdir(parents=True, exist_ok=True)
            created_banks.append(bank_name)

        # 1. Structure and README seeding
        if bank_name == "Idea_Hub":
            (bank_path / "inbox").mkdir(exist_ok=True)
            (bank_path / "active").mkdir(exist_ok=True)
            (bank_path / "archived").mkdir(exist_ok=True)
            readme_file = bank_path / "README.md"
            if not readme_file.exists():
                template_file = template_dir / "idea_hub_readme.template.md"
                if template_file.exists():
                    readme_file.write_text(template_file.read_text(encoding="utf-8"), encoding="utf-8")

        elif bank_name == "MY_Memories":
            (bank_path / "knowledge" / "profile").mkdir(parents=True, exist_ok=True)
            (bank_path / "knowledge" / "boundary").mkdir(parents=True, exist_ok=True)
            (bank_path / "knowledge" / "projects").mkdir(parents=True, exist_ok=True)
            readme_file = bank_path / "README.md"
            if not readme_file.exists():
                template_file = template_dir / "memory_bank.template.md"
                if template_file.exists():
                    readme_file.write_text(template_file.read_text(encoding="utf-8"), encoding="utf-8")

        elif bank_name == "My_Learning":
            (bank_path / "knowledge_gaps").mkdir(exist_ok=True)
            (bank_path / "deep_study").mkdir(exist_ok=True)
            (bank_path / "labs").mkdir(exist_ok=True)
            readme_file = bank_path / "README.md"
            if not readme_file.exists():
                readme_file.write_text("# My_Learning (技术学习与知识缺口库)\n\n存放技术研究计划、知识缺口登记与深度学习笔记。\n", encoding="utf-8")

        elif bank_name == "Reference_Coding":
            readme_file = bank_path / "README.md"
            if not readme_file.exists():
                readme_file.write_text("# Reference_Coding (外部只读参考代码库)\n\n存放第三方开源项目源码供只读学习，严禁在此进行自研代码开发。\n", encoding="utf-8")

        elif bank_name == "Vibe_Coding":
            readme_file = bank_path / "README.md"
            if not readme_file.exists():
                readme_file.write_text("# Vibe_Coding (自研生产项目库)\n\n存放个人所有自建与生产级独立项目，每个子目录为独立 Git 仓库并由 project-guard 守护。\n", encoding="utf-8")

        # 2. Inject Bank-Level AGENTS.md (if template exists and file doesn't exist)
        if bank_name in bank_template_map:
            agents_file = bank_path / "AGENTS.md"
            if not agents_file.exists():
                tmpl_name = bank_template_map[bank_name]
                rule_tmpl = template_dir / tmpl_name
                if rule_tmpl.exists():
                    agents_file.write_text(rule_tmpl.read_text(encoding="utf-8"), encoding="utf-8")
                    injected_rules.append(f"{bank_name}/AGENTS.md")

        # 3. Inject CLAUDE.md multi-agent pointer (if not present)
        claude_file = bank_path / "CLAUDE.md"
        if not claude_file.exists():
            claude_file.write_text(claude_content, encoding="utf-8")
            injected_rules.append(f"{bank_name}/CLAUDE.md")

    # Set environment variables
    env_root_ok = set_persistent_env("AI_WORKSPACE_ROOT", str(root_dir))
    env_mem_ok = set_persistent_env("MY_MEMORIES_PATH", str(root_dir / "MY_Memories"))

    return {
        "root_dir": str(root_dir),
        "created_banks": created_banks,
        "existing_banks": existing_banks,
        "injected_rules": injected_rules,
        "env_set": {
            "AI_WORKSPACE_ROOT": env_root_ok,
            "MY_MEMORIES_PATH": env_mem_ok
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Bootstrap the 6-bank workspace topology.")
    parser.add_argument("--root-dir", "-r", required=True, help="Target root directory for the 6 workspace banks")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    root_path = Path(args.root_dir).resolve()
    script_dir = Path(__file__).parent.resolve()
    template_dir = script_dir.parent / "templates"

    result = scaffold_topology(root_path, template_dir)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("===============================================================")
        print("           Workspace Bootstrap Topology Initializer            ")
        print("===============================================================")
        print(f"目标根目录 : {result['root_dir']}")
        print(f"已存在工作区: {', '.join(result['existing_banks']) if result['existing_banks'] else '无'}")
        print(f"新建工作区  : {', '.join(result['created_banks']) if result['created_banks'] else '已全部就绪'}")
        print(f"注入规则契约: {', '.join(result['injected_rules']) if result['injected_rules'] else '无新增 (已存在)'}")
        print(f"环境变量注入: AI_WORKSPACE_ROOT={'成功' if result['env_set']['AI_WORKSPACE_ROOT'] else '失败'}, MY_MEMORIES_PATH={'成功' if result['env_set']['MY_MEMORIES_PATH'] else '失败'}")
        print("===============================================================")
        print("[完成] 6 大工作区生态初始化与自举完成！")

if __name__ == "__main__":
    main()
