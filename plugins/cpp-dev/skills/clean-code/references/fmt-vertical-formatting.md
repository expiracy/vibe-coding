---
title: Use Vertical Formatting for Readability
impact: HIGH
impactDescription: enables scanning code like a newspaper
tags: fmt, vertical, whitespace, organization
---

## Use Vertical Formatting for Readability

Code should read like a newspaper article: headline at the top, details as you go down. Use vertical whitespace to separate concepts. Keep related code close together.

**Incorrect (no vertical organization):**

```cpp
#include <map>
#include <string>

namespace example {
class WikiPageResponder {
std::map<std::string, std::string> pages;
public:
explicit WikiPageResponder(const std::map<std::string, std::string>& values):pages(values){}
std::string makeResponse(const std::string& resource) const {
auto page=pages.find(resource);
if(page==pages.end())return "not found";
return "<page>"+page->second+"</page>";
}
};
}
```

**Correct (vertical formatting applied):**

```cpp
#include <map>
#include <string>

namespace example {
class WikiPageResponder {
    std::map<std::string, std::string> pages;

public:
    explicit WikiPageResponder(const std::map<std::string, std::string>& values)
        : pages(values) {}

    std::string makeResponse(const std::string& resource) const {
        const auto page = pages.find(resource);
        if (page == pages.end()) return "not found";

        return makePageResponse(page->second);
    }

private:
    std::string makePageResponse(const std::string& content) const {
        return "<page>" + content + "</page>";
    }
};
}
```

**Guidelines:**
- Blank lines between concepts (methods, logical sections)
- Related code grouped together
- Caller above callee (top-down reading)
- Variable declarations close to their usage

Reference: [Clean Code, Chapter 5: Formatting](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [fmt-vertical-formatting](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/fmt-vertical-formatting.md).
