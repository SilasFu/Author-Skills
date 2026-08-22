# {{PROJECT_NAME}} - Claude Code Guidelines (CLAUDE.md)

This project strictly follows the Single Source of Truth (SSOT) defined in [`AGENTS.md`](./AGENTS.md).

## Quick Architecture & Quality Summary
- **SSOT Rules**: Refer to [`AGENTS.md`](./AGENTS.md) for all architectural boundaries and quality gates.
- **Line-Count Gate**: Strict business/UI single-file limit of **≤ 200 lines**. If exceeding 200 lines, refactor into `Component.tsx`, `useComponent.ts`, and `types.ts`.
- **Design Contract**: Refer to [`DESIGN.md`](./DESIGN.md) for design tokens and states. No hardcoded hex colors or untracked inline styles.
- **Verification Gate**: Must run `{{CHECK_COMMAND}}` with **0 Errors / 0 Warnings** before task completion.
