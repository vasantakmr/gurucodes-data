---
title: "Fundamental Bitwise Operators"
---

Bitwise operators perform operations on integers by manipulating their binary representations. Each integer is represented as a sequence of bits (0s and 1s), and bitwise operators allow you to perform logical operations on these bits.

### **Bitwise Operators in Python**

1. **AND (`&`)**
2. **OR (`|`)**
3. **XOR (`^`)**
4. **NOT (`~`)**

#### **1. Bitwise AND (`&`)**

Performs a logical AND operation on each pair of corresponding bits of two integers. The result bit is `1` only if both input bits are `1`; otherwise, it's `0`.

**Syntax:**

```python
result = a & b
```

**Example:**

```python
a = 60        # Binary: 0011 1100
b = 13        # Binary: 0000 1101
result = a & b  # Binary: 0000 1100 (12)
print(result)   # Output: 12
```

**Explanation:**

```
   60: 0011 1100
&  13: 0000 1101
--------------
      0000 1100  => 12
```

#### **2. Bitwise OR (`|`)**

Performs a logical OR operation on each pair of corresponding bits. The result bit is `1` if at least one of the input bits is `1`; otherwise, it's `0`.

**Syntax:**

```python
result = a | b
```

**Example:**

```python
a = 60        # Binary: 0011 1100
b = 13        # Binary: 0000 1101
result = a | b  # Binary: 0011 1101 (61)
print(result)   # Output: 61
```

**Explanation:**

```
   60: 0011 1100
|  13: 0000 1101
--------------
      0011 1101  => 61
```

#### **3. Bitwise XOR (`^`)**

Performs a logical exclusive OR (XOR) operation on each pair of corresponding bits. The result bit is `1` if the input bits are different; otherwise, it's `0`.

**Syntax:**

```python
result = a ^ b
```

**Example:**

```python
a = 60        # Binary: 0011 1100
b = 13        # Binary: 0000 1101
result = a ^ b  # Binary: 0011 0001 (49)
print(result)   # Output: 49
```

**Explanation:**

```
   60: 0011 1100
^  13: 0000 1101
--------------
      0011 0001  => 49
```

#### **4. Bitwise NOT (`~`)**

Performs a logical NOT operation on each bit, inverting the bits (i.e., `1` becomes `0` and `0` becomes `1`). In Python, the result is the complement of the number, which is equal to `-x-1`.

**Syntax:**

```python
result = ~a
```

**Example:**

```python
a = 60         # Binary: 0011 1100
result = ~a    # Binary: 1100 0011 (Two's complement: -61)
print(result)  # Output: -61
```

**Explanation:**

```
~60 = -(60) - 1 = -61
```

### **Additional Examples**

#### **Example 1: Clearing Specific Bits Using AND**

To clear (set to `0`) specific bits in a number, you can use the AND operator with a mask.

```python
a = 0b10101010  # 170 in decimal
mask = 0b11110000
result = a & mask  # 0b10100000 (160)
print(bin(result))  # Output: 0b10100000
```

#### **Example 2: Setting Specific Bits Using OR**

To set specific bits to `1`, use the OR operator with a mask.

```python
a = 0b10100000  # 160 in decimal
mask = 0b00001111
result = a | mask  # 0b10101111 (175)
print(bin(result))  # Output: 0b10101111
```

#### **Example 3: Toggling Specific Bits Using XOR**

To toggle specific bits (flip `0` to `1` and `1` to `0`), use the XOR operator with a mask.

```python
a = 0b10101111  # 175 in decimal
mask = 0b00001111
result = a ^ mask  # 0b10100000 (160)
print(bin(result))  # Output: 0b10100000
```

### **Best Practices**

- **Use Masks Carefully:** When manipulating specific bits, ensure your masks are correctly defined to target the desired bits.
- **Understand Two's Complement:** Bitwise NOT in Python uses two's complement representation, which affects how negative numbers are handled.
- **Combine Operators:** Often, multiple bitwise operations are combined to achieve complex bit manipulation tasks.

---
