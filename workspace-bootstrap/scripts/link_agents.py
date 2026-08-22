#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
link_agents.py - 多 Agent 准入环境检测与规则挂载器 (Multi-Agent Linker)
Detects installed AI coding agent environments and verifies/links rule mounts.
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

def detect_agent_environments() -> List[Dict[str, Any]]:
    """Detect installed Agent IDEs and tools on the local machine."""
    home = Path.home()
    agents = []

    # 1. Google Antigravity / Gemini CLI
    gemini_dir = home / ".gemini"
    if gemini_dir.exists():
        skills_dir = gemini_dir / "config" / "skills"
        agents.append({
            "name": "Google Antigravity / Gemini CLI",
            "key": "antigravity",
            "installed": True,
            "config_path": str(gemini_dir),
            "skills_path": str(skills_dir) if skills_dir.exists() else str(gemini_dir / "skills"),
            "mount_type": "Skills Directory / Config Rules"
        })
    else:
        agents.append({
            "name": "Google Antigravity / Gemini CLI",
            "key": "antigravity",
            "installed": False,
            "config_path": str(gemini_dir),
            "mount_type": "Skills Directory"
        })

    # 2. Cursor IDE
    cursor_dir = home / ".cursor"
    cursor_appdata = home / "AppData" / "Roaming" / "Cursor" if sys.platform == "win32" else home / ".config" / "Cursor"
    cursor_installed = cursor_dir.exists() or cursor_appdata.exists()
    agents.append({
        "name": "Cursor IDE",
        "key": "cursor",
        "installed": cursor_installed,
        "config_path": str(cursor_dir if cursor_dir.exists() else cursor_appdata),
        "mount_type": "Project .cursorrules / AGENTS.md"
    })

    # 3. Claude Code
    claude_dir = home / ".claude"
    claude_config = home / ".config" / "claude-code"
    claude_installed = claude_dir.exists() or claude_config.exists()
    agents.append({
        "name": "Claude Code CLI",
        "key": "claude_code",
        "installed": claude_installed,
        "config_path": str(claude_dir if claude_dir.exists() else claude_config),
        "mount_type": "Global CLAUDE.md / Skills"
    })

    # 4. Windsurf / Codeium
    windsurf_dir = home / ".windsurf"
    windsurf_appdata = home / "AppData" / "Roaming" / "Windsurf" if sys.platform == "win32" else home / ".config" / "Windsurf"
    windsurf_installed = windsurf_dir.exists() or windsurf_appdata.exists()
    agents.append({
        "name": "Windsurf IDE",
        "key": "windsurf",
        "installed": windsurf_installed,
        "config_path": str(windsurf_dir if windsurf_dir.exists() else windsurf_appdata),
        "mount_type": "Global .windsurfrules / AGENTS.md"
    })

    return agents

def print_agent_mount_card(agents: List[Dict[str, Any]], skills_src: Path):
    """Render structured Agent Mount Status Card."""
    print("=========================================================================================")
    print("                 Multi-Agent Environment Detection & Mount Status                       ")
    print("=========================================================================================")
    print(f"自研技能源头 (Source) : {skills_src}")
    print("-----------------------------------------------------------------------------------------")
    print(f"{'Agent 工具名称':<32} | {'安装状态':<10} | {'规则挂载机制':<32}")
    print("-----------------------------------------------------------------------------------------")

    installed_count = 0
    for ag in agents:
        status_str = "[OK] 已安装" if ag["installed"] else "[--] 未探测到"
        if ag["installed"]:
            installed_count += 1
        print(f"{ag['name']:<32} | {status_str:<10} | {ag['mount_type']:<32}")

    print("=========================================================================================")
    print(f"[统计] 本地探测到 {installed_count} 个可用 Agent 环境。")
    print("[提示] 本地 Agent 技能分发请通过 `skills-manager` 或在用户配置根目录建立指向 `Author-Skills` 的挂载。")

def main():
    parser = argparse.ArgumentParser(description="Detect installed Agent environments and verify rule mounts.")
    parser.add_argument("--skills-dir", "-s", default=".", help="Path to Author-Skills repository")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")
    args = parser.parse_args()

    skills_path = Path(args.skills_dir).resolve()
    agents = detect_agent_environments()

    if args.json:
        print(json.dumps({
            "skills_source": str(skills_path),
            "agents": agents
        }, ensure_ascii=False, indent=2))
    else:
        print_agent_mount_card(agents, skills_path)

if __name__ == "__main__":
    main()
