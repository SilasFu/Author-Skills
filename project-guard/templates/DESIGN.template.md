# {{PROJECT_NAME}} 视觉与交互设计契约 (DESIGN.md)

## 1. 设计哲学与核心原则

本项目遵循现代工业级软件的极致设计标准，保证跨设备、跨屏幕、多模态下的一致性与高质感：

1. **灰阶中性基调 (Neutral & Monochromatic)**：
   - 整体以高质感的中性黑白灰为骨架，避免杂乱的花哨配色；
   - 品牌色与状态色仅作为高亮引导点缀（Accent Color）。
2. **去卡片化与呼吸感 (Anti-Card & Rhythm)**：
   - 减少厚重嵌套卡片与强描边；
   - 依赖 **8px 网格系统**（8px, 16px, 24px, 32px, 48px）的留白与轻微层次阴影建立视觉呼吸感。
3. **确定性语义 Token (Deterministic Semantic Tokens)**：
   - 严禁手写任意十六进制色值或原始 RGB；所有色彩必须映射到语义化变量。

---

## 2. 核心色彩体系与语义 Token

| 语义角色 | CSS / Tailwind Token | 亮色模式 (Light) | 暗色模式 (Dark) | 用途说明 |
| :--- | :--- | :--- | :--- | :--- |
| **主背景** | `bg-background` | `#FFFFFF` | `#09090B` | 页面最底层主容器背景 |
| **次级背景** | `bg-muted` / `bg-secondary` | `#F4F4F5` | `#27272A` | 侧边栏、搜索框、输入框背景 |
| **主前景色** | `text-foreground` | `#09090B` | `#FAFAFA` | 标题、主要正文内容 |
| **次级前景色** | `text-muted-foreground` | `#71717A` | `#A1A1AA` | 辅助说明、占位符、副标题 |
| **边框分隔** | `border-border` | `#E4E4E7` | `#27272A` | 分隔线、输入框弱边框 |
| **强调主色** | `bg-primary` / `text-primary` | `#18181B` | `#FAFAFA` | 核心操作按钮、选中高亮 |
| **危险与错误** | `text-destructive` | `#EF4444` | `#DC2626` | 报错提示、删除操作 |
| **成功态** | `text-emerald-500` | `#10B981` | `#059669` | 成功提示、在线状态 |

---

## 3. UI 交互 8 大全状态矩阵 (The 8-State UI Matrix)

在实现任何组件或页面时，**必须全面覆盖以下 8 大状态**，严禁仅实现理想态：

| 状态类型 | 触发条件 | 视觉与交互表现 | 验收标准 |
| :--- | :--- | :--- | :--- |
| **1. 理想态 (Ideal)** | 数据正常加载且有充实内容 | 标准布局、语义排版、高质感对齐 | 核心内容流畅呈现，无溢出与布局抖动 |
| **2. 空状态 (Empty)** | 查询结果为空或初次进入无数据 | 居中弱化图标 + 友好文案 + 引导创建 CTA | 禁止空白一片，必须提供前进行动路径 |
| **3. 加载中 (Loading)** | 异步数据请求中 | 骨架屏 (Skeleton) 优先于菊花转圈 (Spinner) | 骨架尺寸与真实内容 1:1，防止闪烁 |
| **4. 局部加载 (Partial)** | 大数据集分页或分块加载中 | 主体呈现 + 局部轻量 Progress 指示 | 不阻塞用户对已加载部分的交互 |
| **5. 错误态 (Error)** | 接口失败或网络异常 | 红色弱警示背景 + 错误原因 + 重试按钮 (Retry) | 给出可理解的原因，支持一键重试 |
| **6. 离线态 (Offline)** | 网络断开连接 | 顶部弱条提示 (Banner) + 禁用网络操作 | 本地数据只读可用，网络恢复自动重连 |
| **7. 鉴权态 (Unauthorized)** | 未登录或权限不足 | 锁图标 + 权限升级或登录跳转引导 | 保护敏感视图，清晰告知获取权限途径 |
| **8. 激活/悬停态 (Interactive)** | 用户 Hover, Focus, Active, Disabled | 300ms 以内微动效、透明度变化、聚焦环 (Ring) | 状态反馈即时，Disabled 态禁用点击 |

---

## 4. 字体与排版层级 (Typography)

- **字体族**：`Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **代码字体**：`JetBrains Mono, Fira Code, Menlo, monospace`
- **层级规范**：
  - `H1 (Page Title)`：28px / Bold / `tracking-tight`
  - `H2 (Section Header)`：20px / SemiBold
  - `H3 (Sub Section)`：16px / Medium
  - `Body (正文)`：14px / Regular / `leading-relaxed`
  - `Caption (辅助说明)`：12px / Regular / `text-muted-foreground`

---

## 5. 设计规范禁忌 (Do's and Don'ts)

### ❌ 严禁事项 (Don'ts)
- 严禁手写 `#ffffff`、`#333333`、`rgb(12, 34, 56)` 等硬编码颜色；
- 严禁出现无反馈的死按钮（点击后没有任何 Loading 或禁用状态）；
- 严禁直接抛出原生 Exception 堆栈给终端用户。

### ✅ 推荐实践 (Do's)
- 组件边角统一使用标准圆角（如 `rounded-lg` 8px / `rounded-md` 6px）；
- 所有过渡动画采用 `transition-all duration-200 ease-in-out`；
- 所有交互元素必须具备键盘 Tab 可访问性（`focus-visible:ring-2`）。
