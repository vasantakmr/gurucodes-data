---
title: "GROUP BY Clause"
---

The `GROUP BY` clause groups rows that have the same values in specified columns into summary rows, like "total", "average", "count", etc.

---

### Aggregating Data

The `GROUP BY` clause is often used with aggregate functions (COUNT, MAX, MIN, SUM, AVG) to group the result set by one or more columns.

**Syntax:**

```sql
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1;
```

**Example:**
To find the number of movies directed by each director:

```sql
SELECT Director, COUNT(*) AS NumberOfMovies
FROM TeluguMovies
GROUP BY Director;
```

**Real-life Example:**
Using `GROUP BY` is like organizing your movie list by director and then counting how many movies each director has made.

---

**Example 1:**
Finding the average rating of movies by each director:

```sql
SELECT Director, AVG(Rating) AS AverageRating
FROM TeluguMovies
GROUP BY Director;
```

**Example 2:**
Counting the number of movies in each genre:

```sql
SELECT Genre, COUNT(*) AS NumberOfMovies
FROM TeluguMovies
GROUP BY Genre;
```
