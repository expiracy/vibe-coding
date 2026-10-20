---
title: Separate Commands from Queries
impact: MEDIUM
impactDescription: eliminates ambiguous function behavior
tags: func, cqs, command, query, separation
---

## Separate Commands from Queries

Functions should either do something or answer something, but not both. Either your function changes the state of an object, or it returns information about that object.

**Incorrect (command and query mixed):**

```cpp
#include <map>
#include <string>

namespace example {
class Settings {
    std::map<std::string, std::string> attributes;
public:
    bool set(const std::string& attribute, const std::string& value) {
        attributes[attribute] = value;
        return true; // The name does not explain the result.
    }
};
}
```

**Correct (separated command and query):**

```cpp
#include <map>
#include <string>

namespace example {
class Settings {
    std::map<std::string, std::string> attributes;
public:
    bool attributeExists(const std::string& attribute) const {
        return attributes.find(attribute) != attributes.end();
    }
    void setAttribute(const std::string& attribute, const std::string& value) {
        attributes[attribute] = value;
    }
};
}
```

**Alternative (return new state for immutable design):**

```cpp
#include <map>
#include <string>

namespace example {
class Settings {
    std::map<std::string, std::string> attributes;
public:
    Settings withAttribute(const std::string& attribute, const std::string& value) const {
        Settings updated = *this;
        updated.attributes[attribute] = value;
        return updated;
    }
};
}
```

The separation makes ordinary single-threaded usage easier to read. A command
may return its natural result; do not split checking and updating when the
operation must remain atomic.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-command-query-separation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-command-query-separation.md).
