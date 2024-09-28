---
title: "Views, Indexes, and Performance Optimization [Week 8]"
---

#### **Views**

A **View** in SQL is a virtual table that is derived from one or more underlying tables or other views. The result of a SQL query can be stored as a view, and it can be queried just like a regular table. However, it doesn't store any actual data, rather, it stores a query that can be executed whenever the view is called.

**Advantages of Views**:
- Simplifies complex queries by encapsulating them under a single name.
- Provides an additional layer of security by restricting access to specific columns or rows.
- Allows abstraction of complex joins, subqueries, and transformations into a single query structure.
- Ensures data consistency by enabling you to change a single view, rather than updating multiple queries.

**Creating a View**:
```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```


**Example**: If you want to create a view for retrieving employee names and their departments from an `employees` table:

```sql


`CREATE VIEW employee_view AS
SELECT employee_name, department
FROM employees
WHERE status = 'active';` 
```
**Querying a View**: Once the view is created, you can query it like a regular table:

```sql
`SELECT * FROM employee_view;` 
```
**Updating Data through Views**:  
In most cases, you can update data in a view, but there are certain limitations. For example, you can’t update a view that involves joins or aggregations.

```sql
`UPDATE employee_view
SET department = 'HR'
WHERE employee_name = 'John Doe';` 
```
#### **Indexes**

An **Index** in SQL is a database object that improves the speed of data retrieval operations on a table at the cost of additional storage. Indexes function similarly to an index in a book, where you can quickly look up a topic and find its location without scanning the entire book.

**Types of Indexes**:

1.  **Clustered Index**:
    
    -   Sorts and stores the actual data rows of the table based on the key values.
    -   A table can only have one clustered index, as the rows can only be sorted in one order.
    -   Clustered index directly affects the physical ordering of the data.
2.  **Non-Clustered Index**:
    
    -   Contains a sorted pointer to the actual data rows, but does not affect the physical order of the data.
    -   A table can have multiple non-clustered indexes, providing multiple ways to speed up queries on different columns.

**Creating an Index**: To create a basic non-clustered index on a table:

```sql


`CREATE INDEX index_name ON table_name (column_name);` 
```
**Example**: If you frequently query the `last_name` column in the `employees` table, creating an index on that column will speed up these queries:

```sql

`CREATE INDEX idx_last_name ON employees (last_name);` 
```
**Clustered Index Example**: You can create a clustered index on the `employee_id` column to optimize queries based on employee IDs:

```sql

`CREATE CLUSTERED INDEX idx_employee_id ON employees (employee_id);` 
```
#### **Clustered vs Non-Clustered Indexes**

-   **Clustered Index**:
    
    -   There can only be one clustered index per table.
    -   The data in the table is physically sorted to match the clustered index.
    -   Ideal for queries that return large result sets or range queries.
-   **Non-Clustered Index**:
    
    -   You can create multiple non-clustered indexes on a table.
    -   Points to the physical location of the data in the table without sorting it.
    -   Best for queries that filter or search by specific values.

#### **Performance Optimization Using Indexes**

Indexes can significantly speed up read operations (e.g., `SELECT` queries), especially on large datasets. However, they come with trade-offs:

-   **Index Maintenance**: Indexes require additional storage and slow down write operations (e.g., `INSERT`, `UPDATE`, `DELETE`), as each modification requires updating the index.
-   **Too Many Indexes**: Having too many indexes can slow down performance for write-heavy applications, so it's essential to index only frequently queried columns.

**Best Practices for Indexing**:

-   Use indexes on columns that are frequently used in `WHERE`, `JOIN`, `GROUP BY`, or `ORDER BY` clauses.
-   Avoid indexing columns with low selectivity, such as columns with only a few unique values (e.g., boolean fields).
-   Consider the read-to-write ratio of your application: if you have a lot of `INSERT` or `UPDATE` queries, limit the number of indexes to reduce overhead.

----------

#### **Additional Performance Optimization Tips**

1.  **Avoid `SELECT *` in Production**:  
    Using `SELECT *` retrieves all columns from a table, even if you only need a few columns. This can lead to unnecessary data retrieval, causing slower performance.
    
    Instead, specify only the columns you need:
    
    ```sql
    
    `SELECT column1, column2 FROM table_name;` 
    ```
2.  **Limit Result Sets**:  
    If you're working with large datasets, always use `LIMIT` (or `TOP` in SQL Server) to restrict the number of rows returned by the query. This helps reduce the amount of data processed by the database and transmitted over the network.
    
    Example:
    
    ```sql
    
    `SELECT column1, column2
    FROM table_name
    WHERE condition
    LIMIT 100;` 
    ```
3.  **Use Joins Efficiently**:  
    When working with multiple tables, ensure that your joins are properly indexed. Joins on unindexed columns can be slow and resource-intensive. Always try to join tables on indexed columns, typically primary and foreign keys.
    
4.  **Analyze Query Execution Plans**:  
    Most database systems provide tools for analyzing query execution plans. Use them to see how the database engine executes your queries, and look for areas to optimize (e.g., missing indexes, full table scans).
    
5.  **Use Caching**:  
    In some cases, caching frequently accessed data outside of the database (e.g., in-memory cache systems like Redis) can reduce the load on your database and improve performance.
    

```sql

`EXPLAIN SELECT column1, column2
FROM table_name
WHERE condition;` 
```