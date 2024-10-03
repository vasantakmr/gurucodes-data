---
title: "HAVING Clause"
---

The `HAVING` clause is used to filter groups based on a specified condition. It is similar to the `WHERE` clause but is used for groups rather than individual rows.

---

### Filtering Aggregated Data

The `HAVING` clause filters data after it has been grouped.

**Syntax:**

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

**Example:**
To find directors who have directed more than 3 movies:

```sql
SELECT Director, COUNT(*) AS NumberOfMovies
FROM TeluguMovies
GROUP BY Director
HAVING COUNT(*) > 3;
```

**Real-life Example:**
Using the `HAVING` clause is like filtering a summary report to only show entries that meet certain criteria, such as showing only those directors who have made a significant number of films.

---

**Example 1:**
Finding genres with more than 5 movies:

```sql
SELECT Genre, COUNT(*) AS NumberOfMovies
FROM TeluguMovies
GROUP BY Genre
HAVING COUNT(*) > 5;
```

**Example 2:**
Finding directors with an average movie rating above 7:

```sql
SELECT Director, AVG(Rating) AS AverageRating
FROM TeluguMovies
GROUP BY Director
HAVING AVG(Rating) > 7;
```
