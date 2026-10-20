---
title: Define Exceptions by Caller Needs
impact: HIGH
impactDescription: makes success and failure contracts understandable
tags: err, wrapper, classification, design
---

## Define Exceptions by Caller Needs

Define exception classes based on how they are caught, not on their source or type. Often a single exception class is sufficient for a particular area of code. Wrap third-party API exceptions.

**Incorrect (catching many exception types):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
struct DeviceResponseError : std::runtime_error { using std::runtime_error::runtime_error; };
struct DeviceTimeoutError : std::runtime_error { using std::runtime_error::runtime_error; };
void readVendorPort(int status) {
    if (status == 1) throw DeviceResponseError("invalid response");
    if (status == 2) throw DeviceTimeoutError("timed out");
}


std::string usePort(int status) {
    try { readVendorPort(status); return "ready"; }
    catch (const DeviceResponseError& error) { return std::string("port unavailable: ") + error.what(); }
    catch (const DeviceTimeoutError& error) { return std::string("port unavailable: ") + error.what(); }
}
}
```

**Correct (unified exception handling):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
struct DeviceResponseError : std::runtime_error { using std::runtime_error::runtime_error; };
struct DeviceTimeoutError : std::runtime_error { using std::runtime_error::runtime_error; };
void readVendorPort(int status) {
    if (status == 1) throw DeviceResponseError("invalid response");
    if (status == 2) throw DeviceTimeoutError("timed out");
}


struct PortUnavailable : std::runtime_error { using std::runtime_error::runtime_error; };
void readLocalPort(int status) {
    try { readVendorPort(status); }
    catch (const DeviceResponseError& error) { throw PortUnavailable(error.what()); }
    catch (const DeviceTimeoutError& error) { throw PortUnavailable(error.what()); }
}
std::string usePort(int status) {
    try { readLocalPort(status); return "ready"; }
    catch (const PortUnavailable& error) { return std::string("port unavailable: ") + error.what(); }
}
}
```

**Benefits of wrapping:**
- Minimizes dependencies on third-party APIs
- Easier to mock for testing
- Easier to switch implementations later
- Single exception type per area simplifies catching

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-define-by-caller-needs](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-define-by-caller-needs.md).
