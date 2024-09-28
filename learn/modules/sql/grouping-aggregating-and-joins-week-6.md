---
title: "Grouping, Aggregating, and Joins [Week 6]"
---

#### **Aggregating Data**

-   **SUM**: Calculate the total of a numeric column.
    
    ```sql
    `SELECT SUM(column_name) FROM table_name;` 
    ```
-   **MAX, MIN**: Find the maximum and minimum values in a column.
    
   ```sql
    `SELECT MAX(column_name), MIN(column_name) FROM table_name;` 
    ```
-   **COUNT**: Count the number of rows.
   ```sql   
    
    `SELECT COUNT(column_name) FROM table_name;` 
    ```
-   **AVG**: Calculate the average value.
    
   ```sql 
    `SELECT AVG(column_name) FROM table_name;` 
   ``` 

#### **GROUP BY and HAVING**

-   **GROUP BY**: Group rows sharing a common attribute.
    
   ```sql
    
    `SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;` 
   ``` 
-   **HAVING**: Filter groups after aggregation.
    
   ```sql
    `SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING COUNT(*) > 1;` 
   ``` 

#### **JOINS**

-   **INNER JOIN**: Return records that have matching values in both tables.
    
   ```sql
   `SELECT columns FROM table1
   INNER JOIN table2 ON table1.column = table2.column;` 
   ```
-   **LEFT JOIN**: Return all records from the left table, and the matched records from the right table.
    
   ```sql
    `SELECT columns FROM table1
    LEFT JOIN table2 ON table1.column = table2.column;` 
  ```  
-   **RIGHT JOIN**: Return all records from the right table, and the matched records from the left table.
    ```sql
    `SELECT columns FROM table1
    RIGHT JOIN table2 ON table1.column = table2.column;` 
    ```
-   **FULL OUTER JOIN**: Return all records when there is a match in either table.

   ```sql    
    `SELECT columns FROM table1
    FULL OUTER JOIN table2 ON table1.column = table2.column;` 
    ```