# Author-Skills (自研 Agent 技能库)

个人原创与深度定制的 AI Agent 技能（Skills）母库。所有技能遵循 [`writing-for-agents`](https://github.com/SilasFu/Author-Skills) 规范构建，支持通过 `skills-manager` 一键安装并分发至 Antigravity、Codex、Claude Code 等多 Agent 运行环境。

---

## 🎯 仓库定位与架构流转

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. 本地自研母库 (D:\Vibe_Coding\Author-Skills)                │
│    • 编写、调试、规范化校验自研 Skill 源码                      │
└──────────────────────────────┬──────────────────────────────┘
                               │ git push
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. GitHub 远程仓库 (SilasFu/Author-Skills)                   │
└──────────────────────────────┬──────────────────────────────┘
                               │ skills-manager 导入安装
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. skills-manager 中枢 (~/.skills-manager)                   │
│    • 场景编排 (PM-Design, UI-Design, CD-Systems 等)         │
│    • 一键分发至各 Agent (Antigravity, Codex, Claude Code)     │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 技能清单 (Skill Inventory)

| 技能名称 | 类型 | 适用场景与触发条件 |
| :--- | :--- | :--- |
| **`workspace-lifecycle-governance`** | 治理与决策 | 多工作区生命周期路由：知识盲区感知登记、新项目立项 vs 现有项目扩展 4 步决策树、记忆库连续性同步 |
| **`my-memories`** | 查询与检索 | 权威知识库（`D:\MY_Memories`）的画像、工作偏好、协作边界与产品蓝图规范化查询接口 |

---

## 🛠️ 技能开发与贡献标准

所有存入本库的技能必须严格遵循以下质量标准：
1. **Frontmatter 严谨性**：`description` 必须前置触发引导词（Leading Words），清晰列出互斥的触发分支，杜绝冗余口水词。
2. **明确的完成条件 (Completion Criteria)**：每个 SOP 步骤必须具备“可检验完成度（Checkable Bounds）”，防止模型过早结束。
3. **正向行为引导 (Anti-Negation)**：使用正向目标描述，避免多重否定句式。
4. **编码规范**：所有文件使用 `UTF-8 without BOM`。