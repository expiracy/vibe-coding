---
title: Avoid Hybrid Data-Object Structures
impact: MEDIUM-HIGH
impactDescription: prevents worst-of-both-worlds maintenance burden
tags: obj, hybrid, structure, design
---

## Avoid Hybrid Data-Object Structures

Hybrids are half object, half data structure. They have functions that do significant things, AND they have public variables or accessors that expose internal structure. Avoid creating these monstrosities.

**Incorrect (hybrid structure):**

```java
// Half object, half data structure
public class Employee {
    // Public data like a data structure
    public String name;
    public double salary;
    public List<String> skills;

    // Behavior like an object
    public void promote() {
        this.salary *= 1.1;
        notifyHR();
    }

    public void addSkill(String skill) {
        this.skills.add(skill);
        updateTrainingRecord();
    }
}

// Client code can bypass behavior
employee.salary = employee.salary * 1.5;  // Skips notifyHR()
employee.skills.clear();  // Skips updateTrainingRecord()
```

**Correct (choose one approach):**

```java
// Pure object - hide data, expose behavior
public class Employee {
    private String name;
    private Money salary;
    private SkillSet skills;

    public void promote(PromotionDetails details) {
        this.salary = salary.increase(details.getRaisePercentage());
        notifyHR(details);
    }

    public void addSkill(Skill skill) {
        this.skills.add(skill);
        updateTrainingRecord(skill);
    }

    public EmployeeReport getReport() {
        return new EmployeeReport(name, salary.getAmount(), skills.list());
    }
}

// OR pure data structure - no behavior, expose data
public final class EmployeeData {
    private final String name;
    private final double salary;
    private final List<String> skills;

    public EmployeeData(String name, double salary, List<String> skills) {
        this.name = name;
        this.salary = salary;
        this.skills = List.copyOf(skills);
    }

    public String getName() { return name; }
    public double getSalary() { return salary; }
    public List<String> getSkills() { return skills; }
}
```

Hybrids make it hard to add new functions AND hard to add new data structures.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-avoid-hybrids](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-avoid-hybrids.md).
