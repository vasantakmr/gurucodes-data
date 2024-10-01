---
title: "Introduction to Type Conversion"
---

**Type conversion** in Python refers to the process of converting one data type into another. Python provides several built-in functions to perform explicit type conversion (also known as **type casting**). In some cases, Python automatically converts types, which is known as **implicit type conversion**.

There are two types of type conversion:
1. **Implicit Type Conversion**: Automatically performed by Python.
2. **Explicit Type Conversion**: Performed by the programmer using built-in functions.

---

## 1. Implicit Type Conversion

Python automatically converts one data type to another whenever necessary, without any user intervention. This usually happens when performing operations between different data types.

### Example: Implicit Conversion
```python
age = 25      # int
height = 5.9  # float

# Python implicitly converts 'age' to float before addition
combined = age + height
print(combined)
print(type(combined))
```

**Output:**
```
30.9
<class 'float'>
```

In this example:
- `age` is an integer, and `height` is a float.
- When they are added, Python converts `age` to a float implicitly, so the result is a float.

---

## 2. Explicit Type Conversion

Explicit type conversion is performed manually by using Python's built-in functions. The most commonly used functions for type conversion are:
- `int()`: Converts a value to an integer.
- `float()`: Converts a value to a floating-point number.
- `str()`: Converts a value to a string.
- `list()`: Converts a value to a list.
- `tuple()`: Converts a value to a tuple.
- `dict()`: Converts a value to a dictionary.

### Example: Integer to String Conversion
```python
age = 30
name = "Dodagatta Nihar"

# Explicitly convert 'age' to a string to concatenate with 'name'
info = name + " is " + str(age) + " years old."
print(info)
```

**Output:**
```
Dodagatta Nihar is 30 years old.
```

In this example, `age` is an integer, but we explicitly convert it to a string using the `str()` function to concatenate it with the string `name`.

---