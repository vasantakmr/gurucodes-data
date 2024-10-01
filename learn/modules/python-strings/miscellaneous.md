---
title: "Miscellaneous"
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

## Few more examples 

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
