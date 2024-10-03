---
title: "Updating Data"
---

### UPDATE

The `UPDATE` command is used to modify existing records in a table.

**Syntax:**

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Example:**
Updating the genre of a movie:

```sql
UPDATE Movies
SET Genre = 'Epic Action/Drama'
WHERE MovieID = 1;
```

**Real-life Example:**
Updating a record is like editing a document in one of your folders.
