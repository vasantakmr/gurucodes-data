---
title: "WHERE Clause"
---

The `WHERE` clause is used to filter records that meet a certain condition. It is essential for retrieving specific data from a database.

---

### Filtering Data

The `WHERE` clause allows you to specify conditions that the data must meet to be included in the result set.

**Syntax:**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Example:**
Imagine you have a table `TeluguMovies` with columns `MovieID`, `Title`, `Director`, and `ReleaseYear`. To find all movies directed by S. S. Rajamouli:

```sql
SELECT Title, ReleaseYear
FROM TeluguMovies
WHERE Director = 'S. S. Rajamouli';
```

**Real-life Example:**
Using the `WHERE` clause is like applying a filter to your search results on a movie database to only show movies by a specific director.

---

**Example 1:**
Finding movies released after the year 2010:

```sql
SELECT Title, ReleaseYear
FROM TeluguMovies
WHERE ReleaseYear > 2010;
```

**Example 2:**
Finding movies with the genre 'Action':

```sql
SELECT Title, Director
FROM TeluguMovies
WHERE Genre = 'Action';
```
