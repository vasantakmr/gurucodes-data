---
title: "Nested Conditional Statements"
---

**Nested conditional statements** are conditions placed within another condition. This means an `if`, `elif`, or `else` block can contain another conditional statement inside it.

### Syntax:
```python
if condition1:
    if condition2:
        # code block if both condition1 and condition2 are True
    else:
        # code block if condition1 is True but condition2 is False
else:
    # code block if condition1 is False
```

### Example:
```python
x = 10
y = 5

if x > 5:
    if y < 10:
        print(f"x is greater than 5 and y is less than 10")
    else:
        print(f"x is greater than 5 but y is not less than 10")
else:
    print(f"x is not greater than 5")
```

**Output:**
```
x is greater than 5 and y is less than 10
```

### Real-world Example:
Praveen checks both the time and the weather to decide his plan:
```python
time = 18
weather = "sunny"

if time < 20:
    if weather == "sunny":
        print("Praveen will go for a jog.")
    else:
        print("Praveen will stay indoors.")
else:
    print("Praveen will go to bed early.")
```

**Output:**
```
Praveen will go for a jog.
```

---
