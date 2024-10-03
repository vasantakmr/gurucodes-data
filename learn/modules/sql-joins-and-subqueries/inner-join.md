---
title: "INNER JOIN"
---

Joins are used to combine rows from two or more tables based on a related column. Let's explore the different types of joins with examples.

---

### INNER JOIN

An `INNER JOIN` returns only the rows that have matching values in both tables.

**Syntax:**

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;

```

**Example:**
Suppose we have two tables, `Movies` and `Directors`:

```sql
CREATE TABLE Movies (
    MovieID INT,
    Title VARCHAR(100),
    DirectorID INT,
    ReleaseYear INT
);

CREATE TABLE Directors (
    DirectorID INT,
    DirectorName VARCHAR(100)
);

INSERT INTO Movies (MovieID, Title, DirectorID, ReleaseYear) VALUES
(1, 'Baahubali: The Beginning', 101, 2015),
(2, 'Eega', 101, 2012),
(3, 'Ala Vaikunthapurramuloo', 102, 2020);

INSERT INTO Directors (DirectorID, DirectorName) VALUES
(101, 'S. S. Rajamouli'),
(102, 'Trivikram Srinivas');
```

To get a list of movies along with their directors:

```sql
SELECT Movies.Title, Directors.DirectorName
FROM Movies
INNER JOIN Directors
ON Movies.DirectorID = Directors.DirectorID;
```

**Result (Varies on the input data you entered):**

| Title                    | DirectorName       |
| ------------------------ | ------------------ |
| Baahubali: The Beginning | S. S. Rajamouli    |
| Eega                     | S. S. Rajamouli    |
| Ala Vaikunthapurramuloo  | Trivikram Srinivas |
