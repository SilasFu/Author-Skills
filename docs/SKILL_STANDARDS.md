# Author-Skills 技能编写与准入规范 (SKILL_STANDARDS)

所有提交或修改至本仓库的 Agent Skill，必须严格遵循以下质量与安全门禁：

---

## 1. Frontmatter 与上下文指针规范 (Context Pointer)

- `name`: 必须使用小写 kebab-case，且必须与技能目录名称完全一致；
- `description`:
  - 必须前置 **Leading Words**（触发动词）；
  - 必须明确罗列该技能处理的所有**正交触发分支**（`(1)... (2)... (3)...`）；
  - 必须消除同义词堆叠与无意义废话；
  - 必须杜绝在 description 中塞入技能的主体自述（Identity）。

---

## 2. 信息层级与行数控制 (Information Hierarchy)

- **主文件行数警戒线**：`SKILL.md` 正文严格控制在 **300 行以内**（绝对上限 500 行）；
- **渐进披露原则**：复杂领域规范、大段数据模板必须抽离至 `references/` 目录，通过显式指针引导 Agent 按需读取。

---

## 3. 完成标准与防早退规范 (Completion Criteria)

- 每个模式（SOP）的末尾必须包含明确的 **`完成标准 (Completion Criterion)`**；
- 标准必须是**客观可验证的硬指标（Checkable Bounds）**，例如：
  - “文件已落盘且语法编译通过”；
  - “Git 提交成功且包含规范的 commit message”；
  - “向用户输出了结构化健康卡片”。
- 严禁使用模糊的“理解已达成”、“基本处理完毕”等容易诱发 premature completion 的软性描述。

---

## 4. 正向引导与语言规范 (Positive Prompting)

- 优先使用**目标行为的正面肯定描述**（Positive Target），减少单纯使用“禁止做 X”导致的否定反向激活；
- 编码格式：所有 Markdown 与脚本文件统一使用 **UTF-8 without BOM**，行尾采用 LF 或 CRLF 自适应。

---

## 5. 零隐私与中立性审查 (Portability Gate)

- 严禁在技能中硬编码任何真实的个人姓名、私人路径、私人 Token、或特定私有 GitHub 地址；
- 所有环境交互必须通过环境变量、当前工作区自感知相对路径、或交互式选项动态获取。
