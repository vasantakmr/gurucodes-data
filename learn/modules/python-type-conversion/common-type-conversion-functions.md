---
title: "Common Type Conversion Functions"
---

### 1. **`int()`**: Converts a value to an integer.
- Works with floats (truncates the decimal part) and strings containing numeric values.
  
```python
num_float = 7.89
num_str = "50"

print(int(num_float))  # Output: 7
print(int(num_str))    # Output: 50
```

### 2. **`float()`**: Converts a value to a float.
- Works with integers and numeric strings.

```python
num_int = 10
num_str = "30.5"

print(float(num_int))  # Output: 10.0
print(float(num_str))  # Output: 30.5
```

### 3. **`str()`**: Converts a value to a string.
- Works with integers, floats, and other data types.

```python
age = 28
height = 6.1

print(str(age))    # Output: '28'
print(str(height)) # Output: '6.1'
```

### 4. **`list()`**: Converts a value to a list.
- Converts strings, tuples, or other iterable objects into lists.

```python
tuple_example = ("Harsha", "Praveen")
list_example = list(tuple_example)
print(list_example)  # Output: ['Harsha', 'Praveen']
```

### 5. **`tuple()`**: Converts a value to a tuple.
- Converts lists or other iterable objects into tuples.

```python
list_example = ["Vasanta", "Kumar"]
tuple_example = tuple(list_example)
print(tuple_example)  # Output: ('Vasanta', 'Kumar')
```

### 6. **`dict()`**: Converts a list of key-value pairs into a dictionary.
- The list must contain tuples or lists of key-value pairs.

```python
list_of_pairs = [("name", "Dodagatta Nihar"), ("age", 30)]
dict_example = dict(list_of_pairs)
print(dict_example)  # Output: {'name': 'Dodagatta Nihar', 'age': 30}
```

---

## Example: Converting User Input

User input from the `input()` function is always a string, so we often need to convert it to the appropriate type.

```python
# Asking Harsha for his age
age_input = input("Enter your age, Harsha: ")  # User input is string by default

# Convert the input to an integer
age = int(age_input)
print(f"Harsha is {age} years old.")
```

**Output:**
```
Enter your age, Harsha: 26
Harsha is 26 years old.
```

Here, we take Harsha's age as input (which is a string) and convert it to an integer using `int()` before printing it.

---

## Handling Type Conversion Errors

When trying to convert a value to an incompatible type, Python raises a **ValueError**.

### Example: Invalid String to Integer Conversion
```python
invalid_str = "Dodagatta Nihar"

try:
    num = int(invalid_str)
except ValueError:
    print(f"Cannot convert '{invalid_str}' to an integer.")
```

**Output:**
```
Cannot convert 'Dodagatta Nihar' to an integer.
```

---

## Few more examples

### Example 1: Converting Between Data Types
```python
age = "30"  # String
height = 5.9  # Float
name = "Praveen"

# Explicit conversion
age_int = int(age)  # Convert string to int
height_str = str(height)  # Convert float to string

print(f"{name} is {age_int} years old and {height_str} feet tall.")
```

**Output:**
```
Praveen is 30 years old and 5.9 feet tall.
```

### Example 2: List to Tuple Conversion
```python
friends_list = ["Dodagatta Nihar", "Harsha", "Vasanta Kumar"]
friends_tuple = tuple(friends_list)
print(friends_tuple)
```

**Output:**
```
('Dodagatta Nihar', 'Harsha', 'Vasanta Kumar')
```

### Example 3: String to Float Conversion
```python
salary_str = "50000.75"
salary = float(salary_str)  # Convert string to float

print(f"Vasanta Kumar's salary is {salary}.")
```

**Output:**
```
Vasanta Kumar's salary is 50000.75.
```

---
