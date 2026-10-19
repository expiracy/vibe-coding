# UML notation and TikZ layout

Reuse the shared preamble and `uml/` styles in the template for every diagram type. Copy them into self-contained generated assets. Preserve model semantics while adapting layout; these practical defaults do not replace the UML specification or provide automatic layout.

## Diagram types

Use the skill's five-view menu for ordinary software documentation. This table
gives the corresponding notation without introducing additional diagram types.

| Type | Required distinction and canonical primitives |
|------|-----------------------------------------------|
| Sequence | Lifelines, ordered messages, executions and fragments; `uml/lifeline-head`, `uml/lifeline`, call/reply styles, `uml/activation`, frame geometry. |
| Object | Concrete instances, slot values and links at one moment; `uml/object`, underlined `name : Type` headings, `uml/link`. |
| Class | Classifiers, compartments and typed relationships; `uml/class`. |
| Architecture (component view) | High-level components and interfaces/dependencies; `uml/component` with the component keyword or icon when using formal UML. |
| Activity/workflow | Actions, flows, decisions, concurrency and finals; `uml/action`, `uml/control-flow`, `uml/decision`, `uml/bar`, final styles. |

Source: [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF).

## Objects: an instance snapshot

An object diagram shows specific instances at one moment, not the design of their
types. Use `uml/object` with two compartments: an underlined `name : Type` heading
and relevant slots such as `status = paid`. An anonymous instance can use `: Type`.
Do not add an operations compartment or replace actual values with type declarations.

Use solid `uml/link` connections between instances, with supplied role names.
Links must agree with any supplied class model. Do not invent missing instances,
slot values or ownership. Label illustrative snapshots as examples.

```tex
\node[uml/object] (order) {
  \underline{order1 : Order}
  \nodepart[align=left]{two}status = paid
};
\node[uml/object,right=20mm of order] (customer) {
  \underline{customer1 : Customer}
  \nodepart[align=left]{two}name = ``Alice''
};
\draw[uml/link] (order.east) --
  node[uml/label,midway,above=2pt] {customer} (customer.west);
```

Sources: UML 2.5.1 §9.8 and [IBM's instance notation](https://developer.ibm.com/articles/the-class-diagram/#instances).

## Activities: a workflow

Activities use rounded actions, rectangular object nodes/pins, decision/merge diamonds and fork/join bars. `uml/control-flow` and `uml/object-flow` have solid open heads. Label decision guards `[condition]`; decisions select alternatives while forks create concurrent flows. `uml/initial` is a filled circle; `uml/activity-final` is a bull's-eye stopping all flows; `uml/flow-final` is a circled X terminating only that flow.

Keep the workflow focused on the requested process. Start with actions, guarded
choices and a clear end; add concurrency only when the process requires it.

Source: UML 2.5.1 §§15.2.4–15.3.4.

## Relationship direction and meaning

| Relationship | Template style | Meaning and direction |
|--------------|----------------|-----------------------|
| Association | `uml/association` | Solid line; add navigability only when specified. |
| Object link | `uml/link` | Solid line between concrete instances; preserve any supplied role names. |
| Dependency | `uml/dependency` | Dashed line and open barb, from client to supplier. |
| Generalization | `uml/generalization` | Solid line and hollow triangle, from child to parent. |
| Interface realization | `uml/realization` | Dashed line and hollow triangle, from implementation to interface. |
| Shared aggregation | `uml/aggregation` | Hollow diamond at the whole end; use only when that relationship is intended. |
| Composition | `uml/composition` | Filled diamond at the whole end; composition expresses stronger whole/part semantics. |
| Annotation | `uml/note-link` | Dashed connector without an arrowhead; formal comments use the folded-corner `uml/note`. |
| Activity control/object flow | `uml/control-flow` / `uml/object-flow` | Solid open-head flow with the supplied guard/token meaning. |

The template's aggregation and composition styles put the diamond at the start
of the path: draw from the whole toward the part. Draw generalizations and
realizations toward the parent/interface. Arrow decoration does not reverse
the model's meaning automatically.

Put a multiplicity next to the endpoint whose instances it counts. For an order
with one or more lines, put `1..*` beside OrderLine; put `1` beside Order when each
line belongs to exactly one order. Do not infer composition from a pointer field,
or shared aggregation from use of a shared-pointer type.

Sources: [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/PDF) and
[TikZ arrow configuration](https://tikz.dev/tikz-arrows).

## Classes and text

Use `rectangle split` with three parts for the name, attributes, and operations.
The part names are `text`, `two`, and `three`; the first is implicit in the
template. `rectangle split ignore empty parts=false` keeps empty compartments
visible. Vertical split nodes do not honour `minimum height` as a uniform-height
control; account for the actual text and padding in each compartment.

Use `text width` to enable wrapping; `minimum width` alone does not wrap text.
Set `align=left` on the attribute/operation parts. `rectangle split part align`
positions the part boxes and is not the same as the text alignment within them.
Keep class headings centred and emphasised consistently.

Do not let TeX hyphenate a type name into a different-looking identifier.
Widen related boxes together, break before a long type, or break a signature at
argument boundaries. Escape label characters such as underscores, percent signs,
ampersands, and hashes. Preserve symbols and requested visibility notation.

Sources: [Multipart shapes](https://tikz.dev/library-shapes) and
[node text and alignment](https://tikz.dev/tikz-shapes).

## Spacing, routes, labels, and groups

With the `positioning` library, `right=16mm of A` uses the relevant node borders.
Legacy `right of=A`, explicit centre coordinates, and `on grid` can give very
different spacing. Align row tops with common coordinates when node heights differ.
Choose the next row from the tallest relevant box, not an assumed fixed height.

Start with 12–20mm horizontal gaps and 20–26mm between class rows, then adjust
to the rendered content. Set widths and deliberate line breaks before routing.

`-|` goes horizontally then vertically; `|-` goes vertically then horizontally.
Neither searches for obstacles. Select departure/arrival anchors that match the
path direction and add explicit waypoints or offset lanes for congested routes.
Avoid shared segments that make distinct relationships hard to follow.

Place text on an explicitly chosen straight segment. A `pos=.5` label on a
single `-|` or `|-` operation sits at the bend. Split the route into segments
for predictable label positioning, and keep endpoint labels clear of arrowheads.
Small background fills can make labels readable; do not use them to conceal a
collision. Inspect the underlying route as well as the visible stroke.

For a group, create its members first, then an empty `fit` node with padding and
a separately positioned title. Fit includes the specified nodes' cardinal
anchors; separate notes, labels, and routes need inclusion or additional space.
Put group fills on a background layer and specify their drawing styles there.
Draw outer group fills before inner ones when nested.

Sources: [Positioning and labels](https://tikz.dev/tikz-shapes),
[path bends](https://tikz.dev/tikz-paths), [fit](https://tikz.dev/library-fit),
and [background layers](https://tikz.dev/library-backgrounds).

## Architecture: a component view

Show the main services/components, their responsibilities, and the relevant
interfaces or dependencies at one consistent level of detail. Avoid class
compartments, methods and low-level configuration in an architecture overview.

For formal UML components, use `uml/component` with a visible component keyword
or correct UML icon; do not invent an icon that suggests a different kind of entity.
Use the same typography, colours, padding, and relationship conventions as the
class diagrams. Label an informal block diagram as informal architecture and
label its connections with their intended meaning. Architecture is the purpose
of the view, not a separate formal UML diagram type; the default here is a
component diagram. A dependency arrow does not establish runtime message order.

The interface and component labels are UML keywords, not profile stereotypes. Use T1 guillemets (`\guillemotleft` / `\guillemotright`) around keywords and stereotype names.

Source: [IBM's component-diagram guide](https://developer.ibm.com/articles/the-component-diagram/).

## Sequence diagrams

Use `uml/lifeline-head` for participant headers and `uml/lifeline` for vertical
lifelines. Allocate increasing event rows and space for each message label.
Use `uml/call` for synchronous calls and `uml/async` for asynchronous calls.
The template convention is `uml/reply` for dashed, open-barb replies; label
messages and keep self-calls and activation bars clear of neighbouring lifelines.

Sequence time flows downward. Use the UML pentagonal heading tab for the outer `sd` frame and combined fragments; preserve supplied fragment operators and guards. Preserve requested call order and distinguish
simultaneous or asynchronous behaviour from a synchronous call. For formal UML,
use its actual notation for combined fragments and activation bars rather than
implying those meanings through arbitrary boxes or colours.

Sources: [OMG UML](https://www.omg.org/spec/UML/2.5.1/PDF) and
[reply-arrow clarification](https://issues.omg.org/issues/UMLR-317).

## Portable build and visual check

For a standalone asset, keep the template's explicit border. For a figure embedded
in a document, use that document's preamble and check the figure at its final
width. Cropping to the TikZ bounding box does not prove that it fits an A4 page.

An example local workflow, using available TeX and Poppler tools:

```sh
mkdir -p build
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build diagram.tex
pdftoppm -png -r 150 -singlefile build/diagram.pdf build/diagram
```

An existing editor/preview or a compatible LaTeX engine can provide the same
compile-and-inspect loop. Do not enable shell escape for the supplied template.
Keep intermediate build files separate from source. Retain a chosen SVG/PNG preview beside the editable source for Markdown embedding, plus the vector PDF when useful. Existing PDF-to-SVG or PDF-to-PNG tools can provide the preview; no prose LaTeX report is needed. Re-render after source changes and
inspect the actual latest image; warnings alone cannot detect hyphenated names,
incorrect arrow semantics, or overlapping annotations.

Use the whole-page view to check composition and margins, then enlarged views
to check labels, compartments, and connectors. If the canvas is crowded, reorder
nodes, reroute edges, adjust common widths/gaps, or split views when permitted by
the request. Do not solve congestion by making text unreadably small.

Plain TikZ placement is explicit geometry. The separate graphdrawing system can
calculate layouts, but requires LuaTeX and a selected layout library and still
needs visual checking. Introduce it only when the task calls for that capability.

Sources: [Standalone manual](https://tug.ctan.org/macros/latex/contrib/standalone/standalone.pdf)
and [graphdrawing prerequisites](https://tikz.dev/gd-usage-tikz).
