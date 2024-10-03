---
title: "Types of SQL Commands"
---

SQL commands are divided into different categories based on their functionality. Here’s a breakdown of the main types of SQL commands:

1. **DDL (Data Definition Language)**

   DDL commands are used to define and modify the structure of database objects like tables, indexes, and schemas. Key DDL commands include:

   - **CREATE**: Used to create a new table, index, or database.
   - **ALTER**: Modifies the structure of an existing table or database.
   - **DROP**: Deletes tables, indexes, or databases.
   - **TRUNCATE**: Removes all records from a table but retains the structure for future use.

   **Real-life Example**: When setting up a new customer management system, a company would use DDL commands to create tables for storing customer information, orders, and product details.

2. **DML (Data Manipulation Language)**

   DML commands are used to manipulate the data within database objects. These include:

   - **SELECT**: Retrieves data from one or more tables.
   - **INSERT**: Adds new records to a table.
   - **UPDATE**: Modifies existing records in a table.
   - **DELETE**: Removes records from a table.

   **Real-life Example**: A retail store using an inventory system would use DML commands to update stock levels as products are sold and restocked.

3. **DCL (Data Control Language)**

   DCL commands manage access permissions and control the security of the database. These commands include:

   - **GRANT**: Gives a user permission to perform specific tasks.
   - **REVOKE**: Removes previously granted permissions from a user.

   **Real-life Example**: In a banking system, administrators use DCL commands to grant access to different levels of data to employees based on their roles and responsibilities.

4. **TCL (Transaction Control Language)**

   TCL commands are used to manage transactions in a database, ensuring that operations are completed successfully before making changes permanent. Key TCL commands include:

   - **COMMIT**: Saves all changes made during the current transaction.
   - **ROLLBACK**: Reverts the database to its previous state before the transaction began.
   - **SAVEPOINT**: Sets a savepoint within a transaction to which you can later roll back.

   **Real-life Example**: During an online purchase, TCL commands ensure that payment processing, order placement, and inventory updates are all completed successfully. If any part of the process fails, a rollback ensures the database remains consistent and accurate.
