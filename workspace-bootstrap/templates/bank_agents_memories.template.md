# MY_Memories 权威记忆库治理规约 (AGENTS.md)

## 1. 工作区定位与职责边界

本目录为个人 AI 协同的 **唯一权威记忆库 (Memory Bank SSOT)**。
- **物理路径**：默认指向系统环境变量 `$MY_MEMORIES_PATH`；
- **核心职能**：沉淀个人画像、工作与决策偏好、AI 协作红线与各项目权威架构设计契约；
- **纯文件事实源**：所有记忆采用纯 Markdown 文件持久化并接受 Git 版本控制，严禁依赖黑盒私有暗状态。

---

## 2. 核心行为准则与红线 (Do's and Don'ts)

### 2.1 严厉禁止 (Don'ts)
- ❌ **严禁随意静默写入**：除了通过 `/project-guard evolve` 或 `/workspace-lifecycle-governance sync` 提炼的权威规则，严禁将临时会话琐事或未经提炼的垃圾信息写入记忆库；
- ❌ **严禁存储二进制与业务代码**：本仓库严禁存放大体积二进制文件、构建缓存或具体业务项目实现源码；
- ❌ **严禁破坏目录规范**：严格维护 `knowledge/profile/`、`knowledge/boundary/`、`knowledge/projects/` 三大分类。

### 2.2 推荐实践 (Do's)
- ✅ 优先通过 `my-memories` 技能提供的标准化接口进行只读查询；
- ✅ 保持记忆切片高信噪比，原子化组织 Markdown 文档；
- ✅ 每次关键偏好与规则更新后完成结构化 Git Commit。
