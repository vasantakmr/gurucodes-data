---
title: "User Management"
---

### User Management

Effective user management is crucial for database security. It involves creating and managing database users and ensuring that only authorized individuals have access to the database.

---

### Creating and Managing Users

Creating users and assigning appropriate privileges helps control access to the database.

**Creating a User**

**Syntax:**

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```

**Example:**
Creating a user named `telugu_movie_admin`:

```sql
CREATE USER 'telugu_movie_admin'@'localhost' IDENTIFIED BY 'securepassword';
```

**Managing Users**

You can manage users by changing their passwords, renaming them, or deleting them.

**Changing User Password**

```sql
ALTER USER 'telugu_movie_admin'@'localhost' IDENTIFIED BY 'newsecurepassword';
```

**Renaming a User**

```sql
RENAME USER 'telugu_movie_admin'@'localhost' TO 'telugu_movie_manager'@'localhost';
```

**Deleting a User**

```sql
DROP USER 'telugu_movie_manager'@'localhost';
```
