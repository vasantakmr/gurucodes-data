---
title: "String Operations"
---

## String Operations

### 1. **String Concatenation**
You can concatenate (join) two or more strings using the `+` operator.

```python
first_name = "Vasanta"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)
```

**Output:**
```
Vasanta Kumar
```

Here, the `+` operator concatenates `first_name` and `last_name` with a space in between to form `full_name`.

### 2. **String Repetition**
The `*` operator allows you to repeat a string multiple times.

```python
name = "Praveen"
repeat_name = name * 3
print(repeat_name)
```

**Output:**
```
PraveenPraveenPraveen
```

The string `Praveen` is repeated 3 times.

---

## String Indexing and Slicing

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

## String Methods

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

## String Formatting

Python provides multiple ways to format strings, making it easier to insert values into strings dynamically.

### 1. **f-Strings (Formatted String Literals)**
F-strings allow you to embed expressions inside string literals, prefixed by `f`.

```python
name = "Harsha"
age = 25
print(f"{name} is {age} years old.")
```

**Output:**
```
Harsha is 25 years old.
```

### 2. **`str.format()`**
The `format()` method allows for more flexible string formatting by using placeholders `{}`.

```python
name = "Praveen"
occupation = "Software Developer"
print("{} is a {}.".format(name, occupation))
```

**Output:**
```
Praveen is a Software Developer.
```

### 3. **Percentage (`%`) Formatting**
An older way of formatting strings, using `%` operators.

```python
name = "Vasanta Kumar"
age = 30
print("%s is %d years old." % (name, age))
```

**Output:**
```
Vasanta Kumar is 30 years old.
```

---

## Multiline Strings

To create a multiline string, use triple quotes (`'''` or `"""`).

```python
address = """Dodagatta Nihar
123 Main Street
City, State, 12345"""
print(address)
```

**Output:**
```
Dodagatta Nihar
123 Main Street
City, State, 12345
```

Multiline strings are useful when dealing with long texts or paragraphs.

---

## Example Code and Output

### Example 1: String Manipulation with Names
```python
first_name = "Praveen"
last_name = "Kumar"
full_name = first_name + " " + last_name

greeting = f"Hello, {full_name}!"
print(greeting.upper())
```

**Output:**
```
HELLO, PRAVEEN KUMAR!
```

### Example 2: Using String Methods
```python
message = "   Hello, Dodagatta Nihar!   "
cleaned_message = message.strip().replace("Dodagatta Nihar", "Harsha")
print(cleaned_message)
```

**Output:**
```
Hello, Harsha!
```

### Example 3: String Formatting
```python
name = "Vasanta Kumar"
age = 35
formatted_string = f"{name} is {age} years old."
print(formatted_string)
```

**Output:**
```
Vasanta Kumar is 35 years old.
```

---
