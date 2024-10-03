---
title: "Operators"
---

Operators are used to perform operations on data.

---

### Arithmetic Operators

Arithmetic operators perform mathematical operations.

**Operators:**

- `+` (Addition)
- `-` (Subtraction)
- `*` (Multiplication)
- `/` (Division)
- `%` (Modulus)

**Example:**
Calculating the total revenue after applying a discount:

```sql
SELECT Title, Revenue, Revenue - (Revenue * 0.1) AS DiscountedRevenue
FROM Movies;
```

**Real-life Example:**
Using arithmetic operators is like calculating the total cost of items in your shopping cart after applying discounts.

---

### Comparison Operators

Comparison operators compare two values.

**Operators:**

- `=` (Equal)
- `!=` or `<>` (Not Equal)
- `>` (Greater Than)
- `<` (Less Than)
- `>=` (Greater Than or Equal To)
- `<=` (Less Than or Equal To)

**Example:**
Finding movies released after 2015:

```sql
SELECT Title
FROM Movies
WHERE ReleaseYear > 2015;
```

**Real-life Example:**
Using comparison operators is like filtering search results based on criteria, such as finding all movies released after a certain year.

---

### Logical Operators

Logical operators are used to combine multiple conditions.

**Operators:**

- `AND`
- `OR`
- `NOT`

**Example:**
Finding movies that are either action or drama and have a rating greater than 8:

```sql
SELECT Title
FROM Movies
WHERE (Genre = 'Action' OR Genre = 'Drama') AND Rating > 8;
```

**Real-life Example:**
Using logical operators is like refining your search criteria on a movie streaming service to find movies that meet multiple conditions.
