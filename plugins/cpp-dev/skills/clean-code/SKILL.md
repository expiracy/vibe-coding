---
name: clean-code
description: Apply the upstream Clean Code principles to C++ code when writing, reviewing, or refactoring names, functions, comments, formatting, errors, objects, boundaries, classes, and tests. Focuses on design and readability rather than language implementation policy.
license: MIT
metadata:
  version: "1.3.0"
  language-baseline: "C++20"
---

# Clean Code for C++

Use the original [pproenca/dot-skills Clean Code collection](https://github.com/pproenca/dot-skills/tree/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code)
as the source for design and readability principles applied to C++.
The skill retains its 48 rules and ten categories. Read only the reference needed
for the current decision through the [rule index](references/clean-code-index.md).

## Apply the principles in context

- Use names that reveal intent and meaningful distinctions.
- Keep functions and classes focused on coherent responsibilities. Treat size
  and argument counts as review prompts, not quotas.
- Make effects and error contracts clear without breaking required combined
  operations or changing project failure conventions.
- Keep useful comments, required API documentation and notices. Prefer clearer
  expressions to narration and follow the project's formatting conventions.
- Separate data transfer, domain behavior and changing dependencies where the
  actual design benefits. Do not create wrappers or hierarchies by habit.
- Make tests describe one behavior with readable setup, action and checks.
  Several assertions may describe the same concept.
- Prefer a simple design that meets current requirements, expresses intent and
  avoids duplicated knowledge. Preserve observable behavior when refactoring.

## Apply the C++ constraints

Target C++20 for new code and examples. Respect an explicitly older project
baseline without silently changing its build standard. Follow public
interfaces, conventions and error policy; do not modernize unrelated code or
introduce a framework to reproduce an illustration.

Keep language/library implementation policies in the separate C++ guidance.
Most rules need only prose. Retain a short example only when it resolves an
ambiguity or a non-obvious failure; omit demonstration scaffolding. Use existing
project checks and report actual results.

[Source and adaptation notes](UPSTREAM.md) identify the exact upstream snapshot
and bounded corrections. Use the [rule template](assets/templates/_template.md)
only when extending the collection.
