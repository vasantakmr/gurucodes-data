---
title: "String Methods"
---

Python provides a variety of methods for string manipulation. Some of the most commonly used ones are:

### 1. **`upper()` and `lower()`**
Converts a string to uppercase or lowercase.

```python
name = "Dodagatta Nihar"
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
```

**Output:**
```
DODAGATTA NIHAR
dodagatta nihar
```

### 2. **`strip()`**
Removes leading and trailing whitespace (or any specified characters).

```python
message = "   Hello, Vasanta!   "
clean_message = message.strip()
print(clean_message)
```

**Output:**
```
Hello, Vasanta!
```

The `strip()` method removes the extra spaces from both ends of the string.

### 3. **`replace()`**
Replaces all occurrences of a substring with another substring.

```python
greeting = "Hello, Harsha!"
new_greeting = greeting.replace("Harsha", "Praveen")
print(new_greeting)
```

**Output:**
```
Hello, Praveen!
```

The `replace()` method replaces `"Harsha"` with `"Praveen"` in the `greeting` string.

### 4. **`split()`**
Splits a string into a list of substrings, based on a specified delimiter.

```python
full_name = "Vasanta Kumar"
name_list = full_name.split()
print(name_list)
```

**Output:**
```
['Vasanta', 'Kumar']
```

The `split()` method breaks the string into two substrings at the space character.

### 5. **`join()`**
Joins the elements of a list into a single string, using a specified separator.

```python
name_list = ["Dodagatta", "Nihar"]
full_name = " ".join(name_list)
print(full_name)
```

**Output:**
```
Dodagatta Nihar
```

The `join()` method joins the elements of `name_list` into a single string, with a space between them.

---