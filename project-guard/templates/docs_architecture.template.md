# {{PROJECT_NAME}} 技术架构与模块设计文档 (ARCHITECTURE)

## 1. 系统总体分层架构 (System Architecture)

本项目采用清晰的三层职责切片架构：

```mermaid
flowchart TD
    subgraph UI ["1. 表现层 (Presentation Layer)"]
        A["组件视图 (Components / Views)"]
        B["页面路由 (Pages / Routes)"]
    end

    subgraph Business ["2. 业务与状态层 (Domain & Logic Layer)"]
        C["自定义 Hooks / 组合式函数"]
        D["状态存储 (State Store)"]
        E["业务核心服务 (Services)"]
    end

    subgraph Infrastructure ["3. 基础设施与数据契约 (Infrastructure & Contracts)"]
        F["API 客户端 / 本地存储"]
        G["类型契约 (types.ts)"]
        H["环境配置 / 工具函数 (utils)"]
    end

    UI --> Business
    Business --> Infrastructure
```

---

## 2. 核心模块职责与边界清单

| 模块目录 | 核心职责 | 依赖项 | 禁忌行为 (Don'ts) |
| :--- | :--- | :--- | :--- |
| `src/components/` | 纯 UI 渲染与视图交互 | `types.ts`, `DESIGN.md` | 严禁编写复杂异步请求与副作用逻辑（业务单文件 ≤ 200 行） |
| `src/hooks/` / `src/services/` | 业务逻辑、状态衍生与 API 调度 | `types.ts`, `api` | 严禁包含 JSX/HTML 渲染代码 |
| `src/types/` | 数据结构与 TypeScript 类型契约 | 无（底层事实源） | 严禁使用 `any` 类型逃逸 |

---

## 3. 关键数据流向 (Data Flow)

```mermaid
sequenceDiagram
    autonumber
    actor User as 用户/交互端
    participant View as 视图组件 (Component)
    participant Hook as 业务钩子 (useLogic)
    participant Service as 核心服务 (Service)
    participant Storage as 数据源/API

    User->>View: 触发操作
    View->>Hook: 调用业务方法
    Hook->>Service: 发起业务请求
    Service->>Storage: 数据持久化 / 请求
    Storage-->>Service: 返回响应数据
    Service-->>Hook: 派发状态更新
    Hook-->>View: 触发 UI 响应式重新渲染
```

---

## 4. 关键技术选型与运行时依赖

- **语言与运行时**：{{TECH_STACK}}
- **构建与测试工具**：{{BUILD_TOOL}}
- **设计契约**：遵循项目根目录 [`DESIGN.md`](../DESIGN.md)
- **代码质量与门禁**：遵循项目根目录 [`AGENTS.md`](../AGENTS.md)
