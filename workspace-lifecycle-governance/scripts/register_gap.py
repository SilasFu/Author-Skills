#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
register_gap.py - 知识盲区标准化建档与登记器 (Knowledge Gap Registrar)
Creates and tracks structured knowledge gap cards in My_Learning bank.
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def format_gap_card(
    topic: str,
    scene: str,
    blind_spot: str,
    goal: str,
    poc_path: str = ""
) -> str:
    """Render a standard markdown knowledge gap card."""
    today_str = datetime.now().strftime("%Y-%m-%d")
    poc_str = poc_path or f"My_Learning/deep_study/{topic.replace(' ', '_').lower()}"
    return f"""
### 📌 [知识缺口]：{topic}
- **登记时间**：{today_str}
- **起因与场景**：{scene or '在任务推演与方案设计中发现'}
- **核心盲区**：{blind_spot or '需掌握的核心原理、协议机制或系统架构'}
- **攻克目标**：{goal or '能够独立阐明底层机制并编写验证代码'}
- **验证路径**：在 `{poc_str}` 展开最小原型 PoC 验证
- **当前状态**：[ ] 待学习 / [ ] 实验中 / [x] 已掌握
"""

def register_gap(
    learning_dir: Path,
    topic: str,
    scene: str,
    blind_spot: str,
    goal: str,
    category: str = "technical"
) -> Dict[str, Any]:
    """Register knowledge gap into My_Learning target directory."""
    target_dir = learning_dir / "knowledge_gaps"
    target_dir.mkdir(parents=True, exist_ok=True)

    file_name = f"GAP-{datetime.now().strftime('%Y%m%d')}-{topic.replace(' ', '_').lower()}.md"
    target_file = target_dir / file_name

    card_content = format_gap_card(topic, scene, blind_spot, goal)

    try:
        target_file.write_text(card_content.strip() + "\n", encoding="utf-8")
        written = True
    except Exception as e:
        written = False

    return {
        "topic": topic,
        "category": category,
        "target_file": str(target_file),
        "written": written,
        "card_content": card_content.strip()
    }

def main():
    parser = argparse.ArgumentParser(description="Register a knowledge gap card into My_Learning.")
    parser.add_argument("--topic", "-t", required=True, help="Knowledge gap topic name")
    parser.add_argument("--scene", "-s", default="", help="Context / project where gap was triggered")
    parser.add_argument("--blind-spot", "-b", default="", help="Specific theoretical or architectural blind spot")
    parser.add_argument("--goal", "-g", default="", help="Verifiable mastery goal")
    parser.add_argument("--learning-dir", "-l", default=None, help="Path to My_Learning directory")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON")
    args = parser.parse_args()

    if args.learning_dir:
        learn_path = Path(args.learning_dir).resolve()
    else:
        root_env = os.environ.get("AI_WORKSPACE_ROOT")
        if root_env:
            learn_path = Path(root_env) / "My_Learning"
        else:
            learn_path = Path(".").resolve().parent / "My_Learning"

    result = register_gap(
        learning_dir=learn_path,
        topic=args.topic,
        scene=args.scene,
        blind_spot=args.blind_spot,
        goal=args.goal
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=========================================================================================")
        print("                 Knowledge Gap Registration (知识缺口自动建档卡片)                       ")
        print("=========================================================================================")
        print(result["card_content"])
        print("=========================================================================================")
        if result["written"]:
            print(f"[成功] 知识缺口已成功落盘至: {result['target_file']}")
        else:
            print("[提示] 卡片已生成，请手动追加至目标学习笔记。")

if __name__ == "__main__":
    main()
