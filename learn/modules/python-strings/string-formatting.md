---
title: "String Formatting"
---

Python provides multiple ways to format strings, making it easier to insert values into strings dynamically.

### 1. **f-Strings (Formatted String Literals)**
F-strings allow you to embed expressions inside string literals, prefixed by `f`.

```python
name = "Harsha"
age = 25
print(f"{name} is {age} years old.")
```

**Output:**
```
Harsha is 25 years old.
```

### 2. **`str.format()`**
The `format()` method allows for more flexible string formatting by using placeholders `{}`.

```python
name = "Praveen"
occupation = "Software Developer"
print("{} is a {}.".format(name, occupation))
```

**Output:**
```
Praveen is a Software Developer.
```

### 3. **Percentage (`%`) Formatting**
An older way of formatting strings, using `%` operators.

```python
name = "Vasanta Kumar"
age = 30
print("%s is %d years old." % (name, age))
```

**Output:**
```
Vasanta Kumar is 30 years old.
```

---