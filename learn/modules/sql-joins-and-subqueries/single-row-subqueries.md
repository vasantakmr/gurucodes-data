---
title: "Single-Row Subqueries"
---

Subqueries are queries nested inside another query. They can be used to perform operations that require multiple steps or to simplify complex queries.

---

### Single-Row Subqueries

A single-row subquery returns one row. It is typically used with comparison operators like `=`, `<`, `>`, etc.

**Example:**
Finding the director of the most recent movie:

```sql
SELECT DirectorName
FROM Directors
WHERE DirectorID = (SELECT DirectorID
                    FROM Movies
                    ORDER BY ReleaseYear DESC
                    LIMIT 1);
```

**Result (Varies on the input data you entered):**

DirectorName

---

Trivikram Srinivas

---
