---
title: "LEFT JOIN"
---

A `LEFT JOIN` returns all rows from the left table and the matched rows from the right table. If there is no match, the result is NULL on the right side.

**Syntax:**

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

**Example:**
To get a list of all movies along with their directors, including movies without a director in the `Directors` table:

```sql
SELECT Movies.Title, Directors.DirectorName
FROM Movies
LEFT JOIN Directors
ON Movies.DirectorID = Directors.DirectorID;
```

**Result (Varies on the input data you entered):**

| Title                    | DirectorName       |
| ------------------------ | ------------------ |
| Baahubali: The Beginning | S. S. Rajamouli    |
| Eega                     | S. S. Rajamouli    |
| Ala Vaikunthapurramuloo  | Trivikram Srinivas |
| Vinaya Vidheya Rama      | NULL               |
