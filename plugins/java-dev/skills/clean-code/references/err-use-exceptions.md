---
title: Separate Error Handling from Happy Path
impact: HIGH
impactDescription: makes success and failure contracts understandable
tags: err, exceptions, error-handling, separation, result-types
---

## Separate Error Handling from Happy Path

Error handling is important, but when it obscures logic, it's wrong. The core insight is separation: keep the happy path visible and error handling consolidated, regardless of which mechanism your language uses.

**Incorrect (error handling obscures business logic):**

```java
if (deletePage(page) == E_OK) {
    if (registry.deleteReference(page.name) == E_OK) {
        if (configKeys.deleteKey(page.name.makeKey()) == E_OK) {
            logger.log("page deleted");
        } else {
            logger.log("configKey not deleted");
        }
    } else {
        logger.log("deleteReference from registry failed");
    }
} else {
    logger.log("delete failed");
    return E_ERROR;
}
```

**Correct (successful work separated from reporting):**

```java
public void delete(Page page) {
    try {
        deletePageAndAllReferences(page);
    } catch (PageDeletionException e) {
        logger.log(e.getMessage());
    }
}

private void deletePageAndAllReferences(Page page) throws PageDeletionException {
    deletePage(page);
    registry.deleteReference(page.name);
    configKeys.deleteKey(page.name.makeKey());
}
```

The principle is separation, not a mandate to change the project's error
mechanism. These examples illustrate an exception-enabled contract. Preserve
the existing failure and side-effect contract when adapting them. Expected
absence and operational failure can require different results.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) and [Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-use-exceptions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-use-exceptions.md).
