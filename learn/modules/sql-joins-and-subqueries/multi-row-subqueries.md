---
title: "Multi-Row Subqueries"
---

A multi-row subquery returns multiple rows. It is typically used with operators like `IN`, `ANY`, `ALL`.

**Example:**
Finding all movies directed by directors who have directed more than one movie:

```sql
SELECT Title
FROM Movies
WHERE DirectorID IN (SELECT DirectorID
                     FROM Movies
                     GROUP BY DirectorID
                     HAVING COUNT(*) > 1);
```

**Result (Varies on the input data you entered):**

Title

---

Baahubali: The Beginning

---

Eega

---
