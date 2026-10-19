---
title: "Make Arguments Express a Clear Contract"
impact: HIGH
impactDescription: "Give each argument a clear role and avoid redundant or unrelated inputs"
tags: clean-code, func
---

## Make Arguments Express a Clear Contract

Give each argument a clear role and avoid redundant or unrelated inputs. Several values that form one real domain concept may belong together; an arbitrary argument bag does not improve the interface.

Replace an ambiguous mode flag with a clearer operation or meaningful option when it improves the contract. Do not impose a numerical argument limit or change a public interface without considering its callers.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
