---
title: Keep Functions Small
impact: CRITICAL
impactDescription: enables comprehension at a glance
tags: func, size, readability, comprehension
---

## Keep Functions Small

Functions should be small. They should be smaller than that. Review function responsibilities rather than imposing a fixed line limit. Each function should do one thing, do it well, and do it only.

**Incorrect (large function doing multiple things):**

```cpp
#include <string>

namespace example {
struct PageData { bool test{}; std::string content; };


void renderPageWithSetupsAndTeardowns(PageData& pageData, bool isSuite) {
    if (pageData.test) {
        std::string content;
        if (isSuite) content += "suite setup\n";
        content += "setup\n";
        content += pageData.content;
        content += "teardown\n";
        if (isSuite) content += "suite teardown\n";
        pageData.content = content;
    }
}
}
```

**Correct (small, focused functions):**

```cpp
#include <string>

namespace example {
struct PageData { bool test{}; std::string content; };


std::string getSetups(bool suite) { return suite ? "suite setup\nsetup\n" : "setup\n"; }
std::string getTeardowns(bool suite) { return suite ? "teardown\nsuite teardown\n" : "teardown\n"; }
std::string buildPageContent(const PageData& page, bool suite) {
    return getSetups(suite) + page.content + getTeardowns(suite);
}
void includeSetupsAndTeardowns(PageData& page, bool suite) {
    page.content = buildPageContent(page, suite);
}
void renderPageWithSetupsAndTeardowns(PageData& pageData, bool isSuite) {
    if (pageData.test) includeSetupsAndTeardowns(pageData, isSuite);
}
}
```

The helpers express focused concepts at a useful level of abstraction; their line counts are not quotas.

**When NOT to apply this pattern:**
- If a 15-20 line function does one thing at one level of abstraction, it does not need further decomposition. The goal is comprehensibility, not minimizing line count.
- Do not extract functions that are only called from one place and whose names merely restate their implementation — this adds indirection without clarity.
- Ousterhout's "deep modules" critique: extremely small functions can create "shallow modules" that spread logic across many files, forcing readers to jump between functions to understand a single behavior. Balance depth (functionality per interface) against size.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-small](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-small.md).
