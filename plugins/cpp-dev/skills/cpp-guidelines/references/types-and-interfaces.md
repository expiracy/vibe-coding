# C++ types, interfaces and library contracts

Apply these language-specific choices within the project's standard, public
interfaces, exception policy, ABI and performance requirements.

## Object semantics and polymorphism

Prefer values and the rule of zero. Standard containers and owning members
usually supply cleanup, copying and moving. If custom resource management needs
special members, deliberately define or delete the relevant copy, move and
destructor operations; do not add them mechanically to ordinary value types.

Use a class to protect an invariant and an aggregate for independent data.
Choose a callable or template for compile-time substitution when appropriate;
use runtime polymorphism when the interface really needs an open runtime set.
A base destroyed through a base pointer needs a virtual destructor. Otherwise
prevent that deletion where appropriate, such as with a protected non-virtual
destructor. Do not pass a polymorphic object by value and accidentally slice it.

For a small closed domain, an exhaustive enum switch can be suitable. Listing
every enumerator without a masking default helps compilers report additions.
Use `std::variant` and visitation when alternatives carry different value data.
Validate external text or numbers before treating them as a valid domain enum.

Sources: Core Guidelines C.2, C.20, C.21, C.35 and C.67.

## Initialization, values and parameter passing

Initialize objects before use. Brace initialization can reject narrowing, but
braces and parentheses can select different constructors, notably a container's
initializer-list constructor versus a size constructor. Choose the intended
operation rather than mechanically replacing parentheses with braces.

Pass cheap input values by value, larger read-only inputs by `const&`, and
required in-out objects by mutable reference. Prefer a returned value or result
record to unrelated output parameters. Choose a container reference or bounded
view such as C++20 `std::span` according to the caller's contract. A view does
not extend storage lifetime; asynchronous or queued work needs a valid lifetime
contract or an independent value. See [the pointer reference](pointers-and-lifetimes.md).

Validate untrusted sizes and indices. Avoid narrowing, C-style casts and casting
away `const`. Keep arithmetic range, signedness, units and overflow requirements
explicit; a named type does not make unchecked arithmetic safe.

Sources: Core Guidelines ES.20, ES.46, ES.49, ES.50 and F.16–F.21.

## Library operations and concurrency

Preserve the combined contract of library operations. `erase` can return the
iterator needed for traversal; `map::extract` transfers a node handle; stream
extraction updates its destination; atomic read-modify-write operations return
information coupled to the update. Do not split them into separate observations
and mutations when correctness requires one operation.

Retain the synchronization needed by the complete operation. A separate
`contains` check does not make insertion safe, and an atomic counter does not
protect unrelated mutable state. Relaxed atomic ordering is appropriate only
when its limited contract is sufficient; it does not publish other data.
Shared ownership keeps an object alive but does not synchronize its contents.

Sources: Core Guidelines CP.2 and the specific library operation's contract.

## Identifiers and build modes

Names containing `__` anywhere are reserved to the implementation. Names that
start with an underscore followed by an uppercase letter are reserved everywhere;
names starting with an underscore are also reserved in the global namespace.
Retain legitimate local naming conventions, but do not introduce reserved names.

In tests, ordinary `assert` can be disabled by `NDEBUG`. Use the existing test
framework's checks or explicit failure handling when verification must also run
in that build mode. Match facilities to the declared standard: the examples in
this skill use C++20; later-standard facilities need explicit project support.

Reference: [reserved identifiers](https://en.cppreference.com/w/cpp/language/identifiers).
