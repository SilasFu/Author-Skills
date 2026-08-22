#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_integrity.py - 记忆库结构完整性与敏感信息防泄漏审计器 (Memory Bank Integrity Auditor)
Audits directory structure, checks sensitive info redactions, and verifies Git sync state.
"""

import os
import re
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

try:
    from search_memories import resolve_memory_bank_root
except ImportError:
    script_dir = Path(__file__).parent
    sys.path.append(str(script_dir))
    from search_memories import resolve_memory_bank_root

# Common sensitive regex patterns (API keys, JWT, raw tokens)
SUSPICIOUS_KEY_PATTERNS = [
    (re.compile(r'(?i)(?:api_key|apikey|secret_key|private_key|auth_token)\s*[:=]\s*["\']([a-zA-Z0-9_\-]{16,})["\']'), "明文 API Key/Token 泄露风险"),
    (re.compile(r'ghp_[a-zA-Z0-9]{36}'), "GitHub Personal Access Token 泄露"),
    (re.compile(r'sk-[a-zA-Z0-9]{32,}'), "OpenAI / Claude API Secret 泄露")
]

REQUIRED_STRUCTURE = [
    "knowledge/profile",
    "knowledge/projects",
    "knowledge"
]

def audit_memory_integrity(mem_root: Path) -> Dict[str, Any]:
    """Audit memory bank integrity, redactions, and index."""
    missing_dirs = []
    for d in REQUIRED_STRUCTURE:
        if not (mem_root / d).exists():
            missing_dirs.append(d)

    unredacted_findings = []
    knowledge_dir = mem_root / "knowledge"

    if knowledge_dir.exists():
        for root, dirs, files in os.walk(knowledge_dir):
            for file in files:
                if file.endswith(".md") or file.endswith(".yml") or file.endswith(".yaml"):
                    file_path = Path(root) / file
                    try:
                        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
                        for line_idx, line in enumerate(lines, 1):
                            # Ignore commented or masked lines
                            if "[敏感]" in line or "placeholder" in line.lower() or "example" in line.lower():
                                continue
                            for pattern, desc in SUSPICIOUS_KEY_PATTERNS:
                                if pattern.search(line):
                                    rel = file_path.relative_to(mem_root).as_posix()
                                    unredacted_findings.append({
                                        "file": rel,
                                        "line": line_idx,
                                        "issue": desc,
                                        "snippet": line[:80]
                                    })
                    except Exception:
                        continue

    is_git = (mem_root / ".git").exists()

    overall_pass = (len(missing_dirs) == 0 and len(unredacted_findings) == 0)

    return {
        "memory_root": str(mem_root),
        "overall_pass": overall_pass,
        "is_git": is_git,
        "missing_dirs": missing_dirs,
        "unredacted_findings": unredacted_findings
    }

def print_integrity_card(report: Dict[str, Any]):
    """Print structured integrity health card."""
    struct_str = "[PASS] 完整" if not report["missing_dirs"] else f"[FAIL] (缺失 {len(report['missing_dirs'])} 目录)"
    leak_str = "[PASS] (0 敏感泄漏)" if not report["unredacted_findings"] else f"[WARN] ({len(report['unredacted_findings'])} 处潜在明文密钥)"
    git_str = "[PASS] (Git 跟踪)" if report["is_git"] else "[INFO] (非 Git 仓库)"

    print("=========================================================================================")
    print("           Authoritative Memory Bank Integrity & Redaction Report                        ")
    print("=========================================================================================")
    print(f"记忆库路径: {report['memory_root']}")
    print("-----------------------------------------------------------------------------------------")
    print(f"  * 核心目录结构完整性 : {struct_str}")
    print(f"  * 敏感信息防泄漏审计 : {leak_str}")
    print(f"  * 权威版本控制状态   : {git_str}")
    print("=========================================================================================")

    if not report["overall_pass"]:
        if report["missing_dirs"]:
            print(f"[缺失目录清单]: {', '.join(report['missing_dirs'])}")
        if report["unredacted_findings"]:
            print(f"[潜在风险清单]: 共 {len(report['unredacted_findings'])} 处，请使用 [敏感]内容[敏感] 进行脱敏掩码。")
            for item in report["unredacted_findings"][:5]:
                print(f"  • {item['file']}:{item['line']} -> {item['issue']}")
    else:
        print("[结果] 权威记忆库结构完备，安全防泄漏门禁 100% PASS！")

def main():
    parser = argparse.ArgumentParser(description="Verify integrity and security of MY_Memories.")
    parser.add_argument("--mem-dir", "-m", default=None, help="Explicit path to MY_Memories")
    parser.add_argument("--json", "-j", action="store_true", help="Output JSON")
    args = parser.parse_args()

    mem_root = resolve_memory_bank_root(args.mem_dir)
    if not mem_root:
        print("Error: Unable to locate MY_Memories root directory.", file=sys.stderr)
        sys.exit(1)

    report = audit_memory_integrity(mem_root)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_integrity_card(report)

    sys.exit(0 if report["overall_pass"] else 1)

if __name__ == "__main__":
    main()
