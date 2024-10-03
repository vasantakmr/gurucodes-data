---
title: "Correlated Subqueries"
---

A correlated subquery is a subquery that uses values from the outer query. It is executed once for each row processed by the outer query.

**Example:**
Finding movies where the director has directed another movie in the same year:

```sql
SELECT Title
FROM Movies m1
WHERE EXISTS (SELECT 1
              FROM Movies m2
              WHERE m1.DirectorID = m2.DirectorID
              AND m1.ReleaseYear = m2.ReleaseYear
              AND m1.MovieID <> m2.MovieID);
```

**Result (Varies on the input data you entered):**

Title

---

Eega

---
