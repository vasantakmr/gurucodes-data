---
title: "Data Types"
---

Python supports various **data types** that specify the kind of value a variable can hold. The most commonly used data types in Python are:

### 1. **Numeric Types**
   - **int**: Integer numbers (e.g., `10`, `-5`, `1000`)
   - **float**: Floating-point numbers (e.g., `3.14`, `-0.001`, `2.0`)
   - **complex**: Complex numbers (e.g., `3 + 4j`, where `j` is the imaginary unit)

### Example:
```python
age = 30        # int
price = 19.99   # float
complex_num = 2 + 3j  # complex
```

### 2. **String (str)**
A string is a sequence of characters enclosed in single (`'`) or double (`"`) quotes. Strings in Python are immutable, meaning their content cannot be changed after creation.

### Example:
```python
name = "Nihar"
greeting = 'Hello, World!'
```

Strings support various operations like concatenation, slicing, and formatting.

### Example (Concatenation):
```python
first_name = "Dodagatta"
last_name = "Nihar"
full_name = first_name + " " + last_name
print(full_name)
```

**Output:**
```
Dodagatta Nihar
```

### Example (Slicing):
```python
text = "Python"
print(text[0])   # Output: 'P'
print(text[1:4]) # Output: 'yth'
```

---

### 3. **Boolean (bool)**
Booleans represent two values: **True** or **False**. They are used for logical operations and conditions.

### Example:
```python
is_adult = True
is_student = False
```

Booleans can be used in conditional expressions.

### Example:
```python
age = 20
is_adult = age >= 18
print(is_adult)  # Output: True
```

---

### 4. **List**
A **list** is an ordered, mutable collection of items. Lists can store elements of different data types and are defined using square brackets (`[]`).

### Example:
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.14, True]
```

Lists can be indexed and sliced, just like strings.

### Example:
```python
print(fruits[0])    # Output: 'apple'
print(numbers[1:3]) # Output: [2, 3]
```

---

### 5. **Tuple**
A **tuple** is an ordered, immutable collection of items. Tuples are defined using parentheses (`()`).

### Example:
```python
person = ("Praveen", 30, "Engineer")
coordinates = (10.5, 20.3)
```

Once created, the elements of a tuple cannot be modified.

### Example:
```python
person = ("Vasanta", 25)
# person[0] = "Kumar"  # This will raise an error because tuples are immutable.
```

---

### 6. **Dictionary (dict)**
A **dictionary** is an unordered, mutable collection of key-value pairs. Dictionaries are defined using curly braces (`{}`).

### Example:
```python
student = {
    "name": "Dodagatta Nihar",
    "age": 25,
    "major": "Computer Science"
}
```

In dictionaries, each key must be unique, and the values can be accessed by their corresponding keys.

### Example:
```python
print(student["name"])  # Output: Dodagatta Nihar
print(student["age"])   # Output: 25
```

---

### 7. **Set**
A **set** is an unordered, mutable collection of unique items. Sets are defined using curly braces (`{}`).

### Example:
```python
my_set = {1, 2, 3, 4, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5} (duplicate 4 is removed)
```

Sets do not allow duplicate values and are mainly used for membership tests and removing duplicates.

---