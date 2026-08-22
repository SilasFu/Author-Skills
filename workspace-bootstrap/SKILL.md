---
name: workspace-bootstrap
description: >-
  Universal workspace ecosystem bootstrapper and multi-device topology initializer.
  Trigger on: (1) cold-starting on a brand-new machine or environment,
  (2) establishing/linking the 6-bank workspace topology (Idea Hub, Memory, Projects, Learning, Reference, Skills),
  (3) generating portable workspace mounts and agent configuration rules.
argument-hint: "init | status | link"
---

# Workspace Bootstrap (工作区生态自举与拓扑初始化引擎)

Universal ecosystem bootstrapper for cold-starting, multi-device syncing, workspace topology initialization, and multi-agent configuration links across **Idea Hub**, **Memory Bank**, **Project Bank**, **Learning Bank**, **Reference Bank**, and **Author-Skills**.

---

## 核心模式与触发指令

| 模式 | 用户典型触发语 | 核心使命与底层工具支撑 |
| :--- | :--- | :--- |
| **init (冷启动自举)** | “在新电脑上初始化工作区”、“配置多 Agent 工作区”、“/workspace-bootstrap init” | 运行 `scripts/setup_topology.py` 自动化创建 6 大工作区骨架、注入模板并持久化环境变量。 |
| **status (拓扑健康巡检)** | “检查工作区拓扑状态”、“查看当前绑定的仓库与路径”、“/workspace-bootstrap status” | 运行 `scripts/check_topology.py` 毫秒级扫描 6 大工作区存在性、Git 状态与环境变量配置。 |
| **link (多 Agent 规则挂载)** | “重新挂载 Agent 规则”、“将工作区规则注入到新安装的工具”、“/workspace-bootstrap link” | 运行 `scripts/link_agents.py` 智能探测本机 Antigravity/Cursor/Claude 等环境并建立规则连接。 |

---

## 模式一：init（全生态冷启动与自适应建库 SOP）

当在新电脑或新环境中执行 `/workspace-bootstrap init` 时：

### 1. 探测或确认工作区根目录
- Windows 优先探测多分区（如 `D:\` 或 `C:\Workspaces`）；
- Mac/Linux 默认推荐 `~/Workspaces` 或 `$HOME/Projects`；
- 向用户确认根目录绝对路径（如 `--root-dir D:\`）。

### 2. 执行自动化拓扑初始化脚本
参考 [`references/topology_spec.md`](references/topology_spec.md) 了解 6 大工作区拓扑与权责规约，执行内置自举脚本：
```bash
python <path-to-skill>/scripts/setup_topology.py --root-dir <RootPath>
```
脚本将自动完成：
1. 创建缺失的 6 大工作区目录（`Idea_Hub`, `MY_Memories`, `Vibe_Coding`, `My_Learning`, `Reference_Coding`, `Author-Skills`）；
2. 依据各工作区专属模板注入工作区级治理规则（`AGENTS.md`）；
3. 注入多 Agent 规则桥接契约（`CLAUDE.md`，SSOT 指向 `AGENTS.md`）；
4. 依据 [`templates/idea_hub_readme.template.md`](templates/idea_hub_readme.template.md) 注入灵感中枢看板与 3 级流转目录（`inbox/`, `active/`, `archived/`）；
5. 依据 [`templates/memory_bank.template.md`](templates/memory_bank.template.md) 注入权威记忆库初始种子骨架；
6. 跨平台持久化注入系统用户级环境变量 `AI_WORKSPACE_ROOT` 与 `MY_MEMORIES_PATH`。

### 3. 多 Agent 准入环境自动探测与关联
执行：
```bash
python <path-to-skill>/scripts/link_agents.py --skills-dir <RootPath>/Author-Skills
```
参考 [`references/agent_mount_matrix.md`](references/agent_mount_matrix.md) 确认各 Agent 挂载状态。

**完成标准 (Completion Criterion)**：
- 6 大工作区目录全部就绪，各 Bank 专属 `AGENTS.md` 与 `CLAUDE.md` 规则契约骨架落盘；
- 环境变量在操作系统持久层生效；
- 向用户输出结构化自举完成报告。

---

## 模式二：status（拓扑健康巡检 SOP）

当执行 `/workspace-bootstrap status` 时：

### 1. 运行拓扑健康诊断脚本
```bash
python <path-to-skill>/scripts/check_topology.py
```
脚本将自动检测：
1. 6 大工作区物理目录是否存在；
2. 各工作区的 Git Remote 关联与未提交修改状态（Clean / Dirty）；
3. 校验环境变量 `AI_WORKSPACE_ROOT` 与 `MY_MEMORIES_PATH` 是否与实际路径完全一致。

### 2. 输出拓扑健康卡片 (Topology Card)
依据脚本输出，向用户呈现标准的 6 大工作区表格化健康卡片，并对缺失项给出修复指引。

**完成标准 (Completion Criterion)**：扫描完毕并呈现结构化状态表格，异常项给出修复建议。

---

## 模式三：link（多 Agent 规则重挂载 SOP）

当用户安装了新 IDE 或更新了 Agent 配置时执行 `/workspace-bootstrap link`：

1. 运行 `python <path-to-skill>/scripts/link_agents.py`；
2. 探测已安装的 Antigravity、Cursor、Claude Code、Windsurf 等开发工具；
3. 参考 [`references/agent_mount_matrix.md`](references/agent_mount_matrix.md) 输出各工具规则挂载状态与安装引导。

**完成标准 (Completion Criterion)**：输出多 Agent 探测报告，向用户确认规则挂载就绪。
