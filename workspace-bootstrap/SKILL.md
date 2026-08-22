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

| 模式 | 用户典型触发语 | 核心使命 |
| :--- | :--- | :--- |
| **冷启动初始化 (init)** | “在新电脑上初始化工作区”、“帮我配置这台机器上的多 Agent 工作区”、“/workspace-bootstrap init” | 交互式引导探测根目录、绑定 6 大工作区私有仓库、注入通用环境变量、配置多 Agent 规则软链接。 |
| **状态与健康检查 (status)** | “检查工作区拓扑状态”、“查看当前绑定的仓库与路径”、“/workspace-bootstrap status” | 探测当前 6 大工作区的存在性、Git Remote 状态、环境变量与挂载有效性。 |
| **多 Agent 重新挂载 (link)** | “重新挂载 Agent 规则”、“将工作区规则注入到新安装的工具”、“/workspace-bootstrap link” | 将全局规则与项目级契约无损注入到 Cursor, Antigravity, Claude Code, Codex 等工具中。 |

---

## 模式一：init（全生态冷启动与自适应建库 SOP）

当在新电脑或新环境中执行 `/workspace-bootstrap init` 时，依次执行以下 4 步交互引导：

### 步骤 1：工作区根目录定位（Root Directory Detection）
探测并向用户确认本地工作区根目录：
- Windows 优先探测多分区（如 `D:\` 或 `C:\Workspaces`）；
- Mac/Linux 默认推荐 `~/Workspaces` 或 `$HOME/Projects`；
- 用户可直接回车使用推荐路径，或输入自定义绝对路径。

### 步骤 2：六大工作区交互式绑定（Private Instance Binding）

按照标准拓扑结构，逐一引导用户绑定属于自己的资产：

```text
┌────────────────────┬───────────────────────────────┬──────────────────────────────────────────┐
│ 工作区角色         │ 默认本地子目录                │ 引导配置选项                             │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 1. 灵感总控中枢    │ <Root>/Idea_Hub               │ [A] 基于标准中枢骨架全新初始化           │
│    (Idea Hub)      │                               │ [B] 关联本地已有目录                     │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 2. 权威记忆库      │ <Root>/MY_Memories            │ [A] 克隆已有私有 Git 仓库 (输入 Git URL) │
│    (Memory Bank)   │                               │ [B] 基于标准骨架全新初始化 (推送到私有库)│
│                    │                               │ [C] 关联本地已有文件夹                   │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 3. 自建代码库      │ <Root>/Vibe_Coding            │ 存放用户的所有自建生产项目工作区         │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 4. 知识学习库      │ <Root>/My_Learning            │ 存放技术研究计划、知识缺口登记与学习笔记 │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 5. 外部参考库      │ <Root>/Reference_Coding       │ 存放第三方开源只读参考源码 (严格只读)    │
├────────────────────┼───────────────────────────────┼──────────────────────────────────────────┤
│ 6. 自研技能库      │ <Root>/Author-Skills          │ 存放用户自研与定制的 Agent Skill 源码    │
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
- 6 大工作区物理目录存在，Git 远程仓库可正常通信；
- 环境变量 `AI_WORKSPACE_ROOT` 与 `MY_MEMORIES_PATH` 在当前会话与系统持久层均已生效；
- 至少 1 个已安装的 Agent 成功建立规则软链接或配置注入。

---

## 模式二：status（拓扑健康巡检 SOP）

当执行 `/workspace-bootstrap status` 时：
1. 扫描 6 大工作区的物理目录是否存在；
2. 检查 `MY_Memories` 与 `Idea_Hub` 是否存在未提交的 Git 变更；
3. 验证环境变量 `$env:MY_MEMORIES_PATH` 是否与实际路径吻合；
4. 输出拓扑健康卡片：
   ```text
   ┌─────────────────────────────────────────────────────────────┐
   │ Workspace Topology Status Report                            │
   ├──────────────────────┬────────────────────────┬─────────────┤
   │ Workspace            │ Local Path             │ Status      │
   ├──────────────────────┼────────────────────────┼─────────────┤
   │ 💡 Idea Hub          │ <Root>/Idea_Hub        │ [OK] Active │
   │ 🧠 Memory Bank       │ <Root>/MY_Memories     │ [OK] Linked │
   │ 💻 Project Bank      │ <Root>/Vibe_Coding     │ [OK] Ready  │
   │ 📚 Learning Bank     │ <Root>/My_Learning     │ [OK] Ready  │
   │ 🔍 Reference Bank    │ <Root>/Reference_Coding│ [OK] Clean  │
   │ 🛠️ Author Skills     │ <Root>/Author-Skills   │ [OK] Synced │
   └──────────────────────┴────────────────────────┴─────────────┘
   ```

**完成标准 (Completion Criterion)**：
- 6 大工作区的路径与状态扫描完毕；
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
