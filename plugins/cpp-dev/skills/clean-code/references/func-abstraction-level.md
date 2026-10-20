---
title: Maintain One Level of Abstraction
impact: CRITICAL
impactDescription: prevents jarring context switches
tags: func, abstraction, stepdown, readability
---

## Maintain One Level of Abstraction

Statements within a function should all be at the same level of abstraction. Mixing high-level concepts with low-level details is confusing. Code should read like a top-down narrative.

**Incorrect (mixed abstraction levels):**

```cpp
#include <algorithm>
#include <cctype>
#include <map>
#include <sstream>
#include <string>

namespace example {
struct Document { std::string text; };
using WordFrequency = std::map<std::string, int>;


std::string analyzeDocument(const Document& document) {
    std::string text = document.text;
    std::transform(text.begin(), text.end(), text.begin(),
        [](unsigned char ch) { return static_cast<char>(std::tolower(ch)); });
    std::istringstream words(text);
    WordFrequency counts;
    for (std::string word; words >> word;) ++counts[word];
    std::ostringstream output;
    for (const auto& entry : counts) output << entry.first << ": " << entry.second << '\n';
    return output.str();
}
}
```

**Correct (consistent abstraction level):**

```cpp
#include <algorithm>
#include <cctype>
#include <map>
#include <sstream>
#include <string>

namespace example {
struct Document { std::string text; };
using WordFrequency = std::map<std::string, int>;


std::string normalizeText(const Document& document) {
    std::string text = document.text;
    std::transform(text.begin(), text.end(), text.begin(),
        [](unsigned char ch) { return static_cast<char>(std::tolower(ch)); });
    return text;
}
WordFrequency analyzeFrequency(const std::string& text) {
    WordFrequency counts;
    std::istringstream words(text);
    for (std::string word; words >> word;) ++counts[word];
    return counts;
}
std::string formatResults(const WordFrequency& counts) {
    std::ostringstream output;
    for (const auto& entry : counts) output << entry.first << ": " << entry.second << '\n';
    return output.str();
}
std::string analyzeDocument(const Document& document) {
    return formatResults(analyzeFrequency(normalizeText(document)));
}
}
```

Read the code from top to bottom. Each function introduces the next level of abstraction.

**When mixing levels is acceptable:**
- Short utility functions (under 10 lines) that perform one task can mix levels without confusion. The overhead of extracting one-line helpers often exceeds the readability benefit.
- Test code frequently mixes setup (low-level) with assertions (high-level) — this is expected and follows the Arrange-Act-Assert pattern.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-abstraction-level](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-abstraction-level.md).
