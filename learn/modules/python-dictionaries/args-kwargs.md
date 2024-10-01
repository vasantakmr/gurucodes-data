---
title: "*args and **kwargs in Python"
---

## Introduction

In Python, `*args` and `**kwargs` are used to pass a variable number of arguments to functions. They allow you to handle function arguments more flexibly, making your functions more versatile and easier to manage.

- **`*args`**: Used to pass a variable number of non-keyword arguments (positional arguments) to a function.
- **`**kwargs`**: Used to pass a variable number of keyword arguments (named arguments) to a function.

---

## 1. Using `*args`

### Definition

`*args` allows a function to accept any number of positional arguments. The arguments passed through `*args` are captured as a tuple.

### Syntax:
```python
def function_name(*args):
    # Function body
```

### Example:
```python
def print_fruits(*args):
    for fruit in args:
        print(fruit)

print_fruits("apple", "banana", "cherry")
```

**Output:**
```
apple
banana
cherry
```

### Real-world Example:
Dodagatta Nihar uses `*args` to handle multiple scores in a grading function:
```python
def calculate_average(*scores):
    return sum(scores) / len(scores)

average_score = calculate_average(85, 90, 78, 92)
print(f"Average Score: {average_score}")
```

**Output:**
```
Average Score: 86.25
```

---

## 2. Using `**kwargs`

### Definition

`**kwargs` allows a function to accept any number of keyword arguments. The arguments passed through `**kwargs` are captured as a dictionary.

### Syntax:
```python
def function_name(**kwargs):
    # Function body
```

### Example:
```python
def print_person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_details(name="John", age=30, city="New York")
```

**Output:**
```
name: John
age: 30
city: New York
```

### Real-world Example:
Harsha uses `**kwargs` to create a profile with various details:
```python
def create_profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

create_profile(name="Harsha", profession="Engineer", location="Bangalore")
```

**Output:**
```
name: Harsha
profession: Engineer
location: Bangalore
```

---

## 3. Combining `*args` and `**kwargs`

You can use `*args` and `**kwargs` together in a function to handle both positional and keyword arguments. `*args` must appear before `**kwargs` in the function definition.

### Syntax:
```python
def function_name(*args, **kwargs):
    # Function body
```

### Example:
```python
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info("apple", "banana", fruit_count=2, location="fruit basket")
```

**Output:**
```
Positional arguments: ('apple', 'banana')
Keyword arguments: {'fruit_count': 2, 'location': 'fruit basket'}
```

### Real-world Example:
Vasanta Kumar uses both `*args` and `**kwargs` to log user activities:
```python
def log_activity(user_id, *activities, **metadata):
    print(f"User ID: {user_id}")
    print("Activities:", activities)
    print("Metadata:", metadata)

log_activity(101, "login", "view_profile", "logout", timestamp="2024-09-17", session_id="XYZ123")
```

**Output:**
```
User ID: 101
Activities: ('login', 'view_profile', 'logout')
Metadata: {'timestamp': '2024-09-17', 'session_id': 'XYZ123'}
```

---

## Few more examples

### Example 1: Function with `*args`
```python
def concat_strings(*args):
    return " ".join(args)

result = concat_strings("Hello", "world", "from", "Python")
print(result)
```

**Output:**
```
Hello world from Python
```

### Example 2: Function with `**kwargs`
```python
def summarize_data(**kwargs):
    summary = ""
    for key, value in kwargs.items():
        summary += f"{key}: {value}\n"
    return summary

summary = summarize_data(name="Alice", age=28, city="Paris")
print(summary)
```

**Output:**
```
name: Alice
age: 28
city: Paris
```

### Example 3: Function with `*args` and `**kwargs`
```python
def report_data(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

report_data(1, 2, 3, name="Bob", status="active")
```

**Output:**
```
Arguments: (1, 2, 3)
Keyword arguments: {'name': 'Bob', 'status': 'active'}
```

---

