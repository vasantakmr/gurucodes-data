---
title: "CROSS JOIN"
---

A `CROSS JOIN` returns the Cartesian product of the two tables, combining all rows from the left table with all rows from the right table.

**Syntax:**

```sql
SELECT columns
FROM table1
CROSS JOIN table2;
```

**Example:**
To get all possible combinations of movies and directors:

```sql
SELECT Movies.Title, Directors.DirectorName
FROM Movies
CROSS JOIN Directors;
```

**Result (Varies on the input data you entered):**

| Title                    | DirectorName       |
| ------------------------ | ------------------ |
| Baahubali: The Beginning | S. S. Rajamouli    |
| Baahubali: The Beginning | Trivikram Srinivas |
| Eega                     | S. S. Rajamouli    |
| Eega                     | Trivikram Srinivas |
| Ala Vaikunthapurramuloo  | S. S. Rajamouli    |
| Ala Vaikunthapurramuloo  | Trivikram Srinivas |
