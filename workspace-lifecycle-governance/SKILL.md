---
name: workspace-lifecycle-governance
description: >-
  Universal workspace lifecycle governance and decision engine across Memory, Learning, Projects, and References.
  Trigger on: (1) user knowledge gap detected requiring study registration, (2) project creation vs repo extension decision,
  (3) syncing milestone, boundary change, or architecture decision to memory bank.
argument-hint: "gap | reuse | sync"
---

# Workspace Lifecycle Governance & Decision Engine

Universal execution router for managing state transitions and boundary integrity across **Memory Bank**, **Learning Bank**, **Project Bank**, **Reference Bank**, and **Author-Skills**.

---

## 1. 动态拓扑与自感知路由 (Portable Topology Routing)

所有寻址基于环境变量 `$env:AI_WORKSPACE_ROOT` / `$env:MY_MEMORIES_PATH` 或当前工作区自感知相对路径：

| 工作区角色 | 相对路径 / 环境变量锚点 | 核心职责 | 存储规范 |
| :--- | :--- | :--- | :--- |
| **Memory Bank (记忆库)** | `${MY_MEMORIES_PATH}` / `./MY_Memories` | 权威真实源与连续性心智 | 决策偏好 (`knowledge/profile/`), 协作边界 (`knowledge/collaboration/`), 项目上下文 (`knowledge/projects/`), 治理规则 (`governance/`) |
| **Learning Bank (学习库)** | `${AI_WORKSPACE_ROOT}/My_Learning` | 认知缺口登记与系统学习 | 学习路线图 (`AI学习/`), 知识点笔记, 缺口跟踪卡片 |
| **Learning Labs (实验库)** | `${AI_WORKSPACE_ROOT}/Learning_Labs` | 概念验证与技术基准测试 | 最小 PoC 实验代码, 基准评测夹具 |
| **Project Bank (代码库)** | `${AI_WORKSPACE_ROOT}/Vibe_Coding` | 自建正式产品与服务代码 | 生产项目源码, 单元与集成测试, `AGENTS.md` / `DESIGN.md` 契约 |
| **Reference Bank (参考库)** | `${AI_WORKSPACE_ROOT}/Reference_Coding` | 外部开源参考源码 (严格只读) | 仅用于架构与实现模式借鉴, 代码全部自写, 不依赖、不复制 |
| **Author-Skills (技能库)** | `${AI_WORKSPACE_ROOT}/Author-Skills` | 自研与定制技能母体仓库 | 遵循开放标准的 Agent Skill 源码 |

---

## 2. SOP 1: 知识缺口自感知与闭环流转 (Knowledge Gap Loop)

### 触发条件 (Trigger)
当用户在对话或方案推演中表现出对某项底层原理、协议机制、算法或专业领域的认知盲区时，Agent 自动感知并触发：

### 执行步骤
1. **目标文件定位**：
   - AI/Agent 相关缺口 ➡️ `My_Learning/AI学习/` (如 `AI应用与Agent系统学习计划.md`);
   - 核心工程/系统架构缺口 ➡️ `My_Learning/Technical_Learning/`.
2. **标准缺口卡片格式**：
```markdown
### 📌 [知识缺口]：<主题名称>
- **登记时间**：YYYY-MM-DD
- **起因与场景**：<触发任务 / 所在项目>
- **核心盲区**：<需掌握的具体理论、API 或工程机制>
- **攻克目标**：<可检验的产出标准，例如可独立编写该 Adapter / 解释核心原理>
- **验证路径**：在 `Learning_Labs/<experiment-dir>` 编写最小 PoC 验证
- **当前状态**：[ ] 待学习 / [ ] 实验中 / [x] 已掌握
```
3. **高信噪比提醒**：
   在回复中附带一句轻量提醒：
   > 💡 **知识补全已登记**：在本次任务中发现 `<主题名称>` 存在认知盲区，已自动在 `My_Learning` 中建档，建议后续在 `Learning_Labs` 展开最小概念验证。

### 完成标准 (Completion Criterion)
- 缺口条目已追加到目标学习文档；
- 输出包含简明攻克目标的提醒卡片。

---

## 3. SOP 2: 项目创建 vs 存量复用阶梯决策 (Project Reuse-Ladder Engine)

### 触发条件 (Trigger)
当用户提出新功能、新工具、新架构或新建仓库诉求时，强制运行复用阶梯，坚决防止盲目造轮子与项目碎片化：

### 阶梯决策流程（严格按顺序匹配，命中即止）：

1. **第一阶梯：现有工具/标准协议直接解决 (Zero Code)**
   - 评估已有工具（如标准 CLI、现有 MCP Server、系统内置功能）是否能直接满足；
   - *结论*：配置并直接使用，不新建任何代码仓库。
2. **第二阶梯：现有项目模块/插件扩展 (Repo Extension)**
   - 检查该需求是否与 `Vibe_Coding` 中的现有项目共享用户群体、技术栈、持久层或宿主运行时；
   - *结论*：在已有项目中新增 Package / Module / CLI Adapter，禁止立新项目。
3. **第三阶梯：独立立项资格审查 (需同时满足全部 4 项硬门禁)**：
   - [ ] **独立用户心智**：具有完全独立的产品形态与生命周期；
   - [ ] **运行时不兼容**：技术栈或运行宿主存在物理冲突（例如桌面 GUI 与无头 Daemon），强行合并会导致严重依赖污染；
   - [ ] **参考库查重证明**：已在 `Reference_Coding` 中确认无现成可用模式；
   - [ ] **最小 PoC 验证**：核心机制已在 `Learning_Labs` 或临时原型中验证通过。
   - *结论*：授权在 `Vibe_Coding/<new-project>` 中建立新仓库。

### 完成标准 (Completion Criterion)
- 输出 4 项门禁的逐项核验结果；
- 明确给出推荐路径与目标工作区目录。

---

## 4. SOP 3: 权威记忆连续性与索引同步 (Memory Sync & Governance)

### 触发条件 (Trigger)
当项目发生里程碑变更、架构边界调整、用户新增决策偏好，或验证了新的跨项目最佳实践时：

### 执行步骤
1. **定位唯一权威文档**：
   - 用户画像与偏好 ➡️ `MY_Memories/knowledge/profile/`
   - 工具协作与边界 ➡️ `MY_Memories/knowledge/collaboration/`
   - 项目上下文与状态 ➡️ `MY_Memories/knowledge/projects/`
   - 工程最佳实践 ➡️ `MY_Memories/knowledge/practices/`
2. **单一事实源修订 (CUR-008)**：
   - 直接修改权威 Markdown 原文，严禁新建平行的日志或冗余总结；
   - 敏感信息使用 `[敏感]内容[敏感]` 标记；
   - 更新 Frontmatter `最后复核: YYYY-MM-DD`。
3. **全局索引与 Git 提交**：
   - 同步更新 `MY_Memories/knowledge/_index.yml` 中的主题映射与时间戳；
   - 提交 Git Commit，使记忆在跨设备间同步生效。

### 完成标准 (Completion Criterion)
- 权威正文直接修改完成且无平行冗余文件；
- `_index.yml` 索引同步完成且 Git Commit 成功。
