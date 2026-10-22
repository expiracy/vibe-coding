# C++ resources and error mechanisms

## Cleanup on every exit

Acquire resources directly into a matching owner. Prefer existing streams,
containers, lock guards and project wrappers; a custom deleter is useful at a
C API boundary. Scoped destruction handles early returns and exception
unwinding. C++ has no `finally` block.

**Incorrect: a read-failure return leaks the file handle.**

```cpp
#include <cstdio>
#include <optional>

std::optional<unsigned char> read_first_byte(const char* path) {
    auto* file = std::fopen(path, "rb");
    if (!file) return std::nullopt;
    unsigned char byte{};
    if (std::fread(&byte, 1, 1, file) != 1) return std::nullopt;
    std::fclose(file); // The early read-failure return leaks the handle.
    return byte;
}
```

**Correct: the owner closes the handle on every exit.**

```cpp
#include <cstdio>
#include <memory>
#include <variant>

enum class ReadError { open_failed, read_failed };
using ReadResult = std::variant<unsigned char, ReadError>;

ReadResult read_first_byte(const char* path) {
    using File = std::unique_ptr<std::FILE, decltype(&std::fclose)>;
    File file{std::fopen(path, "rb"), &std::fclose};
    if (!file) return ReadError::open_failed;
    unsigned char byte{};
    if (std::fread(&byte, 1, 1, file.get()) != 1) {
        return ReadError::read_failed;
    }
    return byte;
}
```

This C++20 example also works with exceptions disabled. It distinguishes open
failure, read failure and success without discarding the cleanup contract.

## Error channels and guarantees

Keep the project's exception, result or error-code policy. In exception-disabled
code, use its existing error-value convention rather than adding throwing APIs
or `try`/`catch`. A success result and an error should not be simultaneously
present; use the existing result type or an appropriate discriminated union.

Catch exception types by reference, commonly `const std::exception&`, at a point
that can recover, translate or report. Preserve an original `std::error_code`
when returning a contextual error record. `std::throw_with_nested` can preserve
an exception cause when the reporting layer understands nested exceptions.

Define the required exception guarantee for state changes. Resource cleanup
does not roll back business state or make multiple writes transactional.
Destructors must not throw. For an output stream or transaction, provide and
check an explicit flush, close or commit when failure matters; destructor
cleanup alone cannot reliably report it.

## Optional values versus borrowed objects

Use `std::optional<T>` for an optional value when appropriate. C++20 does not
provide `std::optional<T&>`; a documented pointer or
`optional<reference_wrapper<T>>` can describe a borrow. Such a wrapper does not
extend lifetime. Use a copied value or stable identifier when the lifetime
cannot be ensured. Check null results from C APIs before use, and distinguish
operational failures from an ordinary absent result.

The [pointer reference](pointers-and-lifetimes.md) specifies ownership transfer,
nullable borrows, invalidation, weak observers and shared state constraints.

Sources: [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines),
especially R.1/R.12, E.6, E.15 and E.16. The file example is retained from the
former `cpp-style` package; see [source notes](../UPSTREAM.md).
