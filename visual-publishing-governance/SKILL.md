---
name: visual-publishing-governance
description: >-
  Lock, produce, and audit visual publishing via built-in presets or reference-locking with stable composition, evidence-backed copy, and clean deliverables.
  Trigger on: (1) producing social-media long cards, covers, and copy from documents and user assets (avatar, QR code) using built-in layout presets without reference images,
  (2) extracting and locking composition, hierarchy, and color from supplied reference images,
  (3) correcting visual drift, attachment-role mistakes, saved-image watermark contamination, or rejected-output cleanup.
argument-hint: "produce | lock | audit"
---

# Visual Publishing Governance（预置模板与视觉发布治理）

Turn visual requirements into an explicit production contract—either by picking pre-approved layout presets (`templates/presets/`) or by extracting custom layout contracts from references—then keep content, rendering, and cleanup inside that contract.

## Modes

| Mode | Typical request | Output |
| :--- | :--- | :--- |
| `produce` | “根据文档、头像和二维码生成社媒长图与文案”（日常高频，免参考图） | Deterministically composed images using built-in presets (`templates/presets/`) or approved custom contracts, preview, and publish copy |
| `lock` | “完全按照参考图构图”“先锁定新版式” | `visual-job.json` plus one extracted layout contract per page family |
| `audit` | “检查差异”“去掉水印”“只保留合格图片” | Machine-readable audit, visual QA result, and an exact keep/delete list |

## Shared input contract

Classify every input before production because an attachment's presence does not authorize embedding it:

- `reference-layout`: composition evidence (Track B only; omitted in Track A preset flow);
- `content-source`: authoritative facts and wording;
- `avatar`: identity asset allowed in the designated identity slot;
- `qr-code`: official account or channel QR code allowed in designated QR slot;
- `brand-logo`: brand mark / icon allowed in designated logo slot;
- `identity-info`: profile screenshot or account page used to extract display name and positioning only;
- `illustration`: visual asset intended for composition;
- `watermark-sample`: saved-image watermark evidence used to define an exclusion region.

Start from [`templates/visual_job.template.json`](templates/visual_job.template.json). For zero-reference production, load pre-approved layouts from [`templates/presets/`](templates/presets/) and design tokens from [`references/category_theme_matrix.md`](references/category_theme_matrix.md). Read [`references/composition_lock_protocol.md`](references/composition_lock_protocol.md) whenever custom references are supplied. Read [`references/production_and_audit.md`](references/production_and_audit.md) before rendering or deleting outputs.

## Mode: lock (Custom Reference Track)

1. Inventory every attachment and content file with one role from the shared input contract.
2. Extract the reference's canvas ratio, zones, alignment lines, type hierarchy, palette, image coverage, and intentional empty space.
3. Create one layout contract per distinct page family from [`templates/layout_contract.template.json`](templates/layout_contract.template.json). Use pixel boxes on the canonical canvas and record an allowed tolerance.
4. Build `visual-job.json` with content sources, asset roles, page list, output names, forbidden text, and copy-length target.
5. Treat an explicit request such as “完全按照这张参考图” as approval of that reference family. Otherwise show the composition contract and obtain approval before setting `composition_lock.status` to `approved`.
6. Run:

   ```bash
   python <skill>/scripts/validate_visual_job.py <job>/visual-job.json --check-paths
   ```

**Completion Criterion**: every attachment has exactly one role; every planned page has an approved layout contract; identity-info and watermark-sample assets have `embed: false`; the validator exits `0`.

## Mode: produce (Preset & Locked Production)

1. When no reference images are provided, select standard approved layout contracts from [`templates/presets/`](templates/presets/) (`cover_hero`, `body_matrix`, `body_workflow`, `tail_qr_cta`). Otherwise use the locked contracts from Mode `lock`.
2. Validate the job manifest and read every `content-source`. Keep claims traceable to those sources; label user-provided effort or iteration counts as user statements.
3. Build a page content matrix before drawing: page purpose, headline, intro, left/right facts, conclusion, process flow, illustration, and source pointers.
4. Render text, cards, lines, and page geometry with a deterministic code-native layer. Preserve avatar and QR code pixels in designated slots; generate only isolated, transparent 3D illustrative assets.
5. Produce the cover, body pages, combined preview, and copy using [`templates/publish_copy.template.md`](templates/publish_copy.template.md).
6. Export an actual layout contract from the render source and compare it with the approved contract:

   ```bash
   python <skill>/scripts/compare_layout.py <approved.layout.json> <actual.layout.json>
   ```

7. Inspect every output at original resolution for line wrapping, avatar shape, text clipping, illustration edges, and unwanted watermark text.

**Completion Criterion**: all expected images exist at the declared dimensions; every layout comparison exits `0`; the preview contains every page; publish copy is within the declared character range; original-resolution visual QA passes.

## Mode: audit

1. Run the deterministic output audit:

   ```bash
   python <skill>/scripts/audit_outputs.py <job>/visual-job.json
   ```

2. Compare the final cover and one representative body page side-by-side with their references. Report concrete geometric differences instead of subjective reassurance.
3. Confirm that assets classified as `identity-info` or `watermark-sample` are absent from the composition and that forbidden strings are absent from render sources.
4. Build the exact keep list from `output.expected_images`. Treat extra images as rejected candidates.
5. Delete rejected files only inside the run-scoped output directory and only after user authorization; verify the resolved paths before deletion. Preserve source documents and reusable approved assets.

**Completion Criterion**: `audit_outputs.py` exits `0`; the original-resolution review finds no clipping, role violation, or saved-image watermark; the output directory contains exactly the expected image set.

## Delivery report

Report:

1. final cover and page links;
2. combined preview;
3. publish copy;
4. validator, layout comparison, and output audit status;
5. files removed and whether removal was recoverable.

