---
name: cpp-guidelines
description: Apply recommended C++ language and library practices for resources, pointer/reference contracts, lifetimes, object semantics, initialization, constness, parameter passing, type safety, and error mechanisms. Use when making or reviewing these C++ implementation choices.
license: MIT
metadata:
  version: "1.0.0"
  cpp-baseline: "17"
---

# C++ Guidelines

Choose C++ types, resource managers, and library facilities from their contracts.
Apply the relevant [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
to language and library decisions. Correctness, resource safety, the declared
language standard, and the project's contracts govern these choices.

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

## Default C++ choices

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

## Additional C++ details

- [Types, interfaces and library contracts](references/types-and-interfaces.md):
  special members, polymorphic destruction, closed alternatives, initialization,
  reserved identifiers, combined library operations and concurrency constraints.
- [Resources and error mechanisms](references/resources-and-errors.md):
  resource cleanup, error channels, optional values and exception guarantees.

Read only the reference relevant to the C++ decision being made. These resources
do not require loading another skill or a general design-rule catalogue.

## Verification

Use the declared language standard and the existing build, tests, formatter,
static analysis and suitable sanitizers. Check relevant contracts before and
after a change. Ensure test checks remain active in the build modes being used;
ordinary `assert` checks can disappear under `NDEBUG`. Report actual execution
results and anything that could not be verified.

[Source notes](UPSTREAM.md) identify the guide's origin and scope. Use the
[C++ rule template](assets/templates/_template.md) only when extending it.

This independent, provider-neutral skill is a focused selection of C++ guidance,
not an exhaustive copy of the Core Guidelines or a guarantee of conformance.
