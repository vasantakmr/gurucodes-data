---
title: "SQL Queries and Operators [Week 7]"
---

#### **SELECT and Filtering Data**

- **SELECT**: Retrieve data from a table.
  ```sql
  SELECT column_name FROM table_name;
  ```

- **DISTINCT**: Retrieve unique records.
  ```sql
  SELECT DISTINCT column_name FROM table_name;
  ```

- **WHERE**: Filter records based on a condition.
  ```sql
  SELECT * FROM table_name WHERE condition;
  ```

- **LIKE**: Search for a specified pattern in a column.
  ```sql
  SELECT * FROM table_name WHERE column_name LIKE '%pattern%';
  ```

- **ORDER BY**: Sort the result-set.
  ```sql
  SELECT * FROM table_name ORDER BY column_name ASC|DESC;
  ```

- **LIMIT/TOP**: Limit the number of records returned
  ```sql
  SELECT * FROM table_name LIMIT number;
  ```

#### **Logical Operators**

- **AND, OR, NOT**: Combine multiple conditions in the WHERE clause.
  ```sql
  SELECT * FROM table_name WHERE condition1 AND condition2;
  ```

- **IN**: Match against multiple values.
  ```sql
  SELECT * FROM table_name WHERE column_name IN ('value1', 'value2');
  ```
  
- **BETWEEN**: Filter a range of values.
   ```sql
   SELECT * FROM table_name WHERE column_name BETWEEN value1 AND value2;
   ```
