---
title: "variables"
---

A **variable** in Python is a name that refers to a memory location where data is stored. Variables allow you to store, modify, and access data during the execution of a program. Unlike some other programming languages, Python variables are dynamically typed, meaning you do not need to explicitly declare their data type.

### Syntax:
```python
variable_name = value
```

- **variable_name**: A valid identifier that follows Python's naming conventions.
- **value**: The data assigned to the variable.

### Example:
```python
name = "Nihar"
age = 25
height = 6.0
is_student = True
```

In this example:
- `name` is assigned a string (`"Nihar"`).
- `age` is assigned an integer (`25`).
- `height` is assigned a float (`6.0`).
- `is_student` is assigned a boolean value (`True`).

---

## Variable Naming Rules

1. **Case-sensitive**: Variable names are case-sensitive. `age` and `Age` are two different variables.
2. **Must start with a letter or underscore**: Variables can start with a letter (a-z, A-Z) or an underscore (`_`), but not a number.
3. **Cannot use reserved keywords**: Python keywords like `class`, `if`, `while`, etc., cannot be used as variable names.
4. **No spaces allowed**: Use underscores to separate words (`my_variable`).

### Example:
```python
first_name = "Nihar"  # Valid
1st_name = "Nihar"    # Invalid (cannot start with a number)
```

---