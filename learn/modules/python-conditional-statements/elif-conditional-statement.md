---
title: "elif Conditional Statement"
---

## `elif` Statement

The `elif` (short for "else if") statement allows you to check multiple conditions. It is evaluated if the preceding `if` condition is `False`.

### Syntax:
```python
if condition1:
    # code block if condition1 is True
elif condition2:
    # code block if condition2 is True
```

### Example:
```python
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
```

**Output:**
```
x is greater than 5 but less than or equal to 15
```

### Real-world Example:
Harsha checks the weather to decide his plan:
```python
temperature = 28
if temperature > 35:
    print("Harsha will stay indoors.")
elif temperature > 25:
    print("Harsha will go for a walk.")
```

**Output:**
```
Harsha will go for a walk.
```

---