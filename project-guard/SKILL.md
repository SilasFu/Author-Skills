---
name: project-guard
description: >-
  Universal project lifecycle guardian and doctor across all AI agents.
  Trigger when: (1) initializing a newly created or imported project with AGENTS.md and DESIGN.md,
  (2) diagnosing/repairing codebase sprawl, modularity violations (>200 lines), or design drift,
  (3) evolving and immunizing project rules after a problem occurs.
argument-hint: "init | doctor | evolve"
---

# Project Guard (通用项目生命周期守护与诊断修复技能)

Universal active guardian and diagnostic engine for engineering quality, design consistency, and rule evolution across all coding agents (Claude Code, Codex, Cursor, Antigravity, OpenCode).

---

## 什么时候调用此 Skill（触发指令）

| 模式 | 用户典型触发词 | 核心动作 |
| :--- | :--- | :--- |
| **init (初始化植入)** | “帮这个项目初始化规范”、“规范化新项目”、“植入质量机制”、“/project-guard init” | 自动检测技术栈，生成项目级 AGENTS.md，优先继承已有设计系统（严禁覆盖已有 Token），固化编译器与防腐门禁。 |
| **doctor (体检与修复)** | “跑一下项目诊断”、“检查代码行数与规范”、“界面写丑了帮我体检”、“/project-guard doctor” | 扫描 >200 行超长文件、扫描硬编码野样式、运行编译器自检并给出/执行垂直切片重构方案。 |
| **evolve (规则纠偏进化)** | “以后不要这样做了”、“记住这个设计偏好”、“把这个教训沉淀进规则”、“/project-guard evolve” | 提取用户的负向偏好或架构教训，永久追加写入 AGENTS.md 或 DESIGN.md，实现同一错误永久免疫。 |

---

## 模式一：init（新项目初始化与机制植入 SOP）

当用户在任意新项目或刚用第三方工具初始化的项目中触发 init 时，执行以下步骤：

### 1. 技术栈与环境自动探测
- 检测包管理器：pnpm-lock.yaml ➔ pnpm, package-lock.json ➔ npm, yarn.lock ➔ yarn, Cargo.toml ➔ cargo, pyproject.toml ➔ poetry/uv/pip。
- 检测前端框架与 UI 库：React, Next.js, Vue, Tailwind, shadcn/ui, Radix 等。
- 检测编译/类型检查脚本：typecheck / test / lint。

### 2. 自动生成/补齐项目级 AGENTS.md
在项目根目录生成（或增补）专属于该项目的 AGENTS.md，必须包含：
- **单文件行数限制**：组件单文件不超过 200 行，必须拆分 Component.tsx、useComponent.ts 与 types.ts。
- **编译器硬门禁**：写完代码必须自动运行项目原生编译命令（如 pnpm typecheck / cargo check），0 报错才准交工。
- **歧义与线框先行**：需求模糊或涉及新界面时，禁止直接写代码，强制先输出 ASCII 线框图或弹出单选题。
- **1 秒回退支持**：界面不满意时支持 git restore . 瞬间无损恢复。

### 3. 探测与补齐前端设计契约（若存在前端）
- **优先继承原则（Preserve Existing Tokens First）**：
  - 初始化时，**必须首先探测**项目中是否已存在设计系统文档（如 `DESIGN.md`、`docs/DESIGN.md`、`docs/design/DESIGN.md` 或已有的 Tailwind / CSS Token）。
  - **若已存在设计系统**：**严禁全量覆盖或篡改原有的色板 Token、字体与设计哲学！** 必须保持项目原有设计资产的绝对权威，仅做“增量补齐”（检查并增补去卡片化原则、信息密度要求、负向设计禁忌章节），并将 `AGENTS.md` 中的设计指针正确关联至该已有文件。
  - **若完全不存在设计文件**：才在 `docs/design/DESIGN.md` 中生成基准设计契约模板，固化中性灰阶基调、去卡片化与出版级排版规则。

### 4. 验证与交付
- 运行一次类型检查或编译命令，确认当前项目无语法报错。
- 输出初始化报告，向用户展示生成的 AGENTS.md 与 DESIGN.md 路径。

**完成标准**：根目录存在 AGENTS.md，设计契约（已继承原有或新就绪）就绪，编译器自检命令验证通过。

---

## 模式二：doctor（项目健康诊断与修复 SOP）

当项目在迭代过程中出现“代码变乱、界面失控、性能变差”时，用户触发 doctor 执行以下体检：

### 1. 架构与文件行数体检（Modularity Audit）
- 扫描项目所有源码文件（排除 node_modules, dist, .git）。
- 找出所有超过 **200 行** 的巨石组件/模块。
- **自动修复动作**：按“视图（UI）、状态（Hook）、数据契约（Types）”三层架构，提出拆分方案并自动重构为独立小文件。

### 2. 设计规范漂移体检（Design Drift Audit）
- 扫描组件中的硬编码颜色值（如手写的十六进制色 #8B5CF6、野样式内联 style）。
- **自动修复动作**：将其批量替换回 DESIGN.md 中定义的语义 Token 类（如 bg-surface, text-muted-foreground）。

### 3. 编译器与潜在 Regression 巡检（Zero-Error Check）
- 执行项目原生编译与测试命令（如 pnpm typecheck / pnpm test）。
- 若有报错，自动捕获编译器输出并循环修复，直至 0 报错。

### 4. 输出健康卡片（Health Card）
```text
┌──────────────────────────────────────────────────────────┐
│  Project Doctor Report                                   │
├──────────────────────────────┬───────────────────────────┤
│ • 文件体积健康度 (<200 lines) │ 95% 通过 (已拆分 2 个巨石组件)  │
│ • 设计 Token 遵从度          │ 100% 吻合 (已纠正 3 处野样式)  │
│ • 编译器与类型检查           │ 0 Errors (PASS)           │
└──────────────────────────────┴───────────────────────────┘
```

**完成标准**：完成 3 大体检，自动修复落地，编译器命令退出码为 0，向用户呈现健康卡片。

---

## 模式三：evolve（规则纠偏与免疫进化 SOP）

当用户对某个生成结果表达不满（如“这个弹窗太挤了”、“以后表单不要放侧边栏”）时触发：

### 1. 提取负向偏好原子条目
将用户的吐槽或指令转化为一条可执行的“永久禁忌/约束规则”。
- 例如：*“表单组件一律采用独立抽屉面板（Drawer），严禁直接内嵌在窄侧边栏中。”*

### 2. 永久写入项目治理文档
- 若属于设计偏好 ➔ 追加至 docs/design/DESIGN.md 的 ## 负向设计禁忌 章节；
- 若属于工程/代码偏好 ➔ 追加至 AGENTS.md 的 ## 质量与架构禁忌 章节。

### 3. Git 固化提交
- 自动执行 git commit -m "chore(governance): evolve project rules based on user feedback"。
- 从下一轮开始，所有进入该项目的 Agent 都会在第一行读取到这条新规则，永久免疫该错误。

**完成标准**：偏好写入规则文件，Git 提交完成，向用户确认规则已永久生效。
