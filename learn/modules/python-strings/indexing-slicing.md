---
title: "String Indexing and Slicing"
---

### 1. **Indexing**
Each character in a string is assigned an index. You can access individual characters using square brackets `[]`.

```python
name = "Dodagatta Nihar"
print(name[0])  # First character
print(name[-1])  # Last character
```

**Output:**
```
D
r
```

- `name[0]`: Accesses the first character, `D`.
- `name[-1]`: Accesses the last character, `r`.

### 2. **Slicing**
Slicing allows you to extract a substring by specifying a range of indices.

```python
greeting = "Hello, Harsha!"
print(greeting[0:5])  # First 5 characters
print(greeting[7:])   # Characters from index 7 to the end
```

**Output:**
```
Hello
Harsha!
```

- `greeting[0:5]`: Extracts characters from index 0 to 4 (`Hello`).
- `greeting[7:]`: Extracts all characters starting from index 7 (`Harsha!`).

---
