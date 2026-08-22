# Site Category & Theme Matrix (aooby.cn 专栏视觉主题矩阵)

This matrix defines the 7 core content categories for `aooby.cn` and multi-platform visual publishing (WeChat, Social Cards, Posters, Infographics).

> [!IMPORTANT]
> **Aesthetic Standard (SSOT)**: All categories must follow the **Editorial Light Tech (极简亮色 · 陶瓷白)** design foundation:
> - **Canvas**: Porcelain Ice White `#F6F8FC` with soft contextual radial gradient meshes.
> - **Cards**: Crisp Pure White `#FFFFFF` with ultra-fine border `rgba(226, 232, 240, 0.9)` and ambient soft shadows (`0 16px 36px -8px rgba(15, 23, 42, 0.06)`).
> - **Typography**: Obsidian Charcoal `#090D16` (Primary Title 104px / 900 weight), Slate Charcoal `#334155` (Lead 28px / 400 weight / line-height 1.72), Slate `#64748b` (Meta).
> - **Vertical Rhythm**: Title-to-lead vertical gap `>= 36px`, section gap `>= 32px`, zero empty floating voids.
> - **3D Integration**: Seamless optical blend disk + radial gradient mask feathering.

---

## 1. Category Taxonomy & Light Tech Design Tokens

### 1.1 `agent-governance` (AI Agent 元治理 · 旗舰标准)
- **Positioning**: Meta-governance, rule self-evolution, multi-agent coordination, Author-Skills ecosystem.
- **Tone**: Authoritative, robust, architectural, self-healing.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-klein-blue";
    --bg-page: #f6f8fc;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(0, 82, 255, 0.09), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(224, 236, 255, 0.75), transparent 60%),
               linear-gradient(180deg, #fafcff 0%, #edf2f8 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #0052ff;
    --accent-soft: rgba(0, 82, 255, 0.08);
    --accent-border: rgba(0, 82, 255, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.2 `vibe-coding` (Vibe Coding 实验室)
- **Positioning**: Fast prototyping, AI-assisted fullstack engineering, automation scripts, experimental tools.
- **Tone**: High velocity, futuristic, experimental, developer-first.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-amethyst";
    --bg-page: #f8f6fc;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(124, 58, 237, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(243, 232, 255, 0.75), transparent 60%),
               linear-gradient(180deg, #fcfaff 0%, #f1edf8 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #7c3aed;
    --accent-soft: rgba(124, 58, 237, 0.08);
    --accent-border: rgba(124, 58, 237, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.3 `showcase-milestones` (作品发布与成果展示)
- **Positioning**: Major project launches, benchmark metric milestones, product showcases.
- **Tone**: Premium, high impact, luxurious tech, Apple Keynote style.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-amber-gold";
    --bg-page: #faf8f5;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(217, 119, 6, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(254, 243, 199, 0.7), transparent 60%),
               linear-gradient(180deg, #fffdfa 0%, #f4ede4 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #d97706;
    --accent-soft: rgba(217, 119, 6, 0.08);
    --accent-border: rgba(217, 119, 6, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.4 `product-management` (产品经理与商业思考)
- **Positioning**: PRD architecture, decision trade-offs, business flywheels.
- **Tone**: Analytical, structured, strategic clarity.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-slate-sapphire";
    --bg-page: #f6f8fa;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(37, 99, 235, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(219, 234, 254, 0.75), transparent 60%),
               linear-gradient(180deg, #fafcff 0%, #ecf1f7 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #2563eb;
    --accent-soft: rgba(37, 99, 235, 0.08);
    --accent-border: rgba(37, 99, 235, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.5 `design-system` (设计系统与美学实验)
- **Positioning**: Design tokens, UI/UX aesthetics, typography rules, component engineering.
- **Tone**: Pixel-perfect, avant-garde, refined.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-iris";
    --bg-page: #f7f6fc;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(99, 102, 241, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(224, 231, 255, 0.75), transparent 60%),
               linear-gradient(180deg, #faf9ff 0%, #edeaf7 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #4f46e5;
    --accent-soft: rgba(79, 70, 229, 0.08);
    --accent-border: rgba(79, 70, 229, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.6 `curriculum-teaching` (教材授课与实战训练)
- **Positioning**: Systematic bootcamps, 0-to-1 learning roadmaps, cheat sheets.
- **Tone**: Pedagogical, crystal clear, motivating.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-emerald";
    --bg-page: #f6faf7;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(5, 150, 105, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(209, 250, 229, 0.75), transparent 60%),
               linear-gradient(180deg, #f9fdfa 0%, #eaf4ed 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #059669;
    --accent-soft: rgba(5, 150, 105, 0.08);
    --accent-border: rgba(5, 150, 105, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

### 1.7 `beginner-guide` (极速入门与避坑指南)
- **Positioning**: Zero-to-one friendly guides, copy-paste prompts, FAQ fast track.
- **Tone**: Approachable, crystal clear, actionable.
- **CSS Design Tokens**:
  ```css
  :root {
    --theme-name: "editorial-warm-amber";
    --bg-page: #faf8f5;
    --bg-mesh: radial-gradient(ellipse 900px 700px at 85% 35%, rgba(234, 88, 12, 0.08), transparent 70%),
               radial-gradient(ellipse 700px 500px at 15% 75%, rgba(255, 237, 213, 0.75), transparent 60%),
               linear-gradient(180deg, #fffefa 0%, #f6eee4 100%);
    --ink-primary: #090d16;
    --ink-secondary: #334155;
    --ink-tertiary: #64748b;
    --accent: #ea580c;
    --accent-soft: rgba(234, 88, 12, 0.08);
    --accent-border: rgba(234, 88, 12, 0.2);
    --card-bg: #ffffff;
    --card-border: rgba(226, 232, 240, 0.9);
  }
  ```

---

## 2. Dynamic Slot Mapping Table

| Slot ID | Role | Required? | Behavior |
| :--- | :--- | :--- | :--- |
| `category-badge` | Category tag capsule | Yes | Solid black `#090D16` badge with cyan glow dot |
| `primary-title` | Core Headline | Yes | Formatted with `--ink-primary` and accented line |
| `hero-illustration` | 3D visual or product mockup | Optional | Mask-feathered 3D element with optical disc |
| `avatar-slot` | Author Profile Image | Yes | Crop original `avatar` pixels with circle frame |
| `qr-slot` | Official WeChat / Web QR code | Optional | Crisp vector SVG on `tail_qr_cta` |
| `brand-bar` | "aooby.cn · SilasFu" | Yes | Injected author watermark |
