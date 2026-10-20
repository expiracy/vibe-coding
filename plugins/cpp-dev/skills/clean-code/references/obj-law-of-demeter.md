---
title: Follow the Law of Demeter
impact: MEDIUM-HIGH
impactDescription: prevents hidden dependencies between modules
tags: obj, demeter, coupling, encapsulation
---

## Follow the Law of Demeter

A method should only call methods on: its own object, objects passed as parameters, objects it creates, or its direct component objects. Avoid chained method calls on returned objects.

**Incorrect (train wreck - violates Law of Demeter):**

```cpp
#include <string>

namespace example {
struct ScratchDir { std::string absolutePath{"scratch"}; std::string getAbsolutePath() const { return absolutePath; } };
struct Options { ScratchDir scratchDir; const ScratchDir& getScratchDir() const { return scratchDir; } };
struct Context { Options options; const Options& getOptions() const { return options; } };


std::string scratchLocation(const Context& context) {
    return context.getOptions().getScratchDir().getAbsolutePath();
}
}
```

**Correct (respects object boundaries):**

```cpp
#include <sstream>
#include <string>

namespace example {
struct ScratchDir { std::string absolutePath{"scratch"}; std::string getAbsolutePath() const { return absolutePath; } };
struct Options { ScratchDir scratchDir; const ScratchDir& getScratchDir() const { return scratchDir; } };
struct Context { Options options; const Options& getOptions() const { return options; } };


class Workspace {
public:
    std::ostringstream createScratchBuffer() const { return std::ostringstream{}; }
};
std::string renderScratch(const Workspace& workspace) {
    auto buffer = workspace.createScratchBuffer();
    buffer << "temporary report";
    return buffer.str();
}
}
```

**Exception:** The Law of Demeter does not apply to data structures. If `Options`, `ScratchDir`, etc. are just data containers without behavior, the chaining is acceptable:

```cpp
#include <string>

namespace example {
struct ScratchDir { std::string absolutePath{"scratch"}; std::string getAbsolutePath() const { return absolutePath; } };
struct Options { ScratchDir scratchDir; const ScratchDir& getScratchDir() const { return scratchDir; } };
struct Context { Options options; const Options& getOptions() const { return options; } };

// This is an explicit data record, not navigation through hidden object internals.
std::string scratchLocation(const Context& context) { return context.options.scratchDir.absolutePath; }
}
```

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-law-of-demeter](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-law-of-demeter.md).
