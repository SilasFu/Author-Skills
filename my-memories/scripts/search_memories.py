#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
search_memories.py - 权威记忆库切片发现与精准检索器 (Memory Bank Slicer & Searcher)
Extracts targeted memory slices by category or keywords without polluting context with full files.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

CATEGORY_MAP = {
    "profile": [
        "knowledge/profile/个人画像.md",
        "knowledge/profile/工作与决策偏好.md"
    ],
    "collaboration": [
        "knowledge/collaboration/AI协作与工具边界.md",
        "knowledge/boundary/协作边界规范.md"
    ],
    "projects": [
        "knowledge/projects/本地工作区与项目上下文.md"
    ],
    "practices": [
        "knowledge/practices/AI前端设计系统一致性工作流.md"
    ]
}

def resolve_memory_bank_root(custom_path: Optional[str] = None) -> Optional[Path]:
    """Dynamically resolve MY_Memories root directory from env or relative paths."""
    if custom_path:
        p = Path(custom_path).resolve()
        if p.exists():
            return p

    # 1. Check MY_MEMORIES_PATH env var
    env_mem = os.environ.get("MY_MEMORIES_PATH")
    if env_mem and Path(env_mem).exists():
        return Path(env_mem).resolve()

    # 2. Check AI_WORKSPACE_ROOT env var
    env_root = os.environ.get("AI_WORKSPACE_ROOT")
    if env_root:
        p = Path(env_root) / "MY_Memories"
        if p.exists():
            return p.resolve()

    # 3. Check relative parent paths
    current = Path(".").resolve()
    for parent in [current, current.parent, current.parent.parent]:
        p = parent / "MY_Memories"
        if p.exists():
            return p.resolve()

    # 4. Fallback check common Windows drives
    for drive in ["D:\\", "C:\\", "E:\\"]:
        p = Path(drive) / "MY_Memories"
        if p.exists():
            return p.resolve()

    return None

def search_category(mem_root: Path, category: str, query: str = "") -> List[Dict[str, Any]]:
    """Search or slice by category."""
    files_to_check = CATEGORY_MAP.get(category, [])
    results = []

    for rel_path in files_to_check:
        full_path = mem_root / rel_path
        if full_path.exists():
            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
                if query:
                    # Filter matching sections
                    lines = content.splitlines()
                    matching_lines = [l for l in lines if query.lower() in l.lower()]
                    if matching_lines:
                        results.append({
                            "category": category,
                            "file": rel_path,
                            "full_path": str(full_path),
                            "match_count": len(matching_lines),
                            "snippet": "\n".join(matching_lines[:15])
                        })
                else:
                    results.append({
                        "category": category,
                        "file": rel_path,
                        "full_path": str(full_path),
                        "content": content
                    })
            except Exception as e:
                continue

    return results

def full_text_search(mem_root: Path, query: str) -> List[Dict[str, Any]]:
    """Perform quick keyword search across all knowledge documents."""
    results = []
    knowledge_dir = mem_root / "knowledge"
    if not knowledge_dir.exists():
        return results

    for root, dirs, files in os.walk(knowledge_dir):
        for file in files:
            if file.endswith(".md") or file.endswith(".yml") or file.endswith(".yaml"):
                file_path = Path(root) / file
                try:
                    content = file_path.read_text(encoding="utf-8", errors="replace")
                    if query.lower() in content.lower():
                        rel = file_path.relative_to(mem_root).as_posix()
                        lines = [l.strip() for l in content.splitlines() if query.lower() in l.lower()]
                        results.append({
                            "file": rel,
                            "full_path": str(file_path),
                            "matches": len(lines),
                            "snippets": lines[:5]
                        })
                except Exception:
                    continue

    return results

def main():
    parser = argparse.ArgumentParser(description="Query and slice authoritative memories.")
    parser.add_argument("--category", "-c", choices=["profile", "collaboration", "projects", "practices", "all"], help="Category to retrieve")
    parser.add_argument("--query", "-q", default="", help="Keyword query")
    parser.add_argument("--mem-dir", "-m", default=None, help="Explicit path to MY_Memories directory")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON")
    args = parser.parse_args()

    mem_root = resolve_memory_bank_root(args.mem_dir)
    if not mem_root:
        print(f"Error: Unable to locate MY_Memories root directory. Please set MY_MEMORIES_PATH or AI_WORKSPACE_ROOT.", file=sys.stderr)
        sys.exit(1)

    if args.category and args.category != "all":
        results = search_category(mem_root, args.category, args.query)
    elif args.query:
        results = full_text_search(mem_root, args.query)
    else:
        results = []
        for cat in ["profile", "collaboration", "projects", "practices"]:
            results.extend(search_category(mem_root, cat))

    if args.json:
        print(json.dumps({
            "memory_root": str(mem_root),
            "result_count": len(results),
            "results": results
        }, ensure_ascii=False, indent=2))
    else:
        print("=========================================================================================")
        print("                 Authoritative Memory Bank Search & Slice Report                         ")
        print("=========================================================================================")
        print(f"权威记忆库源头 : {mem_root}")
        print(f"检索分类/关键词 : {args.category or '全量'} / '{args.query or '全部'}'")
        print("-----------------------------------------------------------------------------------------")

        if not results:
            print("[无匹配] 未找到符合条件的记忆切片。")
        else:
            for r in results:
                if "content" in r:
                    print(f"\n📄 [文件: {r['file']}]")
                    print(r["content"])
                    print("-----------------------------------------------------------------------------------------")
                else:
                    print(f"\n🔍 [匹配文件: {r['file']}] (命中 {r.get('matches', r.get('match_count', 0))} 处)")
                    snippets = r.get("snippets", [r.get("snippet", "")])
                    for s in snippets:
                        print(f"  • {s}")

        print("=========================================================================================")

if __name__ == "__main__":
    main()
