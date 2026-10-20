---
name: clean-code
description: Apply the upstream Clean Code principles to Java code when writing, reviewing, or refactoring names, functions, comments, formatting, errors, objects, boundaries, classes, and tests. Uses Java examples; focuses on design and readability rather than language implementation policy.
license: MIT
metadata:
  version: "1.0.0"
  language-baseline: "Java 11"
---

# Clean Code for Java

Use the original [pproenca/dot-skills Clean Code collection](https://github.com/pproenca/dot-skills/tree/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code)
as the source for design and readability principles, illustrated here in Java.
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

## Use the Java examples appropriately

Examples target Java 11. Follow the project's declared version, public
interfaces, conventions and error policy; do not modernize unrelated code or
introduce a framework to reproduce an illustration.

The Java examples retain upstream application and test excerpts. Some need the
project's domain classes or existing test framework; they are not standalone
programs or instructions to install a new dependency. Java records are expressed
as ordinary Java 11 classes in this variant.

Use existing project checks and report what actually ran. Passing examples are
evidence about those examples, not proof that an application is correct or that
every principle applies universally.

[Source and adaptation notes](UPSTREAM.md) identify the exact upstream snapshot
and bounded corrections. Use the [rule template](assets/templates/_template.md)
only when extending the collection.
