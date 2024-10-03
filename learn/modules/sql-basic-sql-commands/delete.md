---
title: "Deleting Data"
---

### DELETE

The `DELETE` command is used to remove records from a table.

**Syntax:**

```sql
DELETE FROM table_name
WHERE condition;
```

**Example:**
Deleting a movie from the `Movies` table:

```sql
DELETE FROM Movies
WHERE MovieID = 1;
```

**Real-life Example:**
Deleting a record is like removing a document from a folder and discarding it.
