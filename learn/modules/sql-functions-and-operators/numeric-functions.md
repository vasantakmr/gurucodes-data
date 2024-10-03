---
title: "Numeric Functions"
---

Numeric functions perform operations on numerical data.

---

### ABS

The `ABS` function returns the absolute value of a number, removing any negative sign.

**Syntax:**

```sql
ABS(number);
```

**Example:**
If you have a column `RevenueChange` in the `Movies` table that stores the change in revenue, and you want to get the absolute values:

```sql
SELECT Title, ABS(RevenueChange) AS AbsoluteChange
FROM Movies;
```

**Real-life Example:**
Using `ABS` is like considering only the magnitude of a number without its sign, similar to how we only care about distance in terms of positive values.

---

### ROUND

The `ROUND` function rounds a number to a specified number of decimal places.

**Syntax:**

```sql
ROUND(number, decimal_places);
```

**Example:**
Rounding the revenue of movies to the nearest thousand in the `Movies` table:

```sql
SELECT Title, ROUND(Revenue, -3) AS RoundedRevenue
FROM Movies;
```

**Real-life Example:**
Using `ROUND` is like rounding prices to the nearest dollar when shopping to simplify calculations.

---

### FLOOR

The `FLOOR` function returns the largest integer less than or equal to a number.

**Syntax:**

```sql
FLOOR(number);
```

**Example:**
Finding the floor value of ratings in a `Movies` table:

```sql
SELECT Title, FLOOR(Rating) AS FloorRating
FROM Movies;
```

**Real-life Example:**
Using `FLOOR` is like rounding down a number to the nearest whole number, similar to dropping any fractional part when dealing with counts.
