---
title: "Inserting Data"
---

### INSERT INTO

The `INSERT INTO` command is used to add new records to a table.

**Syntax:**

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Example:**
Adding a new Telugu movie to the `Movies` table:

```sql
INSERT INTO Movies (MovieID, Title, Director, ReleaseYear, Genre)
VALUES (1, 'Baahubali: The Beginning', 'S. S. Rajamouli', 2015, 'Action/Drama');
```

**Real-life Example:**
Inserting a record is like adding a new document to one of the folders in your drawer.
