# MY_Memories (个人权威记忆与知识库)

本仓库是个人唯一跨设备、跨 Agent 的**高置信度权威记忆库 (Source of Truth)**。

---

## 1. 核心目录架构

```text
MY_Memories/
├── README.md               # 记忆库总览
└── knowledge/              # 结构化知识矩阵
    ├── profile/            # 个人画像与长期通用偏好
    │   ├── 个人画像.md
    │   └── 工作与决策偏好.md
    ├── boundary/           # AI 协作红线与工具权限边界
    │   └── 协作边界规范.md
    └── projects/           # 各项目上下文与架构设计规范
        └── 本地工作区与项目上下文.md
```

---

## 2. 访问与维护铁律

1. **只读与权威性**：业务 Agent 在常规会话中对本库仅有**只读查询权**；
2. **受控回写通道**：仅允许通过 `workspace-lifecycle-governance` 或 `project-guard evolve` 执行规则提炼与回写；
3. **版本化固化**：所有重要规则修改必须伴随规范的 Git Commit，实现全生态跨设备免疫。
