---
title: Use Searchable Names
impact: HIGH
impactDescription: enables effective code navigation
tags: name, searchable, constants, refactoring
---

## Use Searchable Names

Single-letter names and numeric constants are hard to locate across a body of text. Longer names trump shorter names, and searchable names trump convenient abbreviations.

**Incorrect (unsearchable):**

```cpp
#include <array>

namespace example {
int estimate(const std::array<int, 34>& t) {
    int s = 0;
    for (int j = 0; j < 34; ++j) s += (t[j] * 4) / 5;
    return s;
}
}
```

**Correct (searchable and meaningful):**

```cpp
#include <array>
#include <cstddef>

namespace example {
int estimate(const std::array<int, 34>& taskEstimate) {
    constexpr int realDaysPerIdealDay = 4;
    constexpr int WORK_DAYS_PER_WEEK = 5;
    constexpr std::size_t NUMBER_OF_TASKS = 34;
    int sum = 0;
    for (std::size_t taskIndex = 0; taskIndex < NUMBER_OF_TASKS; ++taskIndex) {
        const int realTaskDays = taskEstimate[taskIndex] * realDaysPerIdealDay;
        sum += realTaskDays / WORK_DAYS_PER_WEEK;
    }
    return sum;
}
}
```

Now you can search for `WORK_DAYS_PER_WEEK` and find every place it is used. Try searching for `5` in a large codebase.

**Exception:** Single-letter names are acceptable only as local variables in short methods. The length of a name should correspond to the size of its scope.

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-searchable](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-searchable.md).
