---
title: "Miscellaneous"
---

## Looping through a String

A `for` loop can also be used to iterate through the characters of a string.

### Example:
```python
name = "Dodagatta"
for letter in name:
    print(letter)
```

**Output:**
```
D
o
d
a
g
a
t
t
a
```

### Real-world Example:
Harsha spells out his name letter by letter:
```python
name = "Harsha"
for letter in name:
    print(f"Letter: {letter}")
```

**Output:**
```
Letter: H
Letter: a
Letter: r
Letter: s
Letter: h
Letter: a
```

---

## Few more examples

### Example 1: Calculating the Sum of Numbers Using `while` Loop
```python
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"Sum of first {n} numbers is {sum}")
```

**Output:**
```
Sum of first 5 numbers is 15
```

### Example 2: Checking Even Numbers Using `for` Loop
```python
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
```

**Output:**
```
2 is even
4 is even
6 is even
8 is even
10 is even
```

### Example 3: Nested Loop Example - Multiplication Table
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
```

**Output:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
2 x 1 = 2
2 x 2 = 4
...
```

---

