# Production and Audit Protocol

## Content matrix

Create the matrix before rendering:

| Field | Required content |
| :--- | :--- |
| Page purpose | One job for the page |
| Headline | Short enough for the locked bounds |
| Supporting facts | Traceable source pointers |
| Conclusion | One defensible takeaway |
| Flow | Three to five ordered steps when the layout contains a process region |
| Illustration | Asset ID and role |

Prefer six readable pages over compressing an entire guide into one unreadable poster. Use the document structure to decide the page sequence.

## Rendering strategy

1. Load the approved layout contract and the content matrix.
2. Render the canonical size first. Derive platform variants from that source rather than rebuilding them independently.
3. Preserve avatar pixels and aspect ratio. Crop with a mask; do not synthesize a new identity unless requested.
4. Generate illustration cutouts separately with transparent alpha. Verify corner alpha before compositing.
5. Save render sources beside the output so forbidden text and layout boxes remain auditable.

## Visual QA

Inspect at original resolution:

- title width and baseline against the reference;
- text wrapping and clipping;
- central overlaps and card padding;
- illustration coverage and unwanted rectangular backdrops;
- avatar shape and identity fidelity;
- absence of export-platform watermark text;
- consistent page numbering and output dimensions.

The combined preview is a navigation aid, not proof of original-resolution quality.

## Output hygiene

Use a run-scoped directory. Keep accepted outputs in `final/`, reusable approved assets in `assets/`, and drafts in `drafts/`. The manifest's `output.expected_images` is the sole keep list for final delivery.

Before deletion, resolve every target and prove it is inside the run-scoped directory. Delete only after user authorization. Report the number of removed files and whether the operation bypassed the recycle bin.

