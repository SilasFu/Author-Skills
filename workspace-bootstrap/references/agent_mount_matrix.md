# 多 Agent 规则挂载点与配置文件映射矩阵 (Agent Mount Matrix)

本地生态支持多款主流 AI Agent 工具协同作业。本手册定义各 Agent 工具的全局与项目级规则生效机制。

---

## 1. 主流 Agent 配置路径与挂载策略

| Agent 工具 | 用户全局配置路径 | 技能/规则加载机制 | 推荐挂载方式 |
| :--- | :--- | :--- | :--- |
| **Google Antigravity / Gemini CLI** | `~/.gemini/config/skills/` 或 `~/.gemini/antigravity-ide/builtin/skills/` | 读取 `skills/<skill_name>/SKILL.md` 与 `rules/` | 符号链接 (Symlink) 挂载 `Author-Skills/<skill>` 目录 |
| **Cursor IDE** | `~/.cursor/` 或项目根目录 `.cursorrules` / `.cursor/rules/` | 自动索引项目根目录 `AGENTS.md`、`.cursorrules` 与 `DESIGN.md` | 在项目 `AGENTS.md` 中引用，或配置全局 Rules |
| **Claude Code CLI** | `~/.claude/` 或 `~/.config/claude-code/` | 读取全局与项目级 `CLAUDE.md` 与 Skills 目录 | 在项目根目录保留 `CLAUDE.md` 指向 `AGENTS.md` |
| **Windsurf (Codeium)** | `~/.windsurf/` 或项目根目录 `.windsurfrules` | 索引工作区规则与 `AGENTS.md` | 项目根目录生成 `.windsurfrules` 软链接 |
| **OpenCode / Codex** | `~/.config/opencode/` | 原生支持读取项目根目录 `AGENTS.md` 契约 | 纯文件 SSOT 直接读取 |

---

## 2. 规则同步与权限安全红线

1. **分发权限隔离**：Agent 严禁在未经用户明确确认的情况下，越权静默篡改 `$HOME` 下的全局系统级配置文件；
2. **单一事实源 (SSOT)**：所有项目级 Agent 统一优先读取工作区根目录的 `AGENTS.md` 与 `DESIGN.md`，实现一套规范、全 Agent 适用。
