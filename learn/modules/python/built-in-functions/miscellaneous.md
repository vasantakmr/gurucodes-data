---
title: "Miscellaneous"
---

## Type Checking

### `type()`
Returns the type of an object.

**Syntax:**
```python
type(object)
```

**Example:**
```python
print(type("hello"))  # Output: <class 'str'>
print(type(123))  # Output: <class 'int'>
```

### `isinstance()`
Checks if an object is an instance or subclass of a class or a tuple of classes.

**Syntax:**
```python
isinstance(object, classinfo)
```

**Example:**
```python
print(isinstance("hello", str))  # Output: True
print(isinstance(123, (int, float)))  # Output: True
```

---

## Input and Output

### `print()`
Prints objects to the console.

**Syntax:**
```python
print(*objects[, sep=' ', end='\n', file=sys.stdout, flush=False])
```

**Example:**
```python
print("Hello", "world")  # Output: Hello world
```

### `input()`
Reads a line from input, converts it to a string, and returns it.

**Syntax:**
```python
input([prompt])
```

**Example:**
```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

---

## Utility Functions

### `id()`
Returns the identity (unique identifier) of an object.

**Syntax:**
```python
id(object)
```

**Example:**
```python
x = 10
print(id(x))  # Output: A unique identifier for x
```

### `callable()`
Checks if an object appears to be callable (i.e., if it can be called as a function).

**Syntax:**
```python
callable(object)
```

**Example:**
```python
print(callable(print))  # Output: True
print(callable(123))  # Output: False
```

### `eval()`
Evaluates a given expression from a string-based input.

**Syntax:**
```python
eval(expression[, globals[, locals]])
```

**Example:**
```python
result = eval("2 + 3")
print(result)  # Output: 5
```

### `exec()`
Executes a dynamically created Python code which can be a single statement, multiple statements, or a block.

**Syntax:**
```python
exec(object[, globals[, locals]])
```

**Example:**
```python
exec("for i in range(3): print(i)")
```

**Output:**
```
0
1
2
```

### `format()`
Formats a value according to a format specification.

**Syntax:**
```python
format(value[, format_spec])
```

**Example:**
```python
print(format(1234.567, ".2f"))  # Output: 1234.57
```

---
