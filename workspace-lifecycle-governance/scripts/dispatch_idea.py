#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dispatch_idea.py - 灵感中枢需求跨区派发与归档器 (Idea Hub Dispatcher)
Packages drafts from Idea_Hub/inbox into standard task contracts, dispatches to target repo docs/tasks/, and archives.
"""

import os
import sys
import json
import shutil
import argparse
from datetime import datetime
from pathlib import Path
from typing import Dict, Any

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

def dispatch_task(
    idea_hub_dir: Path,
    target_project_dir: Path,
    task_name: str,
    in_scope: str,
    out_of_scope: str,
    acceptance_criteria: str,
    source_file_name: str = ""
) -> Dict[str, Any]:
    """Dispatch idea task to target project and archive source draft."""
    today_str = datetime.now().strftime("%Y%m%d")
    clean_task_name = task_name.replace(" ", "_").lower()
    task_file_name = f"TASK-{today_str}-{clean_task_name}.md"

    tasks_dir = target_project_dir / "docs" / "tasks"
    tasks_dir.mkdir(parents=True, exist_ok=True)
    target_task_path = tasks_dir / task_file_name

    task_content = f"""# 任务规格书: {task_name} (Task Specification)

> 来源: 灵感总控中枢派发 (Idea Hub Dispatch)
> 派发日期: {datetime.now().strftime('%Y-%m-%d')}
> 目标工作区: `{target_project_dir.name}`

---

## 1. 需求范围与边界 (Scope)

### ✅ 必须包含 (In-Scope)
{in_scope or '- 实现核心功能逻辑与用户交互'}

### ❌ 明确排除 (Out-of-Scope)
{out_of_scope or '- 暂不引入重型第三方未评估依赖'}

---

## 2. 客观可验证验收标准 (Acceptance Criteria)

{acceptance_criteria or '- [ ] 核心功能代码编写完成且单文件 <= 200 行\n- [ ] 编译器/类型检查 0 报错通过\n- [ ] 视觉与交互符合 DESIGN.md 规范'}

---

## 3. 一键启动提词 (Downstream Prompt)
```text
@docs/tasks/{task_file_name} 请按照该任务规格书与本项目 AGENTS.md 契约开始执行。
```
"""
    target_task_path.write_text(task_content.strip() + "\n", encoding="utf-8")

    # Archive original if exists in inbox
    archived = False
    if source_file_name:
        inbox_source = idea_hub_dir / "inbox" / source_file_name
        archived_dir = idea_hub_dir / "archived"
        archived_dir.mkdir(parents=True, exist_ok=True)
        if inbox_source.exists():
            shutil.move(str(inbox_source), str(archived_dir / source_file_name))
            archived = True

    return {
        "task_name": task_name,
        "target_task_file": str(target_task_path),
        "target_relative": f"docs/tasks/{task_file_name}",
        "archived_source": archived,
        "downstream_prompt": f"@{target_project_dir.name}/docs/tasks/{task_file_name} 请按照该任务规格书与本项目 AGENTS.md 契约开始执行。"
    }

def main():
    parser = argparse.ArgumentParser(description="Dispatch an idea to target workspace docs/tasks.")
    parser.add_argument("--name", "-n", required=True, help="Task name")
    parser.add_argument("--target-dir", "-t", required=True, help="Target project root directory")
    parser.add_argument("--idea-hub-dir", "-i", default=None, help="Idea_Hub root directory")
    parser.add_argument("--in-scope", default="", help="In-scope bullet points")
    parser.add_argument("--out-scope", default="", help="Out-of-scope bullet points")
    parser.add_argument("--criteria", default="", help="Acceptance criteria")
    parser.add_argument("--source-file", default="", help="Source draft file in inbox")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON")
    args = parser.parse_args()

    target_path = Path(args.target_dir).resolve()
    if args.idea_hub_dir:
        hub_path = Path(args.idea_hub_dir).resolve()
    else:
        root_env = os.environ.get("AI_WORKSPACE_ROOT")
        if root_env:
            hub_path = Path(root_env) / "Idea_Hub"
        else:
            hub_path = Path(".").resolve().parent / "Idea_Hub"

    result = dispatch_task(
        idea_hub_dir=hub_path,
        target_project_dir=target_path,
        task_name=args.name,
        in_scope=args.in_scope,
        out_of_scope=args.out_scope,
        acceptance_criteria=args.criteria,
        source_file_name=args.source_file
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("=========================================================================================")
        print("              Idea Hub Cross-Workspace Task Dispatched Successfully                      ")
        print("=========================================================================================")
        print(f"目标任务文件 : {result['target_task_file']}")
        print(f"原始草稿归档 : {'已归档至 Idea_Hub/archived/' if result['archived_source'] else '直接派发'}")
        print("-----------------------------------------------------------------------------------------")
        print("下游 Agent 一键启动执行提词:")
        print(f"  {result['downstream_prompt']}")
        print("=========================================================================================")

if __name__ == "__main__":
    main()
