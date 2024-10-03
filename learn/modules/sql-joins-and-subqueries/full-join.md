---
title: "FULL JOIN"
---

A `FULL JOIN` returns all rows when there is a match in either the left or right table. If there is no match, the result is NULL from the side where there is no match.

**Syntax:**

```sql
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

**Example:**
To get a complete list of all movies and directors, including those with no matching records:

```sql
SELECT Movies.Title, Directors.DirectorName
FROM Movies
FULL JOIN Directors
ON Movies.DirectorID = Directors.DirectorID;
```

**Result (Varies on the input data you entered):**

| Title                    | DirectorName       |
| ------------------------ | ------------------ |
| Baahubali: The Beginning | S. S. Rajamouli    |
| Eega                     | S. S. Rajamouli    |
| Ala Vaikunthapurramuloo  | Trivikram Srinivas |
| NULL                     | Sukumar            |
| Vinaya Vidheya Rama      | NULL               |
