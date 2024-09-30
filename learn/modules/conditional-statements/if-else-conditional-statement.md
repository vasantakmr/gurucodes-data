---
title: "if - else Conditional Statement"
---

## `else` Statement

The `else` statement is executed if none of the preceding `if` or `elif` conditions are `True`.

### Syntax:
```python
if condition1:
    # code block if condition1 is True
elif condition2:
    # code block if condition2 is True
else:
    # code block if all conditions are False
```

### Example:
```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
```

**Output:**
```
x is 5 or less
```

### Real-world Example:
Vasanta Kumar is deciding whether he should study or relax:
```python
hours_studied = 5
if hours_studied > 6:
    print("Vasanta Kumar can relax now.")
else:
    print("Vasanta Kumar should continue studying.")
```

**Output:**
```
Vasanta Kumar should continue studying.
```

---