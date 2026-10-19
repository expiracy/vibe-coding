---
name: cpp-style
description: Use when writing, reviewing, or refactoring C++ code and tests, especially for style, pointer and reference contracts, ownership, lifetimes, interfaces, initialization, constness, or error handling. Follow the project's language standard and conventions.
license: MIT
metadata:
  version: "2.0.0"
  cpp-baseline: "17"
---

# C++ Style

Write clear, idiomatic C++ with explicit resource and interface contracts.
Use the [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
alongside the retained Clean Code principles. Correctness, lifetime safety, and
the project's contracts take precedence over stylistic preferences.

## Work within the project

- Read project instructions, nearby code, callers, and tests. Establish the
  declared C++ standard, exception policy, ownership, and meaningful checks.
- Preserve naming, formatter configuration, header/source layout, public APIs,
  ABI, thread-safety guarantees, and required performance. Make the smallest
  complete change; avoid unrelated modernization.
- Examples target C++17. Use `std::span`, ranges, concepts, or `std::jthread`
  only with C++20 support, and `std::expected` only with C++23 support.
- Read the supporting reference relevant to the decision. Do not load every
  reference or add a dependency merely to express a guideline.

## Default design choices

- **Values and resources:** prefer values, scoped objects, standard containers,
  and RAII. Avoid unnecessary allocation. Give acquired resources an owner
  immediately, including handles returned by C APIs.
- **Types and classes:** use the rule of zero. When custom resource management
  requires special members, deliberately define or delete the relevant copy,
  move, and destructor operations. Protect real invariants; use aggregates for
  independent data. If deletion occurs through a base pointer, its destructor
  must be virtual; otherwise prevent that deletion where appropriate.
- **Initialization and constness:** initialize objects before use. Prefer
  `const` for values and member functions that should not mutate state. Choose
  initialization syntax deliberately: braces and parentheses can select
  different constructors, particularly for containers.
- **Interfaces:** pass cheap input values by value and larger read-only inputs
  by `const&`; use mutable references for required in-out parameters. Prefer
  return values or a result struct to unrelated output parameters. Make
  ownership transfer, mutation, absence, and failure visible.
- **Type safety and bounds:** use domain types and scoped enums when useful.
  Avoid narrowing conversions, C-style casts, and casting away `const`.
  Prefer ranges and bounded views to unchecked pointer arithmetic; validate
  untrusted sizes and indices.
- **Errors:** retain the project's exception, result, or error-code contract.
  Use RAII on every exit. Catch where recovery or translation is possible;
  destructors must not throw. Cleanup alone does not make a transaction atomic.
- **Readability:** use intent-revealing names and cohesive functions. Comments
  explain non-obvious constraints and reasons. Length and argument counts prompt
  review; they are not quotas. Add no hierarchy, wrapper, hidden dependency, or
  getter/setter layer solely to satisfy a style rule.

These defaults draw on Core Guidelines R.1/R.5/R.12, C.20/C.21/C.35,
ES.20/ES.46/ES.49/ES.50, Con.1/Con.2, and F.16/F.17/F.20/F.21.

## Pointer and reference rules

Choose the type from the contract, not from a blanket preference for smart pointers.

| Contract | Usual type |
|----------|------------|
| Required read-only borrow | `const T&` |
| Required mutable borrow | `T&` |
| Optional borrow | `const T*` or `T*`; handle `nullptr` |
| Transfer exclusive ownership | `std::unique_ptr<T>` by value |
| Replace the caller's exclusive owner | `std::unique_ptr<T>&` |
| Retain shared ownership | `std::shared_ptr<T>` by value |
| Observe a shared lifetime | `std::weak_ptr<T>`; lock once before use |
| Borrow a range | Container reference or supported bounded view |

Raw pointers and references normally borrow. Owning raw pointers at a legacy or
C boundary need an explicit contract and matching resource manager. Prefer
`make_unique` for exclusive allocation; use `shared_ptr` only for an actual
shared lifetime. Ordinary object access should accept a borrow even when the
caller owns the object through a smart pointer.

Use `nullptr`. Keep the owner alive and account for invalidation. Never return
a pointer, reference, or view into a destroyed local object. Const on a pointer
or smart-pointer handle does not make its pointee const. Shared ownership does
not synchronize access to the object.

Read [pointer and lifetime details](references/pointers-and-lifetimes.md) for
parameter choices, weak pointers, bounds, aliasing, examples, and rule citations.

## Verification

For behavior changes, use a focused behavior test and observe the relevant
failure before implementation when execution is available. Before refactoring,
establish a passing baseline and cover behavior that must survive. Refactor under
passing tests. Use the existing build, tests, formatter, static analysis, and
suitable sanitizers. Report actual commands, results, and checks that could not
run. Without execution tools, supply commands and continue from actual user output.

## Supporting references

- [Clean Code reference index](references/clean-code-index.md): the preserved
  48 topics on naming, cohesion, comments, boundaries, errors, and tests.
- [Source provenance](UPSTREAM.md) and [metadata](metadata.json): sources,
  licence, and example baseline.
- [Rule authoring template](assets/templates/_template.md): when extending the
  retained Clean Code references.

This is an independent, provider-neutral guide, not an official endorsement or
an exhaustive copy of the C++ Core Guidelines.
