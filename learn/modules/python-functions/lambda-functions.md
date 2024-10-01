---
title: "Lambda Functions"
---

Lambda functions are small anonymous functions defined using the `lambda` keyword. They can have any number of parameters but only one expression.

### Syntax:
```python
lambda arguments: expression
```

### Example:
```python
add = lambda x, y: x + y
print(add(5, 3))
```

**Output:**
```
8
```

### Real-world Example:
Praveen uses a lambda function to sort a list of tuples by the second element:
```python
data = [(1, 3), (2, 2), (3, 1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
```

**Output:**
```
[(3, 1), (2, 2), (1, 3)]
```

---