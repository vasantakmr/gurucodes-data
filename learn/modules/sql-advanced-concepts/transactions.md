---
title: "Transactions"
---

Transactions are used to ensure that a series of SQL operations are executed as a single unit of work. They follow the ACID properties.

---

### ACID Properties

1. **Atomicity**: Ensures that all operations within a transaction are completed successfully. If not, the transaction is aborted and no changes are made.
2. **Consistency**: Ensures that a transaction brings the database from one valid state to another.
3. **Isolation**: Ensures that concurrent transactions do not affect each other.
4. **Durability**: Ensures that the results of a transaction are permanently stored in the system.

**Real-life Example:**
Consider a banking system where transferring money from one account to another must be a single transaction to ensure the money is either fully transferred or not at all.

---

### COMMIT, ROLLBACK, and SAVEPOINT

**COMMIT**

The `COMMIT` statement is used to save all changes made during the current transaction.

**Syntax:**

```sql
COMMIT;
```

**Example:**

```sql
BEGIN TRANSACTION;
UPDATE TeluguMovies SET ReleaseYear = 2020 WHERE MovieID = 1;
COMMIT;
```

**ROLLBACK**

The `ROLLBACK` statement is used to undo changes made during the current transaction.

**Syntax:**

```sql
ROLLBACK;
```

**Example:**

```sql
BEGIN TRANSACTION;
UPDATE TeluguMovies SET ReleaseYear = 2020 WHERE MovieID = 1;
ROLLBACK;
```

**SAVEPOINT**

The `SAVEPOINT` statement sets a point within a transaction to which you can later roll back.

**Syntax:**

```sql
SAVEPOINT savepoint_name;
```

**Example:**

```sql
BEGIN TRANSACTION;
UPDATE TeluguMovies SET ReleaseYear = 2020 WHERE MovieID = 1;
SAVEPOINT Savepoint1;
UPDATE TeluguMovies SET Genre = 'Drama' WHERE MovieID = 2;
ROLLBACK TO Savepoint1;
COMMIT;
```
