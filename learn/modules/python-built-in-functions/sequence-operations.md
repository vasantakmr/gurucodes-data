---
title: "Sequence Operations"
---

## Sequence Operations

### `len()`
Returns the length of an object.

**Syntax:**
```python
len(object)
```

**Example:**
```python
print(len("hello"))  # Output: 5
print(len([1, 2, 3]))  # Output: 3
```

### `max()`
Returns the largest item in an iterable or the largest of two or more arguments.

**Syntax:**
```python
max(iterable[, key])
max(arg1, arg2[, ...[, key]])
```

**Example:**
```python
print(max([1, 2, 3]))  # Output: 3
print(max(1, 2, 3))  # Output: 3
```

### `min()`
Returns the smallest item in an iterable or the smallest of two or more arguments.

**Syntax:**
```python
min(iterable[, key])
min(arg1, arg2[, ...[, key]])
```

**Example:**
```python
print(min([1, 2, 3]))  # Output: 1
print(min(1, 2, 3))  # Output: 1
```

### `sorted()`
Returns a new sorted list from the elements of an iterable.

**Syntax:**
```python
sorted(iterable[, key][, reverse])
```

**Example:**
```python
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]
```

### `reversed()`
Returns an iterator that accesses the given sequence in the reverse order.

**Syntax:**
```python
reversed(sequence)
```

**Example:**
```python
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]
```

---
