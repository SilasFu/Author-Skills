# 渐进披露查询协议与脱敏手册 (Query Protocols & Redaction)

本手册规范 AI Agent 在访问 `MY_Memories` 时的行为准则，确保上下文高效、低延迟与零隐私泄漏。

---

## 1. 渐进披露查询铁律 (Progressive Disclosure)

1. **严禁全量扫描**：禁止使用通用工具遍历读取整个 `MY_Memories/` 目录；
2. **切片精准提取**：优先使用 `search_memories.py` 脚本按需提取目标切片：
   - 提取个人画像与偏好 ➔ `python scripts/search_memories.py --category profile`
   - 提取工具与协作边界 ➔ `python scripts/search_memories.py --category collaboration`
   - 提取项目上下文 ➔ `python scripts/search_memories.py --category projects`
   - 关键字搜索 ➔ `python scripts/search_memories.py --query "<关键词>"`

---

## 2. 敏感信息脱敏标记规范 (Redaction Standard)

所有写入或提取的记忆文本，若涉及个人隐私或凭据，必须使用双重标记进行脱敏掩码：

- **姓名/个人标识**：`[敏感]张三[敏感]`
- **本地私人路径**：`[敏感]C:\Users\Secret\[敏感]`
- **API Token/密钥**：`[敏感]sk-xxxxxx[敏感]`
- **私人私有仓库地址**：`[敏感]git@github.com:private/repo[敏感]`
