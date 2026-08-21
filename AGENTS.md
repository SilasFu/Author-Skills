# Author-Skills 协作规则 (AGENTS.md)

## 1. 仓库职责

本仓库是个人原创与深度定制 Agent Skill 的**唯一自研源头仓库**。
- 本地路径：`D:\Vibe_Coding\Author-Skills`
- 职责：只存放经工程化检验的自研 Skill 源码与规范文档。
- 严禁存放第三方未经改造的外部 Skill 副本（外部备份归档统一存放在 `My-Skills`）。

---

## 2. 技能编写与演进标准

新增或修改 Skill 时，必须遵循 [`writing-for-agents`](skills/writing-for-agents) 规范：
1. **单一事实源 (Single Source of Truth)**：每个通用概念只在单一权威位置定义。
2. **渐进式加载 (Progressive Disclosure)**：`description` 保持精简敏锐（控制 Context Load），详细的执行流程与模板封装在 `SKILL.md` 正文中。
3. **完成条件闭环**：每个执行流程必须包含客观可核验的 `Completion Criterion`。
4. **测试与校验**：修改 Skill 后，需核对 YAML Frontmatter 格式以及相关路径可达性。

---

## 3. 发布与同步流程

1. 本地完成 Skill 编写或优化；
2. 运行 Git 提交；
3. 推送到远程 GitHub 仓库；
4. 打开 `skills-manager` 进行版本刷新与多 Agent 场景分发；
5. 在个人网站（[https://www.aooby.cn/](https://www.aooby.cn/)）同步更新对应 Skill 的深度图文介绍与案例。

---

## 4. 开源协议与边界

- 本项目采用 **CC BY-NC-SA 4.0** 协议开源。
- 允许个人学习、日常使用与非营利性研究；
- 严禁任何未经授权的商业化售卖、付费课程打包或商业闭源集成。