---
title: "Roles and Permissions"
---

Roles simplify the management of permissions by grouping privileges and assigning them to users.

---

### Granting and Revoking Privileges

**Granting Privileges**

**Syntax:**

```sql
GRANT privilege_name ON database_name.table_name TO 'username'@'host';
```

**Example:**
Granting SELECT and INSERT privileges to `telugu_movie_admin` on the `TeluguMoviesDB`:

```sql
GRANT SELECT, INSERT ON TeluguMoviesDB.* TO 'telugu_movie_admin'@'localhost';
```

**Revoking Privileges**

**Syntax:**

```sql
REVOKE privilege_name ON database_name.table_name FROM 'username'@'host';
```

**Example:**
Revoking INSERT privilege from `telugu_movie_admin`:

```sql
REVOKE INSERT ON TeluguMoviesDB.* FROM 'telugu_movie_admin'@'localhost';
```

**Creating Roles**

Roles are created to group specific privileges and then granted to users.

**Syntax:**

```sql
CREATE ROLE 'role_name';
GRANT privilege_name ON database_name.table_name TO 'role_name';
GRANT 'role_name' TO 'username'@'host';

```

**Example:**
Creating a role for read-only access and assigning it to a user:

```sql
CREATE ROLE 'read_only';
GRANT SELECT ON TeluguMoviesDB.* TO 'read_only';
GRANT 'read_only' TO 'telugu_movie_viewer'@'localhost';
```
