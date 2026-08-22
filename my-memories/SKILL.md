---
name: my-memories
description: >-
  Query and inspect user profile, preferences, collaboration boundaries, project context, and architecture specs in MY_Memories.
  Trigger when: (1) retrieving user personal profile or work preferences, (2) checking AI collaboration and CLI boundary rules,
  (3) reading local workspace context or product architecture specifications.
argument-hint: "profile | collaboration | projects | search | audit"
---

# Authoritative Memory Bank (`MY_Memories`)

Query interface, slicing extractor, and security auditor for the user's authoritative personal knowledge base (Source of Truth).

---

## 核心模式与触发指令

| 模式 | 用户典型触发词 | 核心使命与底层工具支撑 |
| :--- | :--- | :--- |
| **profile (画像与偏好)** | “查询我的工作偏好”、“查看我的个人画像”、“/my-memories profile” | 运行 `scripts/search_memories.py --category profile` 毫秒级提取个人画像与决策偏好。 |
| **collaboration (协作边界)** | “查看 AI 工具边界规范”、“检查 CLI 协作权限”、“/my-memories collaboration” | 运行 `scripts/search_memories.py --category collaboration` 提取工具分工与命令红线。 |
| **projects (项目上下文)** | “查看当前工作区项目状态”、“读取项目架构蓝图”、“/my-memories projects” | 运行 `scripts/search_memories.py --category projects` 提取各项目当前阶段与拓扑。 |
| **search (关键词全局检索)** | “在记忆库中搜索 X”、“查一下关于 Y 的规范”、“/my-memories search <query>” | 运行 `scripts/search_memories.py --query "<关键词>"` 精准提取匹配词条。 |
| **audit (安全与完整性审计)** | “审计记忆库安全”、“检查是否有未脱敏密钥”、“/my-memories audit” | 运行 `scripts/verify_integrity.py` 全面排查敏感凭据泄漏与结构完整性。 |

---

## 模式一：检索与切片发现 SOP (Query & Slice)

当需要查阅用户画像、协作红线或项目事实时：

### 1. 执行确定性检索脚本
```bash
python <path-to-skill>/scripts/search_memories.py --category <profile|collaboration|projects|practices>
```
或者指定关键字：
```bash
python <path-to-skill>/scripts/search_memories.py --query "<关键词>"
```
脚本将自动解析 `$env:MY_MEMORIES_PATH` 或相对拓扑，毫秒级提取纯净 Markdown 片段，**严禁全库扫描读入无关噪音**。

### 2. 遵循置信度阶梯裁决
若遇到记忆库与用户即时对话冲突，参考 [`references/confidence_ladder.md`](references/confidence_ladder.md)：
> **用户当前即时指令 (Level 1)** > **项目 docs 契约 (Level 2)** > **记忆库事实 (Level 3)**

**完成标准 (Completion Criterion)**：输出精准记忆切片，禁止全量读取无关文件。

---

## 模式二：安全审计与防泄漏 SOP (Integrity & Redaction)

当需要排查记忆库合规性与防泄漏状态时：

### 1. 执行审计脚本
```bash
python <path-to-skill>/scripts/verify_integrity.py
```
脚本将自动检测：
1. 核心分类目录（`profile`, `projects`, `boundary`）是否完整；
2. 扫描所有 Markdown 文件是否存在未脱敏的 API Token、私钥或明文凭据；
3. 输出标准化安全与完整性健康卡片。

**完成标准 (Completion Criterion)**：运行 `verify_integrity.py` 退出码为 0，向用户呈现完整性与脱敏健康卡片。