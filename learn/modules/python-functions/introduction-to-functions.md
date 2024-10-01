---
title: "Introduction to Functions"
---

## Introduction

Functions are reusable blocks of code designed to perform specific tasks. They allow you to encapsulate code into a single unit, making it easier to manage, debug, and reuse. Functions help to break down complex problems into smaller, manageable pieces.

---

## Defining a Function

Functions are defined using the `def` keyword followed by the function name and parentheses. The code block within the function is indented.

### Syntax:
```python
def function_name(parameters):
    # Function body
    # Return value (optional)
```

### Example:
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Dodagatta Nihar")
```

**Output:**
```
Hello, Dodagatta Nihar!
```

### Real-world Example:
Harsha defines a function to calculate the area of a rectangle:
```python
def calculate_area(length, width):
    area = length * width
    return area

area = calculate_area(5, 10)
print(f"Area: {area}")
```

**Output:**
```
Area: 50
```

---

## Function Parameters

Functions can accept parameters to work with. Parameters can be positional, keyword, default, or variable-length.

### Positional Parameters

These are the most common type of parameters, where values are passed based on their position.

### Example:
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)
```

**Output:**
```
7
```

### Keyword Parameters

Parameters can be specified by name when calling the function.

### Example:
```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(name="Vasanta Kumar", age=30)
```

**Output:**
```
My name is Vasanta Kumar and I am 30 years old.
```

### Default Parameters

You can provide default values for parameters. If no argument is passed, the default value is used.

### Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  # Uses default value
greet("Praveen")  # Uses provided value
```

**Output:**
```
Hello, Guest!
Hello, Praveen!
```

### Variable-Length Parameters

Functions can accept a variable number of arguments using `*args` for positional arguments and `**kwargs` for keyword arguments.

### Example:
```python
def summarize_data(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

summarize_data(1, 2, 3, name="Alice", age=25)
```

**Output:**
```
Positional arguments: (1, 2, 3)
Keyword arguments: {'name': 'Alice', 'age': 25}
```
