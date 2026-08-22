# Author-Skills 版本演进记录 (CHANGELOG)

## [0.4.0] - 2026-08-23

### 双轨制预置模板与视觉发布治理 (Dual-Track Visual Publishing Governance)
- **新增 `visual-publishing-governance`**：支持 `produce`（内置黄金版式免参考图）、`lock`（参考图锁版定制）与 `audit`（布局漂移与交付审计）三大模式；
- **全站 7 大专栏视觉矩阵**：沉淀 [`references/category_theme_matrix.md`](../visual-publishing-governance/references/category_theme_matrix.md)，为 `aooby.cn` 涵盖的 AI Agent 元治理、Vibe Coding、作品与成果展示、产品经理、设计系统、教材授课、极速入门 7 大维度注入专属 Design Tokens、排版骨架与 3D 插画 Prompt；
- **内置版式预置库**：新增 `cover_hero`、`body_matrix`、`body_workflow` 与 `tail_qr_cta` 等经过几何验证的 1440×1920 标准版式；
- **资产角色门禁**：原生支持 `avatar`（头像保留）、`qr-code`（二维码插槽）、`brand-logo`，默认对 `identity-info` 强制 `embed: false` 拦截，将平台自动水印标记为排除证据；
- **确定性稳定套件**：升级 `validate_visual_job.py`、`compare_layout.py` 与 `audit_outputs.py`；
- **回归自测**：`self_test.py` 覆盖预置模板任务、二维码插槽、布局容差、素材漏分类、未批准合同、身份截图误嵌、旧稿污染与禁用水印等 10 大场景，100% 通过。

## [0.3.2] - 2026-08-22

### 全量技能静态审计与上下文指针加固 (Skill Audit & Context Pointer Hardening)
- **渐进披露指针闭环**：在 `workspace-bootstrap`、`project-guard` 与 `workspace-lifecycle-governance` 的 `SKILL.md` 中补齐对 `topology_spec.md`、`state_matrix.md` 与 `dispatch_task.template.md` 的显式指针；
- **零硬编码彻底清理**：消除 `rule_taxonomy.md` 中的残留绝对路径，全系规则 100% 实现 `$MY_MEMORIES_PATH` 与相对路径自感知；
- **全脚本静态与运行自检**：全量 11 个 Python 脚本通过 `--help` 与全场景运行测试，`project-guard doctor` 审计全部 PASS；
- **新增新手极速入门教程**：沉淀 [`docs/BEGINNER_GUIDE.md`](BEGINNER_GUIDE.md)，为零基础与小白用户提供通俗比喻、0 到 1 实战路径与开箱即用提词速查表。

---

## [0.3.1] - 2026-08-22

### 全生态规则闭环与多 Agent SSOT 桥接升级 (Bank-Level Rules & Multi-Agent SSOT Linking)
- **6 大工作区专属规则注入**：在 `workspace-bootstrap` 沉淀 `bank_agents_idea_hub.template.md`、`bank_agents_memories.template.md`、`bank_agents_learning.template.md`、`bank_agents_reference.template.md`、`bank_agents_vibe_coding.template.md` 与 `claude_pointer.template.md` 模板；
- **自举脚本升级**：`setup_topology.py` 在冷启动创建 6 大工作区时，自动注入各 Bank 专属的 `AGENTS.md` 治理规约与 `CLAUDE.md` 桥接文件，实现工作区根目录规则自动化受控；
- **项目自包含文档矩阵模板沉淀**：在 `project-guard` 沉淀 `docs_prd.template.md`、`docs_architecture.template.md`、`docs_decisions.template.md` 与 `CLAUDE.template.md`；升级 `project-guard init`，一键生成项目根目录规则与 `docs/` 自足上下文矩阵；
- **工作区治理边界手册对齐**：更新 `governance_boundaries.md`，显式建立自包含文档矩阵与标准模板的关联；
- **Author-Skills 自身规则补齐**：为母体仓库根目录补齐 `CLAUDE.md`，无缝继承 `AGENTS.md` 规则。

---

## [0.3.0] - 2026-08-22

### 复合工程化架构升级 (Composite Tool-Augmented Skill Architecture)
- **确立工业级复合 Skill 架构**：彻底打破单一 `SKILL.md` 的纯 Prompt 局限，升级为 `SKILL.md` (轻量调度) + `scripts/` (确定性脚本) + `templates/` (金标模板) + `references/` (渐进披露手册) 复合架构；
- **Project Guard 工程化加固**：引入 `audit_sprawl.py`（超长文件扫描）、`audit_design_drift.py`（前端野样式扫描）与 `doctor.py`（多维度一键体检与健康卡片生成）；沉淀 `AGENTS.template.md`、`DESIGN.template.md`；抽离 `references/rule_taxonomy.md` 与 `references/state_matrix.md`；
- **Workspace Bootstrap 工程化加固**：引入 `check_topology.py`（6 大工作区拓扑巡检）、`setup_topology.py`（跨平台自动化建库与持久环境变量注入）与 `link_agents.py`（多 Agent 准入环境检测与挂载）；沉淀 `idea_hub_readme.template.md`、`memory_bank.template.md`；抽离 `references/topology_spec.md` 与 `references/agent_mount_matrix.md`；
- **Workspace Lifecycle Governance 工程化加固**：引入 `evaluate_reuse.py`（4 级立项复用阶梯与 4 大硬门禁判定）、`register_gap.py`（知识盲区标准化建档）与 `dispatch_idea.py`（灵感跨区派发与归档）；沉淀 `knowledge_gap.template.md`、`reuse_report.template.md`、`dispatch_task.template.md`；抽离 `references/reuse_ladder_matrix.md` 与 `references/governance_boundaries.md`；
- **My Memories 工程化加固**：引入 `search_memories.py`（毫秒级自感知分类切片检索工具，彻底消除 `D:\` 盘符硬编码）与 `verify_integrity.py`（结构完整性与敏感信息防泄漏审计器）；沉淀 `memory_entry.template.md`、`preference_rule.template.md`；抽离 `references/confidence_ladder.md` 与 `references/query_protocols.md`；
- **Windows 跨平台编码防御**：为所有 CLI 脚本增加 Windows 控制台 UTF-8 弹性编码自适应与异常防御。

---

## [0.2.0] - 2026-08-22

### 重大架构升级 (Meta-Governance Realignment)
- **确立元治理母体定位**：剥离琐碎业务轮子，纯粹聚焦于“机制建立、自我修正、自我改进”三大核心使命；
- **新增冷启动自举技能**：新建 `workspace-bootstrap`，支持跨设备一键交互式拉通五大工作区拓扑，消除盘符硬编码；
- **重构流转决策技能**：`workspace-lifecycle-governance` 全面升级为相对寻址与环境变量自感知，强化知识缺口自感知与项目复用阶梯决策；
- **重构守护与自进化技能**：`project-guard` 升级 `evolve` 模式，实现对话纠偏自动提炼规则、回写权威库并 Git 提交，形成跨设备全生态免疫；
- **建立项目级文档矩阵**：正式建立 `docs/` 目录，补齐 `PRD.md`、`ARCHITECTURE.md`、`SKILL_STANDARDS.md`、`CHANGELOG.md` 与 `VERIFICATION.md`。

---

## [0.1.0] - 2026-08-21

### 初始版本发布
- 初始建立三大自研技能：`project-guard`、`workspace-lifecycle-governance`、`my-memories`；
- 遵循 `writing-for-agents` 规范，实现初始规则植入与体检能力。
