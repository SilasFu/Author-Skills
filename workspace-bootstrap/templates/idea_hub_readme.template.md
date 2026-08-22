# Idea Hub (灵感总控中枢)

灵感总控中枢是所有碎片化想法、需求提议、系统重构设想的**第一沉淀点与统一调度中心**。

---

## 1. 目录结构与生命周期流转

```text
Idea_Hub/
├── README.md               # 灵感中枢总览与看板状态
├── inbox/                  # 待评估需求箱 (收纳初生想法与用户原始诉求)
├── active/                 # 推进中需求 (已通过可行性评估，正在规划或分派)
└── archived/               # 已归档/已交付需求 (已成功派发至 Vibe_Coding / My_Learning / Author-Skills)
```

---

## 2. 灵感生命周期流转阶梯

1. **灵感捕获 (Inbox)**：所有灵感以 `REQ-YYYYMMDD-名称.md` 存入 `inbox/`；
2. **四级复用评估 (Triage)**：
   - **Level 1**：存量项目微调 ➔ 直接指派至对应 `Vibe_Coding/<项目>`；
   - **Level 2**：知识盲区学习 ➔ 流转至 `My_Learning/knowledge_gaps/`；
   - **Level 3**：母体机制与技能 ➔ 流转至 `Author-Skills/`；
   - **Level 4**：独立新业务立项 ➔ 移至 `active/` 规划后在 `Vibe_Coding/` 新建工程；
3. **完成归档 (Archived)**：派发成功并闭环后，移入 `archived/`。

---

## 3. 当前活跃灵感看板 (Active Board)

| 灵感编号 | 标题 / 需求描述 | 目标流转工作区 | 当前状态 | 负责人 / Agent |
| :--- | :--- | :--- | :--- | :--- |
| *REQ-001* | *(示例需求占位)* | `Vibe_Coding` | 评估中 | Antigravity |
