# UI 交互 8 大状态设计与验收细则 (The 8-State UI Matrix Guide)

在构建任何前端界面、页面或复合组件时，必须确保覆盖以下完整的 8 大交互状态，杜绝由于状态遗漏导致的界面崩坏或空白。

---

## 1. 状态矩阵对照与代码实现范例

### 状态 1：理想态 (Ideal State)
- **描述**：数据完整无误加载后的主视图。
- **要点**：排版清晰、层次分明、网格对齐、文字具备合理换行截断。
- **范例**：
  ```tsx
  {status === 'success' && data.length > 0 && (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {data.map(item => <CardItem key={item.id} item={item} />)}
    </div>
  )}
  ```

### 状态 2：空状态 (Empty State)
- **描述**：没有任何数据（初次使用、搜索无结果、列表为空）。
- **要点**：**严禁白屏或仅显示空表格**。必须包含：中性弱化插画/图标、提示文案、引导创建或重置筛选的 CTA 按钮。
- **范例**：
  ```tsx
  {status === 'success' && data.length === 0 && (
    <div className="flex flex-col items-center justify-center p-12 text-center border border-dashed rounded-lg">
      <InboxIcon className="w-12 h-12 text-muted-foreground mb-3" />
      <h3 className="text-base font-medium text-foreground">暂无相关数据</h3>
      <p className="text-sm text-muted-foreground mt-1 mb-4">没有找到匹配的记录，请尝试重新搜索或创建新项目。</p>
      <Button onClick={onCreate}>立即创建</Button>
    </div>
  )}
  ```

### 状态 3：加载中 (Loading State)
- **描述**：初始数据加载或全局刷新中。
- **要点**：优先采用与实际内容轮廓 1:1 的**骨架屏 (Skeleton)**，避免单纯使用转圈动画导致视觉跳跃。
- **范例**：
  ```tsx
  {status === 'loading' && (
    <div className="space-y-3 animate-pulse">
      <div className="h-8 bg-muted rounded-md w-1/3" />
      <div className="h-32 bg-muted rounded-lg w-full" />
    </div>
  )}
  ```

### 状态 4：局部加载态 (Partial Loading State)
- **描述**：分页加载更多、表格某一行正在执行操作、后台静默同步。
- **要点**：局部禁用操作并展示内联 Spinner，保持其他已加载部分完全可交互。

### 状态 5：错误态 (Error State)
- **描述**：网络超时、500 服务器错误或业务拒绝。
- **要点**：友好、清晰的错误说明（隐藏复杂堆栈），并提供可恢复的 **【重试 (Retry)】** 按钮。
- **范例**：
  ```tsx
  {status === 'error' && (
    <div className="p-4 rounded-lg bg-destructive/10 border border-destructive/20 text-destructive flex items-center justify-between">
      <div>
        <p className="font-medium">数据加载失败</p>
        <p className="text-sm opacity-80">{errorMessage || '网络连接异常，请检查网络后重试。'}</p>
      </div>
      <Button variant="outline" size="sm" onClick={refetch}>重试</Button>
    </div>
  )}
  ```

### 状态 6：离线态 (Offline State)
- **描述**：用户设备网络断开。
- **要点**：顶部悬浮 Toast/Banner 提示“当前处于离线模式”，允许查看本地缓存，保存操作进入本地重试队列。

### 状态 7：鉴权/权限拦截态 (Unauthorized State)
- **描述**：用户未登录、Token 过期或没有该模块查看权限。
- **要点**：居中锁图标 + “无权访问”说明 + “申请权限/重新登录”操作。

### 状态 8：交互反馈态 (Interactive State - Hover/Focus/Active/Disabled)
- **描述**：鼠标悬停、键盘获得焦点、按压与禁用。
- **要点**：
  - Hover: 轻微透明度或背景色提亮（`hover:bg-muted/80`）；
  - Focus: 清晰的聚焦环（`focus-visible:ring-2 focus-visible:ring-primary`）；
  - Disabled: `opacity-50 cursor-not-allowed pointer-events-none`。
