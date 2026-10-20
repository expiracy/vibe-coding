---
title: Wrap Third-Party APIs
impact: HIGH
impactDescription: makes dependency assumptions explicit
tags: bound, boundary, wrapper, third-party, dependency
---

## Wrap Third-Party APIs

When you use a third-party API, wrap it in a class you control. This minimizes your dependency on the third party, makes testing easier, and gives you a single place to change when the API evolves.

**Incorrect (direct dependency scattered across codebase):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
// Illustrative dependency stand-in, not a real vendor implementation.
struct ACMEPort {
    int status{};
    int read() const {
        if (status != 0) throw std::runtime_error("vendor port status " + std::to_string(status));
        return 42;
    }
};


int readTemperature(const ACMEPort& port) {
    try { return port.read(); }
    catch (const std::runtime_error& error) {
        throw std::runtime_error(std::string("Port unavailable: ") + error.what());
    }
}
int readPressure(const ACMEPort& port) {
    try { return port.read(); }
    catch (const std::runtime_error& error) {
        throw std::runtime_error(std::string("Port unavailable: ") + error.what());
    }
}
}
```

**Correct (wrapped behind your own interface):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
// Illustrative dependency stand-in, not a real vendor implementation.
struct ACMEPort {
    int status{};
    int read() const {
        if (status != 0) throw std::runtime_error("vendor port status " + std::to_string(status));
        return 42;
    }
};


class LocalPort {
    ACMEPort port;
public:
    explicit LocalPort(ACMEPort value) : port(value) {}
    int read() const {
        try { return port.read(); }
        catch (const std::runtime_error& error) {
            throw std::runtime_error(std::string("Port unavailable: ") + error.what());
        }
    }
};
int readTemperature(const LocalPort& port) { return port.read(); }
int readPressure(const LocalPort& port) { return port.read(); }
}
```

**Benefits:**
- One place to change when the third-party API changes
- Easier to mock in tests (mock `LocalPort`, not the vendor library)
- Freedom to switch vendors without rewriting the entire codebase
- Consistent exception hierarchy under your control

**When NOT to wrap:**
- Stable, widely-used standard library APIs (e.g., `std::vector`, `std::string`) do not need wrapping.
- If the wrapper would be a 1:1 passthrough with no value added, it's premature. Wait until you have a concrete reason (testing, migration, or simplification).

Reference: [Clean Code, Chapter 8: Boundaries](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [bound-wrap-third-party](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/bound-wrap-third-party.md).
