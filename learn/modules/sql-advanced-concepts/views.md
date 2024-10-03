---
title: "Views"
---

A view is a virtual table based on the result set of an SQL query. Views simplify complex queries, enhance security, and make data more accessible.

---

### Creating and Managing Views

**Creating a View**

A view is created using the `CREATE VIEW` statement.

**Syntax:**

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Example:**
Imagine we have a table `TeluguMovies` and we want to create a view that shows only movies directed by 'S. S. Rajamouli'.

```sql
CREATE VIEW RajamouliMovies AS
SELECT Title, ReleaseYear
FROM TeluguMovies
WHERE Director = 'S. S. Rajamouli';
```

To query the view:

```sql
SELECT * FROM RajamouliMovies;
```

**Managing Views**

Views can be updated, dropped, or replaced as needed.

**Updating a View**

```sql
CREATE OR REPLACE VIEW RajamouliMovies AS
SELECT Title, ReleaseYear, Genre
FROM TeluguMovies
WHERE Director = 'S. S. Rajamouli';
```

**Dropping a View**

```sql
DROP VIEW RajamouliMovies;
```

**Real-life Example:**
Creating a view is like setting up a specific filter or report in your software application that shows only relevant data to the user without them needing to write complex queries.
