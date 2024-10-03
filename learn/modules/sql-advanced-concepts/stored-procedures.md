---
title: "Stored Procedures"
---

Stored procedures are a collection of SQL statements that can be executed as a single unit. They help in reusing code and improving performance.

---

### Creating and Executing Stored Procedures

**Creating a Stored Procedure**

**Syntax:**

```sql
CREATE PROCEDURE procedure_name
AS
BEGIN
    SQL statements;
END;
```

**Example:**
Creating a stored procedure to add a new movie.

```sql
CREATE PROCEDURE AddMovie
    @Title VARCHAR(100),
    @DirectorID INT,
    @ReleaseYear INT,
    @Genre VARCHAR(50)
AS
BEGIN
    INSERT INTO TeluguMovies (Title, DirectorID, ReleaseYear, Genre)
    VALUES (@Title, @DirectorID, @ReleaseYear, @Genre);
END;
```

**Executing a Stored Procedure**

```sql
EXEC AddMovie 'RRR', 101, 2021, 'Action/Drama';
```

**Real-life Example:**
A stored procedure is like a macro in Excel that performs a series of actions automatically when you run it.
