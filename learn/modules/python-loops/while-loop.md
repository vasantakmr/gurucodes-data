---
title: "While Loop"
---

The `while` loop continues to execute as long as a condition is `True`. It’s useful when you don’t know beforehand how many times you need to loop.

### Syntax:
```python
while condition:
    # code block
```

### Example:
```python
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1
```

**Output:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
```

### Real-world Example:
Harsha is counting down the days until his vacation:
```python
days_left = 5
while days_left > 0:
    print(f"{days_left} days until Harsha's vacation")
    days_left -= 1
```

**Output:**
```
5 days until Harsha's vacation
4 days until Harsha's vacation
3 days until Harsha's vacation
2 days until Harsha's vacation
1 day until Harsha's vacation
```

---
