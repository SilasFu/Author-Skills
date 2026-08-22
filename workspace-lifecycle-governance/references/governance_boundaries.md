# 工作区治理边界与项目自包含落盘手册 (Governance Boundaries & Self-Containment)

本手册界定 6 大工作区之间的权责红线，并强制执行**项目自包含文档落盘铁律 (Project Self-Containment Rule)**。

---

## 1. 六大工作区权责边界总览

```text
┌──────────────────────┬─────────────────────────┬──────────────────────────────────────────┐
│ 工作区 (Bank)        │ 唯一权威职责            │ 严禁越权行为 (Anti-Patterns)            │
├──────────────────────┼─────────────────────────┼──────────────────────────────────────────┤
│ 1. Idea_Hub          │ 灵感接收、评估与派发    │ 严禁在此直接编写生产级业务代码           │
│ 2. MY_Memories       │ 跨项目全局画像与通用偏好│ 严禁存放具体项目的 PRD/架构/API 实现细节 │
│ 3. Vibe_Coding       │ 生产项目正式自研代码    │ 严禁放入未经修改的外部第三方代码         │
│ 4. My_Learning       │ 知识盲区登记与深度研读  │ 严禁作为生产业务代码存放区               │
│ 5. Reference_Coding  │ 外部开源优秀项目只读参考│ 严格只读！严禁在此编写自研业务逻辑       │
│ 6. Author-Skills     │ 自研 Agent 技能与治理母体│ 严禁编写特定业务 UI 或琐碎业务轮子       │
└──────────────────────┴─────────────────────────┴──────────────────────────────────────────┘
```

---

## 2. 项目自包含文档落盘铁律 (Project Self-Containment Rule)

在任何项目立项、架构重构或开发中，必须遵守**第一责任落盘点在【项目自身】**：

1. **项目自足性**：任何拉取了该项目 Git 仓库的开发者或 AI Agent，无需依赖外部未公开的黑盒环境，单凭项目自身即可获得完整开发上下文：
   - 需求规格 ➔ `<ProjectRoot>/docs/PRD.md`（模板源：[`project-guard/templates/docs_prd.template.md`](../../project-guard/templates/docs_prd.template.md)）
   - 架构设计 ➔ `<ProjectRoot>/docs/ARCHITECTURE.md`（模板源：[`project-guard/templates/docs_architecture.template.md`](../../project-guard/templates/docs_architecture.template.md)）
   - 技术决策 ➔ `<ProjectRoot>/docs/DECISIONS.md`（模板源：[`project-guard/templates/docs_decisions.template.md`](../../project-guard/templates/docs_decisions.template.md)）
   - 设计系统契约 ➔ `<ProjectRoot>/DESIGN.md`（模板源：[`project-guard/templates/DESIGN.template.md`](../../project-guard/templates/DESIGN.template.md)）
   - 质量与代码门禁 ➔ `<ProjectRoot>/AGENTS.md`（模板源：[`project-guard/templates/AGENTS.template.md`](../../project-guard/templates/AGENTS.template.md)）
   - 多 Agent 桥接 ➔ `<ProjectRoot>/CLAUDE.md`（模板源：[`project-guard/templates/CLAUDE.template.md`](../../project-guard/templates/CLAUDE.template.md)）
   - 派发任务工单 ➔ `<ProjectRoot>/docs/tasks/`（模板源：[`workspace-lifecycle-governance/templates/dispatch_task.template.md`](../templates/dispatch_task.template.md)）
2. **严禁记忆库代管具体项目细节**：
   - `MY_Memories` 仅允许保留一条简要的状态索引（如 `projects/本地工作区与项目上下文.md` 中记录该项目存在及当前阶段）；
   - **严禁把某个项目的具体 API 文档、数据库表结构或业务 PRD 堆进全局记忆库**。
