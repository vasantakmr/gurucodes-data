---
title: "ORDER BY Clause"
---

The `ORDER BY` clause is used to sort the result set by one or more columns, either in ascending (default) or descending order.

---

### Sorting Data

The `ORDER BY` clause arranges the records in a specified order.

**Syntax:**

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

**Example:**
To list all movies sorted by their release year in descending order:

```sql
SELECT Title, ReleaseYear
FROM TeluguMovies
ORDER BY ReleaseYear DESC;
```

**Real-life Example:**
Using the `ORDER BY` clause is like sorting your movie collection by release date to find the most recent ones easily.

---

**Example 1:**
Sorting movies by title in ascending order:

```sql
SELECT Title, ReleaseYear
FROM TeluguMovies
ORDER BY Title ASC;
```

**Example 2:**
Sorting movies by release year and then by title:

```sql
SELECT Title, ReleaseYear
FROM TeluguMovies
ORDER BY ReleaseYear ASC, Title ASC;
```
