---
title: "RIGHT JOIN"
---

A `RIGHT JOIN` returns all rows from the right table and the matched rows from the left table. If there is no match, the result is NULL on the left side.

**Syntax:**

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

**Example:**
To get a list of all directors and the movies they have directed, including directors with no movies:

```sql
SELECT Movies.Title, Directors.DirectorName
FROM Movies
RIGHT JOIN Directors
ON Movies.DirectorID = Directors.DirectorID;
```

**Result (Varies on the input data you entered):**

| Title                    | DirectorName       |
| ------------------------ | ------------------ |
| Baahubali: The Beginning | S. S. Rajamouli    |
| Eega                     | S. S. Rajamouli    |
| Ala Vaikunthapurramuloo  | Trivikram Srinivas |
| NULL                     | Sukumar            |
