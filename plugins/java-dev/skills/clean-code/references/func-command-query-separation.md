---
title: Separate Commands from Queries
impact: MEDIUM
impactDescription: eliminates ambiguous function behavior
tags: func, cqs, command, query, separation
---

## Separate Commands from Queries

Functions should either do something or answer something, but not both. Either your function changes the state of an object, or it returns information about that object.

**Incorrect (command and query mixed):**

```java
// Does this set the attribute and return success?
// Or check if attribute exists?
public boolean set(String attribute, String value) {
    // ... sets attribute and returns true if it was set
}

// Confusing usage
if (set("username", "bob")) {
    // Was username set, or did it already exist?
}
```

**Correct (separated command and query):**

```java
// Query - returns information
public boolean attributeExists(String attribute) {
    return attributes.containsKey(attribute);
}

// Command - changes state
public void setAttribute(String attribute, String value) {
    attributes.put(attribute, value);
}

// Clear usage
if (!attributeExists("username")) {
    setAttribute("username", "bob");
}
```

**Alternative (return new state for immutable design):**

```java
// For immutable patterns, returning new state is acceptable
public Settings withAttribute(String attribute, String value) {
    Map<String, String> updated = new HashMap<>(this.attributes);
    updated.put(attribute, value);
    return new Settings(updated);
}
```

The separation makes ordinary single-threaded usage easier to read. A command
may return its natural result; do not split checking and updating when the
operation must remain atomic.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-command-query-separation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-command-query-separation.md).
