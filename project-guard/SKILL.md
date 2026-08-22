---
name: project-guard
description: >-
  Universal project lifecycle guardian, health doctor, and rule self-evolution engine across all coding agents.
  Trigger on: (1) initializing a project with AGENTS.md, DESIGN.md contracts, and compiler gates,
  (2) diagnosing/repairing codebase sprawl (>200 lines), blackbox memory pollution, or design drift,
  (3) evolving rules and immunizing the entire ecosystem when a user corrects the agent or sets a new preference.
argument-hint: "init | doctor | evolve"
---

# Project Guard (项目守护、健康自愈与规则自进化引擎)

Universal active guardian, diagnostic doctor, and rule self-evolution engine for engineering quality, design consistency, and permanent error-immunity across all coding agents (Antigravity, Codex, Cursor, Claude Code, OpenCode).

---

## 核心模式与触发指令

| 模式 | 用户典型触发词 | 核心使命与底层工具支撑 |
| :--- | :--- | :--- |
| **init (机制植入)** | “帮这个项目初始化规范”、“植入质量机制”、“/project-guard init” | 基于 `templates/AGENTS.template.md` 与 `templates/DESIGN.template.md`，参数化注入生成项目级规范与门禁。 |
| **doctor (健康体检与自愈)** | “跑一下项目体检”、“检查代码行数与规范”、“清理野样式和暗状态”、“/project-guard doctor” | 运行 `scripts/doctor.py` 进行毫秒级确定性全维度体检，自动执行大文件垂直切片与野样式收敛。 |
| **evolve (规则进化与生态免疫)** | “以后不要这样做了”、“记住这个习惯/偏好”、“把这个教训沉淀进规则”、“/project-guard evolve” | 依据 `references/rule_taxonomy.md` 提取原子化硬规则，精准路由回写权威源并 Git 固化，实现全生态永久免疫。 |

---

## 模式一：init（项目规范与机制自适应植入 SOP）

当在任意新项目或未受控项目中执行 `/project-guard init` 时：

### 1. 技术栈与构建环境自动探测
- 检查构建工具与包管理器：`pnpm` (`pnpm-lock.yaml`), `npm` (`package-lock.json`), `yarn` (`yarn.lock`), `cargo` (`Cargo.toml`), `poetry/pip` (`pyproject.toml`), `go` (`go.mod`)；
- 探测检验命令：`typecheck` / `lint` / `test` / `check`。

### 2. 参数化生成项目级 `AGENTS.md`
- 读取本技能内置的 [`templates/AGENTS.template.md`](templates/AGENTS.template.md)；
- 替换 `{{PROJECT_NAME}}`、`{{TECH_STACK}}`、`{{CHECK_COMMAND}}` 等插槽并落盘至项目根目录；
- 固化 **业务单文件 ≤ 200 行** 硬限制与 **0 报错编译器自检** 门禁。

### 3. 探测与绑定单一设计契约（Single DESIGN.md SSOT）
- 优先探测项目是否已有设计规范（`docs/DESIGN.md` 或 `DESIGN.md`）；
- **若已存在**：将其作为唯一视觉源，严禁覆盖或重复创建；
- **若不存在**：读取 [`templates/DESIGN.template.md`](templates/DESIGN.template.md)，参考 [`references/state_matrix.md`](references/state_matrix.md) 生成标准中性设计系统与 8 大交互状态规范。

### 4. 生成多 Agent 规则桥接契约（CLAUDE.md SSOT Pointer）
- 读取 [`templates/CLAUDE.template.md`](templates/CLAUDE.template.md)；
- 替换插槽并落盘至根目录 `CLAUDE.md`，使 Claude Code / Cursor / Antigravity 实现无缝统一规则驱动。

### 5. 注入自包含工程文档矩阵骨架 (Self-Contained Docs Matrix)
- 依据 [`templates/docs_prd.template.md`](templates/docs_prd.template.md)、[`templates/docs_architecture.template.md`](templates/docs_architecture.template.md)、[`templates/docs_decisions.template.md`](templates/docs_decisions.template.md)；
- 在 `<ProjectRoot>/docs/` 目录下生成 `PRD.md`、`ARCHITECTURE.md` 与 `DECISIONS.md` 初始骨架，确保项目上下文 100% 自足。

**完成标准 (Completion Criterion)**：根目录存在 `AGENTS.md` 与 `CLAUDE.md`，存在且仅存在 1 份 `DESIGN.md`，`docs/` 自包含文档矩阵就绪，编译器自检命令验证通过。

---

## 模式二：doctor（项目健康诊断、防腐与自愈 SOP）

当执行 `/project-guard doctor` 时：

### 1. 运行确定性体检脚本套件
执行内置的确定性诊断编排脚本：
```bash
python <path-to-skill>/scripts/doctor.py --path .
```
脚本将以毫秒级精度并发完成以下 4 项诊断：
1. **代码巨石扫描 (`audit_sprawl.py`)**：列出所有超过 **200 行** 的源码文件；
2. **设计漂移扫描 (`audit_design_drift.py`)**：检出手写十六进制色值（`#...`）与未经受控的内联样式；
3. **黑盒暗状态检查**：排查未提交的私有缓存与黑盒记忆文件；
4. **编译器/类型自检**：执行原生构建与类型检查。

### 2. 自动化垂直切片与防腐自愈
- **针对超标大文件（>200 行）**：
  - 强制执行三层切片重构：UI 渲染层 (`Component.tsx`)、业务与副作用层 (`useComponent.ts`)、类型契约层 (`types.ts`)；
- **针对野样式与硬编码颜色**：
  - 对照 `DESIGN.md` 语义 Token 批量收敛替换（如 `bg-background`、`text-muted-foreground`）；
- **针对编译器报错**：
  - 自动捕获错误堆栈并闭环修复，直至 `python <path-to-skill>/scripts/doctor.py` 退出码为 0。

### 3. 输出结构化健康卡片 (Health Card)
向用户输出标准卡片，标明所有检查项均通过并列出已自愈的文件清单。

**完成标准 (Completion Criterion)**：运行 `doctor.py` 退出码为 0（所有体检项 100% PASS），向用户呈现结构化健康卡片。

---

## 模式三：evolve（规则自进化与全生态免疫 SOP）

当用户在对话中指出 Agent 的错误（如“不要用弹窗”、“以后这种数据一律用本地缓存”）或表达新偏好时：

### 1. 提炼原子规则（Atomic Rule Extraction）
查阅 [`references/rule_taxonomy.md`](references/rule_taxonomy.md)，将用户纠偏提炼为标准四要素原子规则：
`【触发条件】+【强制要求】+【明确禁止】+【验证方式】`。

### 2. 精准路由回写权威事实源（SSOT Routing）
- **个人全局偏好/交互习惯** ➔ 回写至 `MY_Memories/knowledge/profile/工作与决策偏好.md`；
- **视觉/UI/交互禁忌** ➔ 追加至当前项目 `DESIGN.md` 的 `## 5. 设计规范禁忌 (Do's and Don'ts)`；
- **代码质量/架构约束** ➔ 追加至当前项目 `AGENTS.md` 的 `## 3. 质量与架构禁忌`。

### 3. 自动 Git 固化（跨设备全生态永久免疫）
自动执行 Git 提交：
```bash
git commit -m "chore(governance): evolve rules to permanently immunize against <pattern>"
```
**免疫效果**：规则一经提交，全生态所有接入该仓库的 Agent（Cursor/Claude/Antigravity）在下一轮任务均自动受控，**实现同一错误全生命周期绝对不再犯**！

**完成标准 (Completion Criterion)**：新规则已精准写入权威文件，Git 提交完成，向用户输出免疫确认卡片。
