# Author-Skills 仓库开发与维护准则 (AGENTS.md)

## 1. 仓库定位与职责边界

本仓库是个人 AI Agent 技能的**唯一自研与定制源头仓库（Source of Authoring）**。
- **物理路径**：`D:\Vibe_Coding\Author-Skills`
- **核心定位**：专注于工作区生态的**机制建立、自我修正与规则自进化**（元治理母体引擎）；
- **严格边界**：
  - 严禁放入未修改的外部公版技能（外部技能统一归档于 `My-Skills`）；
  - 严禁编写琐碎的业务代码轮子或特定 UI 布局代码；
  - 源码中严禁包含任何个人私有数据、敏感信息或特定 GitHub 账号硬编码。

---

## 2. 技能编写与修改必须遵循的硬门禁

进入本仓库修改或新增任何 Skill 时，必须严格遵守 [`docs/SKILL_STANDARDS.md`](docs/SKILL_STANDARDS.md)：

1. **单一事实源 (SSOT)**：同一规则或方法论只能在一个权威位置定义；
2. **渐进披露 (Progressive Disclosure)**：`description` 精准前置抓手词，正文不超过 300 行，大型参考放入 `references/`；
3. **闭环完成标准 (Completion Criteria)**：每个 SOP 必须定义客观可检验的完成指标；
4. **格式合规检查**：修改后必须运行 Frontmatter 与 YAML 合规检查；
5. **项目文档同步**：新增或修改技能时，必须在同一变更中同步更新 `docs/PRD.md`、`docs/CHANGELOG.md` 与 `README.md`。

---

## 3. 标准维护与发布流水线

1. 本地技能源码编写与静态审计（核对 `writing-for-agents` 标准）；
2. 同步更新 `docs/` 目录文档矩阵；
3. 规范 Git 提交（遵循 Conventional Commits 规范）；
4. 推送至远程 GitHub 私有/开源仓库；
5. 规范 Git 提交并推送至 GitHub 远程；本地各 Agent 运行环境的技能分发与更新由用户自行执行，AI 严禁越权修改本地配置目录。
