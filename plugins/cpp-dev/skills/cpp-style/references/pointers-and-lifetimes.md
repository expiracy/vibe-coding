# Pointers, ownership, and lifetimes

Treat ownership, nullability, mutability, and lifetime as separate parts of the
contract. A smart pointer does not automatically make an interface safer.
These rules paraphrase the linked C++ Core Guidelines; apply them within the
project's language standard, ABI, and resource policies.

## Ownership

Prefer a local value or existing container when no dynamic lifetime is needed.
Use `std::unique_ptr<T>` for exclusive ownership and `std::shared_ptr<T>` when
multiple owners really must keep the same object alive. Prefer `make_unique`
and `make_shared` for normal allocation; respect existing custom deleters,
allocators, and construction constraints. To share an already owned object,
copy its `shared_ptr`; do not create another owning `shared_ptr` from `.get()`.
Separate control blocks for the same object can cause double release.

A raw `T*` or `T&` normally borrows. A legacy or C API can transfer ownership
through a raw pointer; document that exception and immediately put the resource
under its matching RAII manager. An existing `owner<T*>` annotation documents
ownership but does not perform cleanup. Avoid scattered `new`/`delete` and
`malloc`/`free`; confine necessary allocation and release to resource boundaries.

Sources: [R.1](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-raii),
[R.3](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-ptr),
[R.4](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-ref),
[R.5](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-scoped),
[R.11](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-newdelete),
[R.12](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-immediate-alloc),
[R.20–R.23](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-owner).

## Function parameters

Use `const T&` for a required read-only borrowed object and `T&` for a required
mutable one. For cheap input values, pass by value. Use `const T*` or `T*` when
absence is a legitimate part of the API. Ordinary object access should not
require a particular ownership mechanism from the caller.

Smart-pointer parameters describe changes to lifetime or ownership:

- `unique_ptr<T>` by value receives exclusive ownership; callers move an existing owner.
- `unique_ptr<T>&` lets the function replace or reset the caller's owner.
- `shared_ptr<T>` by value lets the function retain shared ownership beyond the call.
- `shared_ptr<T>&` lets the function replace or reset the caller's shared owner.
- `const shared_ptr<T>&` can express conditional retention; copy into an owner
  on the path that retains the object. Use a plain borrow when no path retains it.

Do not use `const unique_ptr<T>&` or `const shared_ptr<T>&` merely for inspection.
If an aliased shared owner might be reset by re-entrant calls, keep a local shared owner
alive while passing its pointee down the call chain. `.get()` is legitimate for
borrowing while the owner and pointee remain valid. For an exclusive owner,
prevent reset or other operations that would destroy the pointee during borrowed use.

Sources: [F.7](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-smart),
[F.16](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-in),
[F.17](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-inout),
[R.30](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-smartptrparam),
[R.32](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-uniqueptrparam),
[R.33](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-reseat),
[R.34](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-sharedptrparam-owner),
[R.35](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-sharedptrparam),
[R.36](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-sharedptrparam-const),
[R.37](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-smartptrget).
R.36's explanation remains provisional in the source; use the actual retention contract.

## Nullability and constness

Use `nullptr` for absence and check nullable pointers before dereferencing them.
A reference represents a required object; it can still dangle. Use an existing
`not_null` type when the project already has one and a pointer-shaped interface
requires non-null input. Do not add a library just for the annotation.

`const T*` permits observing a const pointee; `T* const` fixes the pointer's target
but still allows mutation of the pointee. Likewise, `const shared_ptr<T>` and
`const unique_ptr<T>` make the handle const, not `T`. Use `shared_ptr<const T>`
or `unique_ptr<const T>` when an owning interface must restrict pointee mutation.
Const access does not prevent mutation through other aliases.

Sources: [F.23](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-nullptr),
[F.60](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-ptr-ref).

## Lifetimes and weak observers

Borrowed pointers, references, iterators, `string_view`, and spans require valid
backing storage for every use. C++ can extend a temporary's lifetime in specific
reference bindings; copying or returning a reference, or capturing by reference,
does not carry that extension into another scope. Account for destruction,
container reallocation/erasure, temporary objects, and deferred callbacks. Return
an owning value when backing storage cannot survive the caller's use; never
return a view of a local string.

Use `weak_ptr` for a relationship that must not keep a shared object alive,
including a back-link that would otherwise form an ownership cycle. Call `lock()`
once, check its result, and retain that local owner throughout use. Checking
`expired()` before locking is not sufficient: the last owner can disappear
between the two calls. Reference-counted lifetime does not synchronize mutable
pointee state; use the project's synchronization for concurrent access.

Sources: [R.24](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rr-weak_ptr),
[F.43](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-dangle),
[F.53](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-value-capture),
[ES.65](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#res-deref).

## Ranges and bounds

Use a container reference or a supported view that carries the element count.
`std::span` requires C++20; in C++17 reuse a project view or a suitable container
reference. At an unavoidable pointer-and-size boundary, validate the pair and
indices before accessing data. Keep pointer arithmetic local to that boundary.

A span borrows its storage. `std::span` carrying a length does not guarantee
bounds-checked indexing; validate dynamic indices or use checked operations
provided by the actual container/view. Use `span<const T>` for read-only elements;
a const `span<T>` only makes the view handle const.

Sources: [F.24](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#rf-range),
[ES.42](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#res-ptr).

## Example: distinct borrowing and ownership contracts

**Correct (C++17, with checks that remain active under NDEBUG):**

```cpp
#include <memory>
#include <utility>

struct Widget { int id; bool refreshed{}; };

int inspect(const Widget& widget) { return widget.id; }

void edit(Widget* widget) {
    if (widget) widget->refreshed = true;
}

std::unique_ptr<Widget> receive(std::unique_ptr<Widget> widget) {
    return widget;
}

void reseat(std::unique_ptr<Widget>& owner) {
    owner = std::make_unique<Widget>(Widget{7});
}

bool refresh(const std::weak_ptr<Widget>& observer) {
    if (auto owner = observer.lock()) {
        owner->refreshed = true;
        return true;
    }
    return false;
}

int main() {
    auto owner = std::make_unique<Widget>(Widget{3});
    if (inspect(*owner) != 3) return 1;
    edit(nullptr);
    edit(owner.get());
    if (!owner->refreshed) return 2;

    auto received = receive(std::move(owner));
    if (owner || !received || inspect(*received) != 3) return 3;
    reseat(received);
    if (inspect(*received) != 7) return 4;

    auto shared = std::make_shared<Widget>(Widget{9});
    std::weak_ptr<Widget> observer = shared;
    if (!refresh(observer) || !shared->refreshed) return 5;
    shared.reset();
    if (refresh(observer)) return 6;
    return 0;
}
```

The example is single-threaded. The weak lock protects lifetime, not concurrent
access to `Widget` members.
