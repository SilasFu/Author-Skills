---
name: workspace-lifecycle-governance
description: >-
  Universal workspace lifecycle governance and decision engine across Memory, Learning, Projects, References, and Idea Hub.
  Trigger on: (1) user knowledge gap detected requiring study registration, (2) project creation vs repo extension decision,
  (3) syncing milestone, boundary change, or architecture decision to memory bank, (4) idea hub dispatching to target workspace.
argument-hint: "gap | reuse | sync | dispatch"
---

# Workspace Lifecycle Governance & Decision Engine

Universal execution router for managing state transitions and boundary integrity across **Idea Hub**, **Memory Bank**, **Learning Bank**, **Project Bank**, **Reference Bank**, and **Author-Skills**.

---

## 核心模式与触发指令

| 模式 | 用户典型触发词 | 核心使命与底层工具支撑 |
| :--- | :--- | :--- |
| **gap (知识缺口登记)** | “我不懂这个底层机制”、“登记这个技术盲区”、“/workspace-lifecycle-governance gap” | 运行 `scripts/register_gap.py`，自动基于 `templates/knowledge_gap.template.md` 在 `My_Learning/` 建档。 |
| **reuse (立项复用决策)** | “我想做个新功能/工具”、“这个需要新建仓库吗”、“/workspace-lifecycle-governance reuse” | 运行 `scripts/evaluate_reuse.py`，依据 `references/reuse_ladder_matrix.md` 强制核验 4 级阶梯与 4 大立项硬门禁。 |
| **dispatch (灵感跨区派发)** | “把这个需求分派到项目”、“评估 Inbox 里的想法”、“/workspace-lifecycle-governance dispatch” | 运行 `scripts/dispatch_idea.py`，自动将 `Idea_Hub/inbox/` 打包为 `docs/tasks/` 任务契约并完成归档。 |
| **sync (权威记忆同步)** | “同步项目里程碑到记忆库”、“更新架构边界”、“/workspace-lifecycle-governance sync” | 依据 `references/governance_boundaries.md` 遵循项目自包含落盘铁律，精准同步 `MY_Memories` 索引。 |

---

## 模式一：gap（知识盲区感知与闭环建档 SOP）

当在对话中发现底层原理、协议或算法盲区时：

### 1. 自动化登记知识缺口
执行内置脚本：
```bash
python <path-to-skill>/scripts/register_gap.py --topic "<主题名称>" --scene "<触发任务/项目>" --blind-spot "<核心盲区>" --goal "<检验目标>"
```
脚本将自动在 `My_Learning/knowledge_gaps/` 下生成 `GAP-YYYYMMDD-<topic>.md` 追踪卡片。

### 2. 输出高信噪比提醒
向用户输出结构化卡片与简短提醒：
> 💡 **知识补全已建档**：已在 `My_Learning` 中登记 `<主题名称>`，建议后续在 `Learning_Labs` 展开最小 PoC 验证。

**完成标准 (Completion Criterion)**：缺口卡片落盘成功，输出结构化卡片与验证路径。

---

## 模式二：reuse（项目创建 vs 存量复用阶梯决策 SOP）

当用户提出新功能、新工具或新建仓库诉求时：

### 1. 运行复用阶梯决策脚本
```bash
python <path-to-skill>/scripts/evaluate_reuse.py --title "<需求标题>" --desc "<需求描述>"
```
脚本将严格自顶向下判定：
- **Level 1 (Zero Code)**：现有标准 CLI / MCP 工具直接解决 ➔ 不新建代码；
- **Level 2 (Repo Extension)**：与 `Vibe_Coding` 存量项目共享技术栈/运行时 ➔ 存量模块扩展；
- **Level 3 (Author-Skills)**：属于跨项目规则与治理机制 ➔ 回写母体技能仓库；
- **Level 4 (New Standalone Project)**：必须**同时 100% 满足 4 大硬门禁**（独立用户心智、运行时物理隔离、外部参考查重、最小 PoC 验证通过）。

### 2. 输出决策报告
读取 [`templates/reuse_report.template.md`](templates/reuse_report.template.md)，向用户呈现逐项核验结果与推荐工作区路径。

**完成标准 (Completion Criterion)**：输出 4 级阶梯结论与 4 大门禁核验表，明确指定目标工作区。

---

## 模式三：dispatch（灵感总控跨区派发 SOP）

当在 `Idea_Hub` 处理用户灵感或需求草稿时：

### 1. 执行跨区自动化派发脚本
```bash
python <path-to-skill>/scripts/dispatch_idea.py --name "<任务名称>" --target-dir "<目标项目根路径>" --source-file "<inbox草稿文件名>"
```
脚本将自动完成：
1. 依据 [`templates/dispatch_task.template.md`](templates/dispatch_task.template.md) 在目标项目 `<Project>/docs/tasks/` 下生成标准任务契约 `TASK-YYYYMMDD-<name>.md`；
2. 将 `Idea_Hub/inbox/` 中的原始草稿移动至 `Idea_Hub/archived/`；
3. 输出下游 Agent 一键执行提词。

**完成标准 (Completion Criterion)**：目标项目自身 `docs/tasks/` 落盘任务契约，草稿完成归档，输出一键启动提词。

---

## 模式四：sync（权威记忆连续性同步 SOP）

当项目发生里程碑变更或架构决策调整时：

1. **项目自包含优先**：第一责任先落盘在目标项目自身的 `<Project>/docs/` 矩阵中；
2. **记忆库轻量索引**：仅在 `MY_Memories/knowledge/projects/本地工作区与项目上下文.md` 中追加或更新一条状态索引；
3. **严禁代管**：严禁将具体项目的 PRD/架构源码写入记忆库；
4. **Git 固化**：提交 Git Commit，实现跨设备同步。

**完成标准 (Completion Criterion)**：项目自身文档完备，记忆库轻量索引更新并完成 Git 提交。
