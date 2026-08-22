---
name: my-memories
description: >-
  Query and inspect user profile, preferences, collaboration boundaries, project context, and architecture specs in D:\MY_Memories.
  Trigger when: (1) retrieving user personal profile or work preferences, (2) checking AI collaboration and CLI boundary rules,
  (3) reading local workspace context or product architecture specifications.
---

# Authoritative Memory Bank (`D:\MY_Memories`)

Query interface and reference index for the user's authoritative personal knowledge base.

---

## 1. Directory & Knowledge Map

| Category | Authority Path | Core Contents |
| :--- | :--- | :--- |
| **Workspace & Projects** | `D:\MY_Memories\knowledge\projects\本地工作区与项目上下文.md` | Workspace boundaries (`D:\Vibe_Coding`, `D:\Reference_Coding`, etc.) and project lifecycle status |
| **User Profile & Habits** | `D:\MY_Memories\knowledge\profile\` | `个人画像.md` (skills, background), `工作与决策偏好.md` (communication style, principles) |
| **AI Collaboration** | `D:\MY_Memories\knowledge\collaboration\AI协作与工具边界.md` | Tool responsibilities (Codex, Claude Code, Kimi CLI), permissions, dispatch contracts |
| **Best Practices** | `D:\MY_Memories\knowledge\practices\` | Standard engineering workflows (e.g. `AI前端设计系统一致性工作流.md`) |
| **Product Specifications** | `D:\MY_Memories\docs\` | Core vision, PRDs, and architecture blueprints |
| **Governance & Security** | `D:\MY_Memories\governance\` | Write auditing, redaction rules, safety policies |
| **Global Knowledge Index** | `D:\MY_Memories\knowledge\_index.yml` | Full index of knowledge items with timestamps and confidence levels |

---

## 2. Query Protocols (Progressive Disclosure)

1. **On-Demand Retrieval**:
   - Never scan the full directory tree.
   - Read `knowledge/_index.yml` or specific target file matching the query intent.
2. **Authority Ladder**:
   - User immediate prompt > `docs/` product definitions > `knowledge/` stable facts > `governance/` rules > Active code/tests in project repo.
3. **Sensitive Data Redaction**:
   - Treat personal identifiers, paths, and keys with `[敏感]内容[敏感]`.