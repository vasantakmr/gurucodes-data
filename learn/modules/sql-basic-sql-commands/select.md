---
title: "Selecting Data"
---

### SELECT

The `SELECT` command is used to retrieve data from one or more tables. It's the most commonly used SQL command.

**Syntax:**

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Example:**
Retrieving all movies directed by 'S. S. Rajamouli':

```sql
SELECT * FROM Movies
WHERE Director = 'S. S. Rajamouli';
```

**Real-life Example:**
Using `SELECT` is like pulling out documents from your drawer that match a certain criteria.
