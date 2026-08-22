# Idea_Hub 灵感中枢治理规约 (AGENTS.md)

## 1. 工作区定位与职责边界

本目录为个人 AI 工作区生态的 **灵感与需求总控中枢 (Idea Hub)**。
- **核心职能**：统一收集碎片化需求、轻量创意、功能草案与待评估的想法；
- **流转机制**：草稿进入 `inbox/` ➔ 评估规划后进入 `active/` ➔ 派发至具体工作区后归档至 `archived/`；
- **跨区派发**：
  - 业务项目需求 ➔ 派发至 `Vibe_Coding/<Project>`
  - 技术原理盲区 ➔ 派发至 `My_Learning`
  - 规则与机制自进化 ➔ 派发至 `Author-Skills`

---

## 2. 核心行为准则与红线 (Do's and Don'ts)

### 2.1 严厉禁止 (Don'ts)
- ❌ **严禁在此编写生产业务代码**：本仓库只存放需求描述、PRD 草案与任务卡片，不存放项目业务实现；
- ❌ **严禁未归档遗留**：一旦需求通过 `workspace-lifecycle-governance dispatch` 派发至目标项目，原始草稿必须移动至 `archived/`；
- ❌ **严禁破坏目录结构**：保持 `inbox/`、`active/`、`archived/` 3 级标准流转。

### 2.2 推荐实践 (Do's)
- ✅ 鼓励使用结构化 Markdown 记录想法（包含：背景、痛点、预期目标、潜在方案）；
- ✅ 善用 `/workspace-lifecycle-governance dispatch` 自动化打包派发任务契约。
