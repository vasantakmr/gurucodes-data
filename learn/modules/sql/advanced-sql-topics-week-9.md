---
title: "Advanced SQL Topics [Week 9]"
---


### **Normalization**

Normalization is a process in database design that organizes tables to reduce redundancy and improve data integrity. It ensures that tables are structured to minimize duplication of information and avoid anomalies during data manipulation (e.g., insertions, updates, and deletions). There are several levels of normalization, known as **Normal Forms (NFs)**.



#### **1NF: First Normal Form**
- Eliminate duplicate columns from the same table.
- Ensure each table cell contains only **atomic** (indivisible) values, and each record must be unique.

**Example:**

A non-normalized table might look like this:

| ID  | Name   | Phone Numbers       |
| --- | ------ | ------------------- |
| 1   | John   | 123-4567, 789-4567  |
| 2   | Alice  | 321-6547, 654-7894  |

In 1NF, we would split the phone numbers into separate rows:

| ID  | Name   | Phone Number |
| --- | ------ | ------------ |
| 1   | John   | 123-4567     |
| 1   | John   | 789-4567     |
| 2   | Alice  | 321-6547     |
| 2   | Alice  | 654-7894     |


#### **2NF: Second Normal Form**
- Meet all requirements of 1NF.
- Remove subsets of data that apply to multiple rows and place them in separate tables.
- Ensure that every non-key attribute is fully dependent on the entire primary key (in the case of composite keys).

**Example:**

Consider this table that violates 2NF:

| OrderID | CustomerID | CustomerName | ProductID | ProductName |
| ------- | ---------- | ------------ | --------- | ----------- |
| 1       | 101        | John         | 201       | Laptop      |
| 2       | 102        | Alice        | 202       | Tablet      |

Here, `CustomerName` depends only on `CustomerID`, not `OrderID`. To achieve 2NF, we should split the customer data into a separate table:

**Customers Table**:

| CustomerID | CustomerName |
| ---------- | ------------ |
| 101        | John         |
| 102        | Alice        |

**Orders Table**:

| OrderID | CustomerID | ProductID |
| ------- | ---------- | --------- |
| 1       | 101        | 201       |
| 2       | 102        | 202       |

**Products Table**:

| ProductID | ProductName |
| --------- | ----------- |
| 201       | Laptop      |
| 202       | Tablet      |


#### **3NF: Third Normal Form**
- Meet all requirements of 2NF.
- Ensure that non-key attributes depend only on the primary key, and no transitive dependencies (i.e., a non-key attribute should not depend on another non-key attribute).

**Example:**

Consider the following table:

| OrderID | ProductID | ProductName | ProductPrice |
| ------- | --------- | ----------- | ------------ |
| 1       | 201       | Laptop      | 1000         |
| 2       | 202       | Tablet      | 500          |

Here, `ProductName` and `ProductPrice` depend on `ProductID`, not `OrderID`. To achieve 3NF, we should move product details into a separate table:

**Products Table**:

| ProductID | ProductName | ProductPrice |
| --------- | ----------- | ------------ |
| 201       | Laptop      | 1000         |
| 202       | Tablet      | 500          |


### **Subqueries and Common Table Expressions (CTE)**

#### **Subquery**
A **subquery** is a query nested inside another SQL query. Subqueries are often used in `WHERE` or `FROM` clauses to retrieve data based on the results of another query.

**Example:**
```sql
SELECT * 
FROM orders 
WHERE total_amount = (SELECT MAX(total_amount) FROM orders);
```

In this example, the subquery retrieves the maximum total_amount, and the main query retrieves all orders that have that value.


#### **Common Table Expressions (CTE)**

A **CTE** is a temporary result set that can be referenced within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. CTEs are more readable and reusable compared to subqueries.

**Syntax:**

```sql
`WITH cte_name AS (
    SELECT column1, column2
    FROM table_name
    WHERE condition
)
SELECT * 
FROM cte_name;` 
```
**Example:**

```sql

`WITH SalesCTE AS (
    SELECT employee_id, SUM(sales_amount) AS total_sales
    FROM sales
    GROUP BY employee_id
)
SELECT employee_id, total_sales
FROM SalesCTE
WHERE total_sales > 10000;` 
```

This CTE calculates total sales for each employee and then filters employees with sales greater than 10,000.


### **Window Functions**

**Window functions** perform calculations across a set of table rows that are related to the current row. Unlike aggregate functions, window functions do not collapse the result set.


#### **ROW_NUMBER**

The `ROW_NUMBER()` function assigns a unique sequential integer to rows within a result set.

**Syntax:**

```sql

`SELECT ROW_NUMBER() OVER (ORDER BY column_name) AS row_num, *
FROM table_name;` 
```
**Example:**

```sql

`SELECT ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank, employee_name, salary
FROM employees;` 
```
This query assigns a unique rank to employees based on their salary, with the highest salary ranked first.


#### **RANK and DENSE_RANK**

-   `RANK()` assigns a rank to rows, allowing for gaps in the ranking where there are ties.
-   `DENSE_RANK()` assigns ranks without gaps.

**Syntax (RANK)**:

```sql

`SELECT RANK() OVER (ORDER BY salary DESC) AS rank, employee_name, salary
FROM employees;` 
```
**Syntax (DENSE_RANK)**:

```sql

`SELECT DENSE_RANK() OVER (ORDER BY salary DESC) AS rank, employee_name, salary
FROM employees;` 
```

#### **LEAD and LAG**

-   `LAG()` allows you to access data from the previous row in the result set.
-   `LEAD()` allows you to access data from the following row in the result set.

**Example (LAG)**:

```sql

`SELECT employee_name, salary, 
       LAG(salary, 1) OVER (ORDER BY salary DESC) AS previous_salary
FROM employees;` 
```

This query shows each employee's salary along with the salary of the employee ranked just before them.

**Example (LEAD)**:

```sql

`SELECT employee_name, salary, 
       LEAD(salary, 1) OVER (ORDER BY salary DESC) AS next_salary
FROM employees;` 
```
This query shows each employee's salary along with the salary of the employee ranked just after them.



### **Conclusion**

This week introduces crucial advanced SQL concepts such as **normalization**, **subqueries**, **CTEs**, and **window functions**. Mastering these will help you write efficient, maintainable, and optimized SQL queries for handling complex data and performance scenarios.

