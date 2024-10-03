---
title: "Triggers"
---

Triggers are special types of stored procedures that automatically execute in response to certain events on a table or view.

---

### Creating and Managing Triggers

**Creating a Trigger**

**Syntax:**

```sql
CREATE TRIGGER trigger_name
ON table_name
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SQL statements;
END;
```

**Example:**
Creating a trigger that logs changes to the `TeluguMovies` table.

```sql
CREATE TRIGGER LogMovieChanges
ON TeluguMovies
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    INSERT INTO MovieLog (ChangeType, MovieID, ChangeDate)
    VALUES (CASE
                WHEN EXISTS (SELECT * FROM INSERTED) AND EXISTS (SELECT * FROM DELETED) THEN 'UPDATE'
                WHEN EXISTS (SELECT * FROM INSERTED) THEN 'INSERT'
                WHEN EXISTS (SELECT * FROM DELETED) THEN 'DELETE'
            END,
            COALESCE((SELECT MovieID FROM INSERTED), (SELECT MovieID FROM DELETED)),
            GETDATE());
END;
```

**Real-life Example:**
A trigger is like a notification system that alerts you whenever specific changes happen in your database.
