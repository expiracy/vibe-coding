---
name: clean-code
description: Apply language-independent Clean Code principles when reviewing or refactoring names, function responsibilities, comments, formatting, boundaries, error-flow readability, and tests. Use for design clarity and maintainability, rather than language or library mechanisms.
license: MIT
metadata:
  version: "1.0.0"
---

# Clean Code

Make the code's purpose and behavior easy to understand. Apply the principles
within the project's contracts and conventions, rather than treating them as
universal rules or quotas. Keep implementation mechanisms in language-specific
guidance; this skill is independently usable across languages.

## Review the design and its expression

- Choose names that reveal domain meaning, units, and meaningful distinctions.
- Keep functions cohesive and at a useful level of abstraction. Extract a named
  concept when it clarifies the work, not merely to shorten a function.
- Make important effects visible. A command may return its natural outcome;
  do not break an indivisible operation to enforce command/query separation.
- Use comments for reasons, constraints, and required contracts. Prefer clearer
  code to narration, while preserving meaningful documentation and notices.
- Follow project formatting so related concepts are easy to read together.
- Keep successful work readable and failures meaningful to callers. Distinguish
  an expected missing value from an error; preserve diagnostic context.
- Protect actual invariants and isolate dependencies that genuinely vary.
  Plain data records are valid when behavior-rich abstractions are unnecessary.
- Give each responsibility a clear home. Do not add hierarchies, wrappers, or
  forwarding methods solely to demonstrate a design principle.
- Make tests explain observable behavior. Several assertions may describe one
  concept; arbitrary assertion limits can make the story harder to follow.
- Remove duplicated knowledge and unnecessary structure while preserving
  behavior. Similar-looking code does not always represent the same policy.

## Read only the relevant detail

Use the [48-topic index](references/clean-code-index.md) to find the principle
needed for the current question. Read that rule and any relevant counterexample
or limitation, rather than loading the whole catalogue. The retained categories
and rankings provide source traceability, not an order that overrides correctness.

Check refactors against the project's existing behavior and meaningful checks.
Report actual results and any verification limits. A cleaner-looking change is
not evidence of correctness on its own.

[Source and adaptation notes](UPSTREAM.md) explain the collection's origin.
Use the [rule template](assets/templates/_template.md) only when extending it.
