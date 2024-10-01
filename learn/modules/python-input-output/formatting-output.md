---
title: "Formatting Output"
---

Python also allows more complex formatting of output using **f-strings** (formatted string literals), `str.format()`, or the older `%` operator.

### Example 1: Using f-Strings (Python 3.6+)
```python
name = "Harsha"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

**Output:**
```
My name is Harsha and I am 30 years old.
```

F-strings allow you to embed expressions inside string literals by prefixing the string with `f`.

### Example 2: Using `str.format()`
```python
name = "Harsha"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
```

**Output:**
```
My name is Harsha and I am 30 years old.
```

`str.format()` is an older method for formatting strings by substituting placeholders (`{}`) with variable values.

### Example 3: Using the `%` Operator
```python
name = "Harsha"
age = 30
print("My name is %s and I am %d years old." % (name, age))
```

**Output:**
```
My name is Harsha and I am 30 years old.
```

This method is based on C-style string formatting, where `%s` is used for strings, `%d` for integers, etc. This approach is considered outdated compared to f-strings and `str.format()`.

---