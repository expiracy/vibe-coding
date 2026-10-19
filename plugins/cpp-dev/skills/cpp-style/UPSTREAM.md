# Sources and Adaptation

The retained Clean Code references derive from [pproenca/dot-skills](https://github.com/pproenca/dot-skills),
`skills/.experimental/clean-code`, upstream version 1.0.7 at commit
`cf93c57cac89d6fc3e4194686000411567f5caf3` (retrieved 7 October 2026).

The original MIT licence is retained in LICENSE. The original C++ adaptation keeps all 48
rule filenames and the ten categories, replaces polyglot examples with original
C++17 examples, removes unsubstantiated numerical benefit claims, and adds
language-specific guidance for ownership, lifetimes, errors, static/runtime
polymorphism, reserved identifiers, and actual project conventions. The C++
adaptation was retrieved from [expiracy/clean-code](https://github.com/expiracy/clean-code)
at commit `e9a84cc953a73588f2d180b86ac7a2940af62a93`.

The `cpp-style` refactor retains those references and adds independently written
guidance on pointers, ownership, lifetimes, interfaces, and other C++ practices,
based on the official [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
consulted on 12 October 2026. Linked rule IDs identify the source of each topic;
this is a focused guide, not a copy of the complete guidelines.

Robert C. Martin's Clean Code (2008) supplies the named principles. The linked
C++ Core Guidelines and language/library references supply C++ semantics. Neither
the book's author, the guidelines' authors, nor the upstream project endorses
this independent adaptation.

Checks of metadata, links, and example compilation establish package integrity
and basic code validity. A small agent application test is a smoke test, not a
claim of measured improvement across models or production C++ projects.
