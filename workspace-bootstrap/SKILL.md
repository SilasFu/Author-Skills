---
name: workspace-bootstrap
description: >-
  Universal workspace ecosystem bootstrapper and multi-device topology initializer.
  Trigger on: (1) cold-starting on a brand-new machine or environment,
  (2) establishing/linking the 5-bank workspace topology (Memory, Projects, Learning, Reference, Skills),
  (3) generating portable workspace mounts and agent configuration rules.
argument-hint: "init | status | link"
---

# Workspace Bootstrap (工作区生态一键自举与跨设备拉通技能)

Universal orchestration engine for establishing and linking the full 5-bank workspace topology (**Memory**, **Projects**, **Learning**, **Reference**, **Author-Skills**) on any clean machine, cross-platform OS, or single-drive environment.

---

## 核心定位与原则

1. **100% 通用中立**：纯净的方法论与自举工具，不硬编码任何个人姓名、私人路径或特定 GitHub 账号。
2. **私有资产绝对隔离**：运行时通过交互式引导或环境变量，动态绑定用户自己的私有 Git 仓库，确保数据所有权与权限隔离。
3. **消除路径死锁**：支持任意盘符（C盘/D盘/Mac/Linux）、单分区及多目录拓扑，全面采用自感知相对寻址与环境变量锚点。

---

## 什么时候调用此 Skill

| 场景 | 用户典型触发词 | 核心动作 |
| :--- | :--- | :--- |
| **全生态冷启动 (init)** | “在新电脑初始化我的工作区”、“一键拉通我的生态环境”、“/workspace-bootstrap init” | 交互式引导绑定 5 大私有仓库，建立工作区拓扑，自动挂载到已安装的 Agent 环境。 |
| **状态与健康检查 (status)** | “检查工作区拓扑状态”、“查看当前绑定的仓库与路径”、“/workspace-bootstrap status” | 探测当前 5 大工作区的存在性、Git Remote 状态、环境变量与挂载有效性。 |
| **多 Agent 重新挂载 (link)** | “重新挂载 Agent 规则”、“将工作区规则注入到新安装的工具”、“/workspace-bootstrap link” | 将全局规则与项目级契约无损注入到 Cursor, Antigravity, Claude Code, Codex 等工具。 |

---

## 模式一：init（全生态冷启动与自适应建库 SOP）

当在新电脑或新环境中执行 `/workspace-bootstrap init` 时，依次执行以下 4 步交互引导：

### 步骤 1：工作区根目录定位（Root Directory Detection）
探测并向用户确认本地工作区根目录：
- Windows 优先探测多分区（如 `D:\` 或 `C:\Workspaces`）；
- Mac/Linux 默认推荐 `~/Workspaces` 或 `$HOME/Projects`；
- 用户可直接回车使用推荐路径，或输入自定义绝对路径。

### 步骤 2：五大工作区交互式绑定（Private Instance Binding）

按照标准拓扑结构，逐一引导用户绑定属于自己的私有资产：

```text
┌────────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│ 工作区角色         │ 默认本地子目录                │ 引导配置选项                             │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 1. 权威记忆库      │ <Root>/MY_Memories            │ [A] 克隆已有私有 Git 仓库 (输入 Git URL)  │
│    (Memory Bank)   │                               │ [B] 基于标准骨架全新初始化 (推送到私有库)│
│                    │                               │ [C] 关联本地已有文件夹                   │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 2. 自建代码库      │ <Root>/Vibe_Coding            │ 存放用户的所有自建生产项目工作区         │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 3. 知识学习库      │ <Root>/My_Learning            │ 存放技术研究计划、知识缺口登记与学习笔记 │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 4. 外部参考库      │ <Root>/Reference_Coding       │ 存放第三方开源只读参考源码 (严格只读)    │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 5. 自研技能库      │ <Root>/Author-Skills          │ 存放用户自研与定制的 Agent Skill 源码    │
└────────────────────┴───────────────────────────────┴──────────────────────────────────────────┘
```

### 步骤 3：自适应环境变量与锚点配置
为消除绝对路径硬编码，自动在用户操作系统（或当前终端 Profile）中注入通用环境变量：
- Windows PowerShell:
  ```powershell
  [Environment]::SetEnvironmentVariable("AI_WORKSPACE_ROOT", "<Root>", "User")
  [Environment]::SetEnvironmentVariable("MY_MEMORIES_PATH", "<Root>\MY_Memories", "User")
  ```
- Mac / Linux Shell:
  ```bash
  export AI_WORKSPACE_ROOT="<Root>"
  export MY_MEMORIES_PATH="<Root>/MY_Memories"
  ```

### 步骤 4：多 Agent 准入环境自动挂载
自动探测当前操作系统已安装的 Agent 环境，并建立规则链接：
1. **Antigravity / Gemini CLI**：
   - 软链接或同步自研技能至 `$HOME/.gemini/config/skills/`；
2. **Cursor / Windsurf**：
   - 生成或注入全局 `.cursorrules` / rules 配置，指向 `MY_Memories` 中的行为准则；
3. **Claude Code / Codex**：
   - 生成全局 `CLAUDE.md` / `AGENTS.md` 引用入口。

**完成标准 (Completion Criterion)**：
- 5 大工作区物理目录存在且 Git 远程仓库可正常通信；
- 环境变量 `AI_WORKSPACE_ROOT` 与 `MY_MEMORIES_PATH` 在当前会话与系统持久层均已生效；
- 至少 1 个已安装的 Agent 成功建立规则软链接或配置注入。

---

## 模式二：status（拓扑健康巡检 SOP）

当执行 `/workspace-bootstrap status` 时：
1. 扫描 5 大工作区的物理目录是否存在；
2. 检查 `MY_Memories` 是否存在未提交的 Git 变更；
3. 验证环境变量 `$env:MY_MEMORIES_PATH` 是否与实际路径吻合；
4. 输出拓扑健康卡片：
   ```text
   ┌─────────────────────────────────────────────────────────────┐
   │ Workspace Topology Status Report                            │
   ├──────────────────────┬────────────────────────┬─────────────┤
   │ Workspace            │ Local Path             │ Status      │
   ├──────────────────────┼────────────────────────┼─────────────┤
   │ • Memory Bank        │ <Root>/MY_Memories     │ [OK] Linked │
   │ • Project Bank       │ <Root>/Vibe_Coding     │ [OK] Ready  │
   │ • Learning Bank      │ <Root>/My_Learning     │ [OK] Ready  │
   │ • Reference Bank     │ <Root>/Reference_Coding│ [OK] Clean  │
   │ • Author Skills      │ <Root>/Author-Skills   │ [OK] Synced │
   └──────────────────────┴────────────────────────┴─────────────┘
   ```

**完成标准 (Completion Criterion)**：
- 5 大工作区的路径与状态扫描完毕；
- 呈现完整的表格化状态卡片，并给出明确的异常项修复提示（若有）。

---

## 模式三：link（多 Agent 规则重挂载 SOP）

当用户安装了新的 Agent 工具，或重装了某个 IDE 时执行 `/workspace-bootstrap link`：
1. 重新扫描 `$HOME/.gemini/`、`$HOME/.cursor/`、`$HOME/.claude/` 等配置根；
2. 重新建立符号链接（Symlink）或准入规则注入；
3. 校验各 Agent 打开工作区后能否正确读取权威规范。

**完成标准 (Completion Criterion)**：
- 检测到的所有目标 Agent 配置根均已更新软链接或配置文件；
- 验证读取测试通过，向用户确认规则挂载就绪。
