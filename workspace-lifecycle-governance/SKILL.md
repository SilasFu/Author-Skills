---
name: workspace-lifecycle-governance
description: >-
  Workspace lifecycle governance and decision engine across D:\MY_Memories, D:\My_Learning, D:\Learning_Labs, and D:\Vibe_Coding.
  Trigger on: (1) user knowledge gap detected requiring study registration, (2) project creation vs repo extension decision,
  (3) syncing milestone, boundary change, or architecture decision to memory bank.
---

# Workspace Lifecycle Governance & Decision Engine

Unified execution router for managing state transitions across **Memory (`D:\MY_Memories`)**, **Learning (`D:\My_Learning` / `D:\Learning_Labs`)**, and **Projects (`D:\Vibe_Coding` / `D:\Reference_Coding`)**.

---

## 1. Directory Topology & Single-Truth Routing

| Workspace | Absolute Root | Primary Role | Stored Artifacts |
| :--- | :--- | :--- | :--- |
| **Memory Bank** | `D:\MY_Memories` | Authoritative truth & continuity | Product specs (`docs/`), profiles (`knowledge/profile/`), workspace context (`knowledge/projects/`), governance rules (`governance/`) |
| **Learning Bank** | `D:\My_Learning` | Knowledge acquisition & gap registry | Study roadmaps (`AI学习/`), topic notes, gap logs, reviews |
| **Learning Labs** | `D:\Learning_Labs` | Concept validation & benchmarks | PoC code, test fixtures, benchmark outputs, evaluation datasets |
| **Project Bank** | `D:\Vibe_Coding` | Self-built product codebases | Production apps, core services, integration tests, active contracts |
| **Reference Bank** | `D:\Reference_Coding` | External reference sources (Read-only) | Third-party open-source repos inspected for architecture patterns |
| **Prototyping** | `D:\Vice_Coding` | Ephemeral scratchpads | Throwaway experiments, temporary mockups |

---

## 2. SOP 1: Knowledge Gap Tracking & Learning Loop

### Trigger
Fire when user expresses uncertainty, asks for fundamental explanations, or lacks prerequisite knowledge on:
- AI architecture / RAG / Multi-agent protocols / LLM cost engineering;
- Software design patterns, concurrency, distributed systems, or specialized toolchains;
- Domain business models or regulatory policies.

### Execution Sequence
1. **Target Selection**:
   - AI/Agent topics ➡️ `D:\My_Learning\AI学习/` (active plan: `AI应用与Agent系统学习计划.md` or topic file).
   - Core Engineering ➡️ `D:\My_Learning\Technical_Learning/` (or root study list).
2. **Atomic Entry Format**:
```markdown
### 📌 [知识缺口]：<主题名称>
- **登记时间**：YYYY-MM-DD
- **起因与场景**：<触发任务 / 所在项目>
- **核心盲区**：<需掌握的具体理论、API 或工程机制>
- **攻克目标**：<可检验的产出标准，例如可独立编写该 Adapter / 解释核心原理>
- **验证路径**：在 `D:\Learning_Labs/<experiment-dir>` 编写最小 PoC 验证
- **当前状态**：[ ] 待学习 / [ ] 实验中 / [x] 已掌握
```
3. **User Reminder Output**:
   Emit a high-signal notification block in the chat response:
   > 💡 **知识补全提醒**：在本次任务中发现 `<主题名称>` 存在认知缺口。已登记至 `D:\My_Learning`，建议通过 `D:\Learning_Labs` 进行最小概念验证。

### Completion Criterion
Registration is complete when:
- The Markdown entry is appended to the correct file in `D:\My_Learning`.
- A concise study recommendation card is presented in the current response.

---

## 3. SOP 2: Project Creation vs Feature Extension Decision Engine

### Trigger
Fire when evaluating new feature requests, architecture redesigns, tool requests, or repo initialization.

### Sequential Decision Gates (Reuse-Ladder)
Run each gate in strict sequence. Stop at the first positive match:

1. **Gate 1: Existing Solution Reuse**
   - Check if an existing tool/product solves the problem directly.
   - *Outcome*: Adopt existing tool via standard configuration. Zero code added.
2. **Gate 2: Existing Project Adapter / Plugin Extension**
   - Check if the requirement shares user persona, UI, runtime, or persistence with an existing repo in `D:\Vibe_Coding`.
   - *Outcome*: Add module / CLI adapter / MCP plugin inside the existing repo.
3. **Gate 3: Standalone Project Qualification (All 4 criteria required)**:
   - [ ] **Independent Persona**: Distinct product lifecycle and end-user mental model.
   - [ ] **Architectural Incompatibility**: Distinct runtime stack (e.g. desktop Electron app vs headless backend daemon) where co-locating causes dependency pollution.
   - [ ] **Source-Code Gap Proof**: Confirmed that no external reference in `D:\Reference_Coding` or existing repo can be extended.
   - [ ] **PoC Verification**: Core mechanics already validated in `D:\Vice_Coding` or `D:\Learning_Labs`.
   - *Outcome*: Authorize new repo creation in `D:\Vibe_Coding/<project-name>`.
4. **Fallback: Prototype First**
   - If Gate 3 conditions are not yet fully met, route to `D:\Vice_Coding` or `D:\Learning_Labs` for concept validation first.

### Completion Criterion
Decision is complete when:
- The chosen path, target folder, and evidence against the 4 gates are clearly reported to the user.

---

## 4. SOP 3: Memory Continuity & State Auditing

### Trigger
Fire when:
- A project reaches a milestone, changes status (e.g. active ➡️ read-only archive), or changes architecture boundaries.
- Cross-project engineering standards (Best Practices) are validated.
- User profile, collaboration boundary, or tool permissions evolve.

### Execution Sequence
1. **Locate Target Authority**:
   - Project lifecycle ➡️ `D:\MY_Memories\knowledge\projects\本地工作区与项目上下文.md`
   - Practices ➡️ `D:\MY_Memories\knowledge\practices/`
   - Persona & Preferences ➡️ `D:\MY_Memories\knowledge\profile/`
2. **Single-Truth Revision**:
   - Directly edit the authoritative section. Never create duplicate conflicting summaries.
   - Mask sensitive entities: `[敏感]内容[敏感]`.
   - Maintain frontmatter metadata:
     ```yaml
     ---
     状态: 当前权威
     来源类型: 用户明确指令 / 验证证据
     最后复核: YYYY-MM-DD
     ---
     ```
3. **Index Synchronization**:
   - Update `D:\MY_Memories\knowledge\_index.yml` with the modified file path and updated timestamp.

### Completion Criterion
Memory sync is complete when:
- Authoritative Markdown file in `D:\MY_Memories` reflects the current factual state.
- `_index.yml` contains matching timestamp and status metadata.