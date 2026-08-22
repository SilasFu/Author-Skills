# My_Learning 知识学习库治理规约 (AGENTS.md)

## 1. 工作区定位与职责边界

本目录为个人技术演进的 **知识学习与技术盲区库 (Learning Bank)**。
- **核心职能**：系统沉淀技术盲区、底层协议/算法研究、技术选型调研与最小 PoC 验证；
- **目录结构**：
  - `knowledge_gaps/`：通过 `/workspace-lifecycle-governance gap` 自动感知的知识缺口追踪卡片；
  - `deep_study/`：深度技术研究报告、实战读书笔记与架构剖析；
  - `labs/`：最小可行性技术验证与学习型实验代码。

---

## 2. 核心行为准则与红线 (Do's and Don'ts)

### 2.1 严厉禁止 (Don'ts)
- ❌ **严禁在此编写生产业务代码**：任何正式生产级自研项目必须进入 `Vibe_Coding/`；
- ❌ **严禁随意克隆大型外部仓库**：纯只读学习的外部开源库统一存放在 `Reference_Coding/`；
- ❌ **严禁散乱存放未经分类的零碎文件**。

### 2.2 推荐实践 (Do's)
- ✅ 发现知识盲区时，优先使用 `/workspace-lifecycle-governance gap` 标准化建档；
- ✅ 学习成果以“最小 PoC 跑通”和“高信噪比总结卡片”为闭环交付物。
