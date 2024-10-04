---
title: "Reading from Files"
---

Reading data from files is a common operation, and Python provides several methods to facilitate this process.

**Key Methods:**

- **`read(size=-1)` Method:**

  - Reads up to `size` bytes. If `size` is omitted or negative, reads the entire file.

  **Example:**

  ```python
  with open('example.txt', 'r') as file:
      content = file.read()
  ```

- **`readline()` Method:**

  - Reads the next line from the file.
  - Useful for reading files line by line.

  **Example:**

  ```python
  with open('example.txt', 'r') as file:
      line = file.readline()
      while line:
          print(line, end='')
          line = file.readline()
  ```

- **`readlines()` Method:**

  - Reads all lines and returns a list where each element is a line.

  **Example:**

  ```python
  with open('example.txt', 'r') as file:
      lines = file.readlines()
      for line in lines:
          print(line, end='')
  ```

- **Iterating Over File Objects:**

  - Files are iterable in Python, allowing you to loop through each line.

  **Example:**

  ```python
  with open('example.txt', 'r') as file:
      for line in file:
          print(line, end='')
  ```

- **Handling Large Files:**
  - Use generators or iterate line by line to avoid loading the entire file into memory.

**Advanced Reading Techniques:**

- **Reading Binary Files:**

  - Use binary modes (`'rb'`) and handle data as bytes.

  **Example:**

  ```python
  with open('image.png', 'rb') as file:
      data = file.read()
  ```

- **Specifying Encoding:**

  - When dealing with text files, specify the encoding to correctly interpret characters.

  **Example:**

  ```python
  with open('example.txt', 'r', encoding='utf-8') as file:
      content = file.read()
  ```

**Error Handling:**

- Use try-except blocks to catch and handle `IOError`, `FileNotFoundError`, etc.

**Example:**

```python
try:
    with open('example.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")
```

---
