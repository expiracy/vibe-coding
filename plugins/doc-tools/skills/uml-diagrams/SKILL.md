---
name: uml-diagrams
description: Create or edit common software diagrams in LaTeX/TikZ for Markdown documentation. Use for sequence diagrams, object snapshots, class models, architecture/component views, and activity/workflow diagrams.
---

# UML Diagrams

Create Markdown diagram assets: editable TikZ source, an SVG or PNG preview, and a vector PDF when available.

## Choose the view

Keep the choice to these five views. Choose from the question the reader needs
answered; do not make the user navigate a catalogue of UML terminology.

| Scenario | Diagram |
|----------|---------|
| Who calls whom, and in what order? | **Sequence** |
| Which concrete objects, values and links exist at one moment? | **Object** |
| What types exist, and how do they relate? | **Class** |
| What are the main services/components and their connections? | **Architecture** (component view) |
| What steps, choices or parallel paths make up a process? | **Activity/workflow** |

Honour an explicitly requested supported type; otherwise choose one view and
briefly explain why. Class diagrams show types; object diagrams show particular
instances. For architecture, default to a high-level component view and omit
class members and implementation mechanics. Label plain block views as informal
architecture rather than formal UML.

Draw one focused view unless several are needed. Ask when missing information
would change its meaning. If a different diagram type is explicitly requested,
identify the scope difference instead of silently substituting another view.

Preserve supplied names, relationships, directions, multiplicities, message order, guards and timing. Mark illustrative assumptions; ask when missing semantics affect correctness. Do not infer ownership from pointer types or invent timing, cardinalities or failure policies.

## Reuse the canonical theme

Copy the shared preamble and `uml/` styles from [the template](assets/uml-class-template.tex) into self-contained source and replace its example body. Keep the blue/grey palette, sans-serif type, 0.65pt strokes, 10pt body and 9pt labels. [The preview](assets/uml-class-preview.png) shows the theme.

Use the correct UML symbols for the view. Read [the reference](references/uml-and-layout.md) for its notation and relevant compartment, arrow or layout details. Reserve space for labels and connector routes; reflow before shrinking text.

## Compile and deliver

Prefer an available native source editor/compiler. Use the [existing command-line workflow](references/uml-and-layout.md#portable-build-and-visual-check) when rendered asset export requires it. Do not install a toolchain for an ordinary diagram request.

Compile and check errors, missing glyphs and overfull boxes. Render and inspect at the intended Markdown width for notation, complete text, labels, connectors, overlaps and clipping. Fix the source and re-render after changes; compilation alone does not verify layout.

Keep existing asset paths. In Vault, use `features/assets/<feature-id>/` for new feature assets and the task's `assets/` for task-only media. Embed previews with relative Markdown image links and keep `.tex` source beside them.

Report source and preview paths, actual checks and limitations. If compilation, export or inspection is unavailable, retain the source and mark that scope unverified.
