---
title: "Creating a Database and Tables"
---

Creating databases and tables is the first step in organizing your data. Let's break down the commands and concepts involved.

---

### CREATE DATABASE

The `CREATE DATABASE` command is used to create a new database. A database is a collection of tables and other objects that store and organize data.

**Syntax:**

```sql
CREATE DATABASE database_name;
```

**Example:**
Imagine you’re setting up a database for a Telugu movie rental store. You would start by creating a database named `TeluguMoviesDB`:

```sql
CREATE DATABASE TeluguMoviesDB;
```

**Real-life Example:**
Think of `CREATE DATABASE` as setting up a new file cabinet for organizing all the documents related to your project. Just like you would name a file cabinet, you give your database a name that reflects its purpose.

---

### CREATE TABLE

The `CREATE TABLE` command is used to create a new table within a database. A table is a collection of related data held in a structured format within a database. It consists of rows and columns.

**Syntax:**

```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

**Example:**
Continuing with the Telugu movie rental store example, you might create a table for movies:

```sql
CREATE TABLE Movies (
    MovieID INT PRIMARY KEY,
    Title VARCHAR(100),
    Director VARCHAR(100),
    ReleaseYear INT,
    Genre VARCHAR(50)
);
```

**Real-life Example:**
Creating a table is like setting up a new drawer in your file cabinet with labeled folders (columns) where each folder holds documents (rows) of a specific type.
