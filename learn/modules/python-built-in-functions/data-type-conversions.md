---
title: "Data Type Conversions"
---

### `int()`
Converts a value to an integer.

**Syntax:**
```python
int(value[, base])
```

**Example:**
```python
print(int("123"))    # Output: 123
print(int("1010", 2))  # Output: 10
```

### `float()`
Converts a value to a floating-point number.

**Syntax:**
```python
float(value)
```

**Example:**
```python
print(float("3.14"))  # Output: 3.14
```

### `str()`
Converts a value to a string.

**Syntax:**
```python
str(value)
```

**Example:**
```python
print(str(100))      # Output: "100"
```

### `list()`
Converts a value to a list.

**Syntax:**
```python
list(iterable)
```

**Example:**
```python
print(list("hello"))  # Output: ['h', 'e', 'l', 'l', 'o']
```

### `tuple()`
Converts a value to a tuple.

**Syntax:**
```python
tuple(iterable)
```

**Example:**
```python
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)
```

### `set()`
Converts a value to a set.

**Syntax:**
```python
set(iterable)
```

**Example:**
```python
print(set("hello"))  # Output: {'h', 'e', 'l', 'o'}
```

### `dict()`
Creates a dictionary from a sequence of key-value pairs.

**Syntax:**
```python
dict(iterable)
```

**Example:**
```python
print(dict([("name", "Alice"), ("age", 30)]))  # Output: {'name': 'Alice', 'age': 30}
```

---