---
title: "Control Flow Statements"
---

## `break` Statement

The `break` statement is used to terminate a loop before it has iterated through all items or conditions.

### Example:
```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Real-world Example:
Vasanta Kumar is searching for a specific book in a list, and he stops as soon as he finds it:
```python
books = ["Book A", "Book B", "Book C", "Book D"]
for book in books:
    if book == "Book C":
        print(f"Vasanta Kumar found {book}")
        break
```

**Output:**
```
Vasanta Kumar found Book C
```

---

## `continue` Statement

The `continue` statement skips the current iteration and moves on to the next iteration of the loop.

### Example:
```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

**Output:**
```
0
1
2
4
```

### Real-world Example:
Praveen skips an item if it’s already completed:
```python
tasks = ["Task 1", "Task 2", "Task 3"]
completed_task = "Task 2"

for task in tasks:
    if task == completed_task:
        continue
    print(f"Praveen needs to do: {task}")
```

**Output:**
```
Praveen needs to do: Task 1
Praveen needs to do: Task 3
```

---

## `pass` Statement

The `pass` statement does nothing and is used as a placeholder in situations where code is syntactically required but not needed at the moment.

### Example:
```python
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
```

**Output:**
```
0
1
2
4
```

### Real-world Example:
Dodagatta Nihar is planning to update a task list later:
```python
tasks = ["Task A", "Task B", "Task C"]
for task in tasks:
    if task == "Task B":
        pass  # This will be updated later
    else:
        print(f"Dodagatta Nihar needs to: {task}")
```

**Output:**
```
Dodagatta Nihar needs to: Task A
Dodagatta Nihar needs to: Task C
```

---