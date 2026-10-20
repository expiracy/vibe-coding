---
title: Use Comments to Explain Intent
impact: HIGH
impactDescription: preserves decision rationale for future readers
tags: cmt, intent, why, rationale
---

## Use Comments to Explain Intent

Good comments explain WHY, not WHAT. The code already tells you what it does. Comments should explain the reasoning behind a decision that cannot be expressed in code.

**Incorrect (narrating the code):**

```java
// Increment counter by 1
counter++;

// Loop through all employees
for (Employee employee : employees) {
    // Check if employee is active
    if (employee.isActive()) {
        // Add employee to list
        activeEmployees.add(employee);
    }
}

// Set the name
this.name = name;
```

**Correct (explaining intent):**

```java
// We use insertion sort here because the list is almost always nearly sorted,
// Choose an algorithm using actual workload requirements and measurements.
insertionSort(nearlyOrderedList);

// Format matches the external API's expected date format (ISO 8601 without timezone)
// Illustrative format contract; use the real project specification.
String formattedDate = date.format(DateTimeFormatter.ISO_LOCAL_DATE);

// Bias toward newer sessions - users expect recent data first
// Illustrative requirement: show the newest sessions first.
sessions.sort(Comparator.comparing(Session::getCreatedAt).reversed());
```

**Good comment situations:**
- Legal comments (copyright, license)
- Explanation of intent or rationale
- Clarification of obscure API behavior
- Warning of consequences
- TODO comments (temporary)

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-explain-intent](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-explain-intent.md).
