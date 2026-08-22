# Composition Lock Protocol

## 1. Dual-track layout selection

Choose the track based on user input:

- **Track A: Built-in Presets (`templates/presets/`)**: Use when user requests standard cards/posters with dynamic assets (avatar, QR code, content) without supplying reference images. Select pre-approved layouts (`cover_hero`, `body_matrix`, `body_workflow`, `tail_qr_cta`).
- **Track B: Reference-Locking**: Use when user supplies reference poster images to extract and lock a new custom layout contract.

## 2. Asset-role pass

Assign one role before extracting anything:

| Role | What it controls | Default embedding |
| :--- | :--- | :--- |
| `reference-layout` | Geometry, spacing, hierarchy, palette, image coverage | No |
| `content-source` | Claims, terminology, data, wording | No |
| `avatar` | Identity slot only (cropped/masked) | Yes |
| `qr-code` | Official account/channel QR code slot | Yes |
| `brand-logo` | Brand mark / icon slot | Yes |
| `identity-info` | Display name, role, biography, location | No |
| `illustration` | Approved art inside a declared zone | Yes |
| `watermark-sample` | Exclusion text or region caused by export platforms | No |

A public-account screenshot normally provides identity information. Reclassify it as embeddable content only when the user explicitly asks to show that screenshot.

## 3. Geometry extraction

Record the canonical canvas and every meaningful zone as `[x, y, width, height]`:

- category badge or brand bar;
- primary and secondary headline bounds;
- intro paragraph;
- main comparison or content cards;
- central overlap elements such as `VS`;
- conclusion strip;
- process/detail panel;
- CTA, avatar, and signature;
- hero illustration coverage;
- intentional empty-space regions.

Use alignment anchors as first-class data. Shared left edges and baselines are usually more visually important than isolated component sizes.

## 4. Typography and palette

Record font family, weight, nominal size, line height, and maximum lines for every text role. Record colors by semantic role: background, ink, accent, border, muted text, CTA, and atmosphere glow.

When exact fonts are unavailable, select one fallback before production and keep it fixed across every page. Reflow all pages after a fallback change.

## 5. Lock approval

Set the contract to `approved` only when:

- the user explicitly identifies the reference as the required composition; or
- the user approves a composition preview or contract.

Approval locks geometry and hierarchy, not factual content. Content may change inside its declared zones as long as the layout remains within tolerance.

## 6. Stable rendering rule

Use deterministic drawing for words, lines, cards, masks, and cropping. Full-poster generative rendering causes text errors and layout drift. Limit generative tools to isolated, preferably transparent, illustrative assets; composite them through the deterministic renderer.

