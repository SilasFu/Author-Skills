# 任务规格书: {{TASK_NAME}} (Task Specification)

> 来源: 灵感总控中枢派发 (Idea Hub Dispatch)
> 派发日期: {{DATE}}
> 目标工作区: `{{TARGET_PROJECT}}`

---

## 1. 需求范围与边界 (Scope)

### ✅ 必须包含 (In-Scope)
{{IN_SCOPE_ITEMS}}

### ❌ 明确排除 (Out-of-Scope)
{{OUT_OF_SCOPE_ITEMS}}

---

## 2. 客观可验证验收标准 (Acceptance Criteria)

{{ACCEPTANCE_CRITERIA}}

---

## 3. 一键启动提词 (Downstream Prompt)
```text
@docs/tasks/{{TASK_FILE_NAME}} 请按照该任务规格书与本项目 AGENTS.md 契约开始执行。
```
