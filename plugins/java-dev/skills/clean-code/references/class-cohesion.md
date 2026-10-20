---
title: Maintain Class Cohesion
impact: MEDIUM
impactDescription: enables extracting focused subclasses
tags: class, cohesion, variables, methods
---

## Maintain Class Cohesion

Classes should have a small number of instance variables. Each method should manipulate one or more of those variables. Methods should support a coherent concept; touching more fields does not make unrelated responsibilities cohesive.

**Incorrect (low cohesion - methods use different variables):**

```java
public class Utility {
    private Database db;
    private EmailService email;
    private Logger logger;
    private Cache cache;

    public void saveUser(User user) {
        db.save(user);  // Only uses db
        logger.log("Saved user");  // Only uses logger
    }

    public void sendNotification(String message) {
        email.send(message);  // Only uses email
    }

    public Object getCached(String key) {
        return cache.get(key);  // Only uses cache
    }
}
// Each method uses different instance variables - low cohesion
```

**Correct (high cohesion - methods use shared variables):**

```java
public class Stack {
    private int topOfStack = 0;
    private List<Integer> elements = new LinkedList<>();

    public int size() {
        return topOfStack;  // Uses topOfStack
    }

    public void push(int element) {
        topOfStack++;  // Uses topOfStack
        elements.add(element);  // Uses elements
    }

    public int pop() throws EmptyStackException {
        if (topOfStack == 0)
            throw new EmptyStackException();
        int element = elements.get(--topOfStack);  // Uses both
        elements.remove(topOfStack);  // Uses both
        return element;
    }
}
// Every method uses the same instance variables - high cohesion
```

**When cohesion breaks down:** If a subset of methods only uses a subset of variables, extract those methods and variables into a separate class.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-cohesion](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-cohesion.md).
