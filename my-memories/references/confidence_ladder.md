# 真实源置信度阶梯与决策优先级手册 (Confidence Ladder)

多 Agent 协同作业时，当遇到信息冲突或不一致时，**必须严格按照以下五级置信度阶梯自顶向下裁决，高优先级绝对覆盖低优先级**：

---

## 1. 五级置信度阶梯

```text
[Level 1] 用户当前即时指令 (User Immediate Prompt) ────────► 最高权威 (覆盖一切历史事实)
   │
[Level 2] 当前项目 docs/ 架构契约 (Project Contract) ───────► 项目级最高 (AGENTS.md / DESIGN.md / PRD.md)
   │
[Level 3] 权威记忆库稳定事实 (MY_Memories SSOT) ───────────► 跨项目通用事实与个人长期偏好
   │
[Level 4] 治理规则与历史决策 (Governance & Decisions) ──────► 历史决策记录与架构演进日志
   │
[Level 5] 存量代码与测试用例 (Active Repo Code) ───────────► 代码实现现状 (易腐烂，最低置信度)
```

---

## 2. 裁决冲突典型案例

1. **场景 1：代码里写着某种旧写法，但项目 `AGENTS.md` 写了新规范**：
   - 裁决：`Level 2 (项目契约)` > `Level 5 (存量代码)`，以 `AGENTS.md` 为准，并重构存量代码。
2. **场景 2：用户在对话中明确说“今天这个项目改用 Tailwind”**：
   - 裁决：`Level 1 (用户即时指令)` 覆盖现有 `DESIGN.md`，执行修改并同步更新 `DESIGN.md`。
3. **场景 3：Agent 试图猜测用户个人习惯**：
   - 裁决：禁止随意脑补，必须查阅 `Level 3 (MY_Memories/knowledge/profile/)`。
