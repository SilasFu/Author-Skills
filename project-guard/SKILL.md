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

| 模式 | 用户典型触发词 | 核心使命 |
| :--- | :--- | :--- |
| **init (机制植入)** | “帮这个项目初始化规范”、“植入质量机制”、“/project-guard init” | 探测技术栈，自动生成项目级 `AGENTS.md`，绑定单一 `DESIGN.md` 设计契约，固化单文件 200 行限制与编译器硬门禁。 |
| **doctor (健康体检与自愈)** | “跑一下项目体检”、“检查代码行数与规范”、“清理野样式和暗状态”、“/project-guard doctor” | 扫描 >200 行超长文件并垂直切片拆分、扫描硬编码野样式、清理工具黑盒暗状态、执行 0 报错编译器自检。 |
| **evolve (规则进化与生态免疫)** | “以后不要这样做了”、“记住这个习惯/偏好”、“把这个教训沉淀进规则”、“/project-guard evolve” | 自动捕获负向偏好或新原则，原子化提取后回写进 `MY_Memories` 或项目 `AGENTS.md`，Git 固化实现全设备永久免疫。 |

---

## 模式一：init（项目规范与机制自适应植入 SOP）

当在任意新项目或未受控项目中执行 `/project-guard init` 时：

### 1. 技术栈与环境自动探测
- **构建与包管理**：`pnpm-lock.yaml` (pnpm), `package-lock.json` (npm), `yarn.lock` (yarn), `Cargo.toml` (cargo), `pyproject.toml` (uv/poetry/pip), `go.mod` (go)；
- **UI 与框架体系**：React, Next.js, Vue, Tailwind, shadcn/ui, Radix 等；
- **编译与校验命令**：`typecheck`, `build`, `lint`, `test`。

### 2. 自动生成/补齐项目级 `AGENTS.md`
在项目根目录生成专属于该项目的 `AGENTS.md` 刚性约束：
- **单文件行数硬限制**：所有业务与 UI 单文件严格不超过 **200 行**；超过必须按三层架构切分（UI 组件 `Component.tsx`、业务逻辑 `useComponent.ts`、类型契约 `types.ts`）；
- **编译器硬门禁**：完成代码编写后，必须自动运行原生编译检查（如 `pnpm typecheck` / `cargo check`），0 报错才准交工；
- **零黑盒私有记忆**：严禁将项目逻辑存入工具私有 Memory，一切上下文以项目文件为准；
- **视觉先行与防跑偏**：涉及新界面时，必须优先确认 `DESIGN.md` 与状态矩阵（8 大状态），严禁凭空发挥。

### 3. 探测与绑定单一设计系统契约（Single DESIGN.md SSOT）
- **探测已有规范**：优先检查 `docs/DESIGN.md` ➔ `DESIGN.md` ➔ 现有全局样式；
- **若已存在设计文件**：**绝对禁止覆盖或创建第二份副本**，将其作为全项目唯一视觉真实源，仅补齐 Do/Don't 与语义 Token 映射；
- **若完全不存在**：生成标准 `DESIGN.md`，固化灰阶中性基调、8px 节奏与去卡片化原则。

**完成标准 (Completion Criterion)**：根目录存在 `AGENTS.md`，存在且仅存在 1 份 `DESIGN.md`，编译器自检命令验证通过。

---

## 模式二：doctor（项目健康诊断、防腐与自愈 SOP）

当执行 `/project-guard doctor` 时，自动执行全维度体检并自愈：

### 1. 巨石代码体检与垂直切片自愈 (Modularity & Size Audit)
- 扫描项目源码（排除 `node_modules`, `dist`, `.git`, `build`）；
- 检出所有超过 **200 行** 的大文件；
- **自动自愈动作**：按“视图层 (UI)、状态与副作用 (Hook/Service)、数据结构 (Types)”进行垂直切片重构，生成独立小文件。

### 2. 设计规范漂移与野样式体检 (Design Drift Audit)
- 扫描组件中手写的十六进制色值（如 `#1e1e24`, `rgba(...)`）及未受控的内联样式；
- **自动自愈动作**：批量修正为 `DESIGN.md` 中定义的语义 Token 类（如 `bg-background`, `text-muted-foreground`）。

### 3. 工具私有黑盒暗状态体检 (Anti-Blackbox Audit)
- 检查是否存在未提交的私有缓存、私有对话摘要或外部不可追溯的状态；
- 确保所有项目上下文 100% 存在于当前 Git 仓库中。

### 4. 0 报错编译器自检 (Zero-Error Verification)
- 自动执行项目编译与类型检查命令；
- 若出现报错，自动捕获编译器错误堆栈并循环修复，直至 0 报错。

### 5. 输出健康卡片 (Health Card)
```text
┌─────────────────────────────────────────────────────────────┐
│ Project Guard Doctor Report                                 │
├──────────────────────────────┬──────────────────────────────┤
│ • 单文件健康度 (≤ 200 lines)  │ 100% PASS (已垂直切片 1 文件)│
│ • 设计 Token 遵从度          │ 100% PASS (已纠正 2 处野样式)│
│ • 黑盒暗状态检查             │ 0 违规 (Pure File-based SSOT)│
│ • 编译器自检                 │ 0 Errors (PASS)              │
└──────────────────────────────┴──────────────────────────────┘
```

**完成标准 (Completion Criterion)**：完成 4 大体检项，自动修复落地，编译器命令退出码为 0，向用户呈现结构化健康卡片。

---

## 模式三：evolve（规则自进化与全生态免疫 SOP）

当用户在对话中指出 Agent 的错误（如“不要用弹窗”、“以后这种数据一律用本地缓存”）或表达新偏好时：

### 1. 提炼原子规则（Atomic Rule Extraction）
将用户的纠偏或偏好提炼为**不可歧义的正面/负面硬规则**：
- 规则格式：`【分类】+【触发场景】+【强制执行要求】+【明确禁止项】`。

### 2. 精准回写权威事实源（Single-Truth Revision）
- 若属于 **个人全局偏好/架构方法论** ➔ 自动回写至 `MY_Memories/knowledge/profile/工作与决策偏好.md`；
- 若属于 **设计与 UI 禁忌** ➔ 自动回写至当前项目 `DESIGN.md` 的 `## Do's and Don'ts`；
- 若属于 **代码工程/架构规范** ➔ 自动追加至当前项目 `AGENTS.md` 的 `## 质量与架构禁忌`。

### 3. 自动 Git Commit（跨设备生态免疫固化）
- 自动执行 `git add` 并提交：
  ```bash
  git commit -m "chore(governance): evolve rules to permanently immunize against <issue-pattern>"
  ```
- **免疫效果**：一旦提交，该规则永久生效。无论未来哪个 Agent（Codex/Kimi/Claude）、在哪个设备接手，都会在第一行读取到该规则，**实现全生命周期同一错误绝对不再犯**！

**完成标准 (Completion Criterion)**：新规则已精准写入对应权威文件，Git 提交完成，向用户输出免疫确认卡片。
