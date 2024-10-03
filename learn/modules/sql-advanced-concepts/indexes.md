---
title: "Indexes"
---

Indexes improve the speed of data retrieval operations on a database table at the cost of additional storage space and slower write operations.

---

### Types and Uses of Indexes

**Types of Indexes**

1. **Clustered Index**: Determines the physical order of data in a table. Each table can have only one clustered index.
2. **Non-Clustered Index**: Does not alter the physical order of the data. Each table can have multiple non-clustered indexes.
3. **Unique Index**: Ensures all values in the index are unique.
4. **Full-Text Index**: Used for performing full-text searches.

**Uses of Indexes**

Indexes are used to:

- Speed up the retrieval of rows.
- Enforce uniqueness with unique indexes.
- Improve performance of search queries with full-text indexes.

**Example:**
Creating an index on the `Title` column of the `TeluguMovies` table.

```sql
CREATE INDEX idx_title ON TeluguMovies (Title);
```

---

### Creating and Dropping Indexes

**Creating an Index**

**Syntax:**

```sql
CREATE [UNIQUE] INDEX index_name ON table_name (column1, column2, ...);
```

**Example:**
Creating a unique index on the `MovieID` column.

```sql
CREATE UNIQUE INDEX idx_movie_id ON TeluguMovies (MovieID);
```

**Dropping an Index**

**Syntax:**

```sql
DROP INDEX index_name;
```

**Example:**
Dropping the index on the `Title` column.

```sql
DROP INDEX idx_title;
```

**Real-life Example:**
Using an index is like having a detailed table of contents in a book that allows you to quickly find the information you need without flipping through every page.
