# Vibe_Coding 自研项目库治理规约 (AGENTS.md)

## 1. 工作区定位与职责边界

本目录为个人开发生态的 **自研生产项目库 (Project Bank)**。
- **核心职能**：存放个人自研、独立立项的所有业务系统、CLI 工具与生产级应用；
- **架构隔离**：本目录下每一个子文件夹均为一个独立的 Git 仓库，各自独立演进。

---

## 2. 核心行为准则与红线 (Do's and Don'ts)

### 2.1 严厉禁止 (Don'ts)
- ❌ **严禁混入纯只读外部开源库**：未修改的开源参考项目必须存放于 `Reference_Coding/`；
- ❌ **严禁未受控立项**：所有新项目必须通过 `workspace-lifecycle-governance reuse` 复用阶梯判定，杜绝无意义的项目碎片化；
- ❌ **严禁缺乏质量门禁**：项目根目录必须具备独立的 `AGENTS.md`、`DESIGN.md` 与质量门禁。

### 2.2 推荐实践 (Do's)
- ✅ 每个新项目立项后，第一时间执行 `/project-guard init`，植入：
  1. 单文件行数限制（≤ 200 行）；
  2. 单一设计规范源（`DESIGN.md`）与语义 Token；
  3. 编译器 0 报错（Zero-Error Gate）硬门禁；
  4. 多 Agent 规则桥接（`CLAUDE.md`）。
- ✅ 定期执行 `/project-guard doctor` 消除巨石文件与设计漂移。
