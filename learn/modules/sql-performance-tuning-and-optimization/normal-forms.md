---
title: "Normalization Forms"
---

Database normalization is a systematic approach to organizing data in a database to minimize redundancy and improve data integrity. The process involves decomposing tables into smaller, related tables without losing data, ensuring that each table serves a specific purpose. Normalization is achieved through a series of rules known as **Normal Forms** (NF), each addressing specific types of anomalies and dependencies.

### **Normalization Forms Overview**

1. **First Normal Form (1NF)**
2. **Second Normal Form (2NF)**
3. **Third Normal Form (3NF)**
4. **Boyce-Codd Normal Form (BCNF)**
5. **Fourth Normal Form (4NF)**
6. **Fifth Normal Form (5NF)**

For most practical applications, achieving up to **BCNF** is sufficient.

---

### **1. First Normal Form (1NF)**

**Definition:**
A table is in **First Normal Form (1NF)** if:

- **Atomicity:** Each column contains only atomic (indivisible) values.
- **Uniqueness:** Each record is unique.
- **No Repeating Groups:** There are no repeating groups or arrays.

**Issues Addressed:**

- Eliminates duplicate data.
- Ensures that each field contains only one value.

**Example:**

**Unnormalized Table (Not in 1NF):**

| OrderID | CustomerName | Items Ordered         |
| ------- | ------------ | --------------------- |
| 1       | John Doe     | Laptop, Mouse         |
| 2       | Jane Smith   | Smartphone            |
| 3       | Bob Johnson  | Tablet, Case, Charger |

**Problems:**

- The "Items Ordered" column contains multiple values (non-atomic).

**Normalization to 1NF:**

To convert to 1NF, ensure that each field contains only one value. This can be achieved by creating separate rows for each item ordered.

**1NF Compliant Table:**

| OrderID | CustomerName | Item Ordered |
| ------- | ------------ | ------------ |
| 1       | John Doe     | Laptop       |
| 1       | John Doe     | Mouse        |
| 2       | Jane Smith   | Smartphone   |
| 3       | Bob Johnson  | Tablet       |
| 3       | Bob Johnson  | Case         |
| 3       | Bob Johnson  | Charger      |

---

### **2. Second Normal Form (2NF)**

**Definition:**
A table is in **Second Normal Form (2NF)** if:

- It is already in 1NF.
- **Full Functional Dependency:** All non-key attributes are fully functionally dependent on the **entire** primary key.

**Issues Addressed:**

- Eliminates partial dependencies where non-key attributes depend only on part of a composite primary key.

**Example:**

**Table in 1NF (Composite Primary Key: OrderID + Item):**

| OrderID | Item   | CustomerName | CustomerAddress |
| ------- | ------ | ------------ | --------------- |
| 1       | Laptop | John Doe     | 123 Elm St      |
| 1       | Mouse  | John Doe     | 123 Elm St      |
| 2       | Phone  | Jane Smith   | 456 Oak St      |
| 3       | Tablet | Bob Johnson  | 789 Pine St     |
| 3       | Case   | Bob Johnson  | 789 Pine St     |

**Problems:**

- "CustomerName" and "CustomerAddress" depend only on "OrderID," not on the combination of "OrderID + Item."

**Normalization to 2NF:**

1. **Identify Partial Dependencies:**

   - "CustomerName" and "CustomerAddress" depend only on "OrderID."

2. **Create Separate Tables:**

   **Orders Table:**

   | OrderID | CustomerName | CustomerAddress |
   | ------- | ------------ | --------------- |
   | 1       | John Doe     | 123 Elm St      |
   | 2       | Jane Smith   | 456 Oak St      |
   | 3       | Bob Johnson  | 789 Pine St     |

   **OrderItems Table:**

   | OrderID | Item   |
   | ------- | ------ |
   | 1       | Laptop |
   | 1       | Mouse  |
   | 2       | Phone  |
   | 3       | Tablet |
   | 3       | Case   |

**Result:**

- Each non-key attribute is fully dependent on the primary key of its respective table.

---

### **3. Third Normal Form (3NF)**

**Definition:**
A table is in **Third Normal Form (3NF)** if:

- It is already in 2NF.
- **No Transitive Dependencies:** No non-key attribute depends on another non-key attribute.

**Issues Addressed:**

- Eliminates transitive dependencies where non-key attributes depend on other non-key attributes, not directly on the primary key.

**Example:**

**Table in 2NF:**

**Orders Table:**

| OrderID | CustomerID | CustomerName | CustomerAddress |
| ------- | ---------- | ------------ | --------------- |
| 1       | C001       | John Doe     | 123 Elm St      |
| 2       | C002       | Jane Smith   | 456 Oak St      |
| 3       | C003       | Bob Johnson  | 789 Pine St     |

**Problems:**

- "CustomerName" and "CustomerAddress" depend on "CustomerID," which in turn depends on "OrderID."

**Normalization to 3NF:**

1. **Identify Transitive Dependencies:**

   - "CustomerName" and "CustomerAddress" depend on "CustomerID."

2. **Create Separate Tables:**

   **Orders Table:**

   | OrderID | CustomerID |
   | ------- | ---------- |
   | 1       | C001       |
   | 2       | C002       |
   | 3       | C003       |

   **Customers Table:**

   | CustomerID | CustomerName | CustomerAddress |
   | ---------- | ------------ | --------------- |
   | C001       | John Doe     | 123 Elm St      |
   | C002       | Jane Smith   | 456 Oak St      |
   | C003       | Bob Johnson  | 789 Pine St     |

**Result:**

- Eliminates transitive dependencies by separating customer-related information into its own table.

---

### **4. Boyce-Codd Normal Form (BCNF)**

**Definition:**
A table is in **Boyce-Codd Normal Form (BCNF)** if:

- It is already in 3NF.
- **Every Determinant is a Candidate Key:** For every functional dependency (A → B), A should be a super key.

**Issues Addressed:**

- Handles anomalies not addressed by 3NF, especially in cases of overlapping candidate keys or multiple dependencies.

**Example:**

**Table Not in BCNF:**

Consider a table where a student can have only one advisor, and each advisor can advise multiple departments. Departments can have multiple advisors.

| StudentID | Advisor   | Department   |
| --------- | --------- | ------------ |
| S001      | Dr. Smith | Computer Sci |
| S002      | Dr. Smith | Computer Sci |
| S003      | Dr. Jones | Mathematics  |
| S004      | Dr. Brown | Physics      |

**Functional Dependencies:**

1. StudentID → Advisor
2. Advisor → Department

**Problem:**

- "Advisor" determines "Department," but "Advisor" is not a candidate key.

**Normalization to BCNF:**

1. **Identify Violating Dependencies:**

   - Advisor → Department (Advisor is not a super key)

2. **Decompose the Table:**

   **Students Table:**

   | StudentID | Advisor   |
   | --------- | --------- |
   | S001      | Dr. Smith |
   | S002      | Dr. Smith |
   | S003      | Dr. Jones |
   | S004      | Dr. Brown |

   **Advisors Table:**

   | Advisor   | Department   |
   | --------- | ------------ |
   | Dr. Smith | Computer Sci |
   | Dr. Jones | Mathematics  |
   | Dr. Brown | Physics      |

**Result:**

- Each table now has dependencies where determinants are candidate keys, satisfying BCNF.

---

### **5. Fourth Normal Form (4NF)**

**Definition:**
A table is in **Fourth Normal Form (4NF)** if:

- It is already in BCNF.
- **No Multi-Valued Dependencies:** There are no non-trivial multi-valued dependencies other than a candidate key.

**Issues Addressed:**

- Eliminates scenarios where multiple independent multi-valued facts about an entity are stored in the same table, leading to unnecessary duplication.

**Example:**

**Table Not in 4NF:**

A table where employees can have multiple skills and multiple projects independently.

| EmployeeID | Skill      | Project       |
| ---------- | ---------- | ------------- |
| E001       | Java       | Project Alpha |
| E001       | Python     | Project Beta  |
| E002       | C#         | Project Alpha |
| E002       | SQL        | Project Gamma |
| E003       | JavaScript | Project Beta  |

**Issues:**

- Employees have multiple skills and can work on multiple projects independently, leading to redundant data.

**Normalization to 4NF:**

1. **Identify Multi-Valued Dependencies:**

   - EmployeeID →→ Skill
   - EmployeeID →→ Project

2. **Decompose the Table:**

   **EmployeeSkills Table:**

   | EmployeeID | Skill      |
   | ---------- | ---------- |
   | E001       | Java       |
   | E001       | Python     |
   | E002       | C#         |
   | E002       | SQL        |
   | E003       | JavaScript |

   **EmployeeProjects Table:**

   | EmployeeID | Project       |
   | ---------- | ------------- |
   | E001       | Project Alpha |
   | E001       | Project Beta  |
   | E002       | Project Alpha |
   | E002       | Project Gamma |
   | E003       | Project Beta  |

**Result:**

- Eliminates multi-valued dependencies by separating skills and projects into distinct tables.

---

### **6. Fifth Normal Form (5NF)**

**Definition:**
A table is in **Fifth Normal Form (5NF)**, also known as **Projection-Join Normal Form (PJNF)**, if:

- It is already in 4NF.
- **No Join Dependencies:** The table cannot be decomposed into smaller tables without loss of data.

**Issues Addressed:**

- Deals with cases where information can be reconstructed from smaller pieces of information, ensuring that the database is free from all anomalies.

**Example:**

**Table Not in 5NF:**

Consider a table that records which supplier supplies which part for which project.

| Supplier | Part | Project |
| -------- | ---- | ------- |
| S1       | P1   | ProjA   |
| S1       | P2   | ProjB   |
| S2       | P1   | ProjB   |
| S2       | P3   | ProjA   |
| S3       | P2   | ProjA   |
| S3       | P3   | ProjB   |

**Issues:**

- Complex relationships where supplier, part, and project are interdependent.

**Normalization to 5NF:**

1. **Identify Join Dependencies:**

   - The combination of Supplier, Part, and Project cannot be fully determined by any subset.

2. **Decompose the Table:**

   **SupplierPart Table:**

   | Supplier | Part |
   | -------- | ---- |
   | S1       | P1   |
   | S1       | P2   |
   | S2       | P1   |
   | S2       | P3   |
   | S3       | P2   |
   | S3       | P3   |

   **SupplierProject Table:**

   | Supplier | Project |
   | -------- | ------- |
   | S1       | ProjA   |
   | S1       | ProjB   |
   | S2       | ProjA   |
   | S2       | ProjB   |
   | S3       | ProjA   |
   | S3       | ProjB   |

   **PartProject Table:**

   | Part | Project |
   | ---- | ------- |
   | P1   | ProjA   |
   | P1   | ProjB   |
   | P2   | ProjA   |
   | P2   | ProjB   |
   | P3   | ProjA   |
   | P3   | ProjB   |

**Result:**

- Each table now represents a single relationship, and the original table can be reconstructed by joining these tables without loss of data.

---

## Summary of Normal Forms

| Normal Form | Requirements                                    | Purpose                                       |
| ----------- | ----------------------------------------------- | --------------------------------------------- |
| **1NF**     | Atomicity, uniqueness, no repeating groups      | Eliminate duplicate data and ensure atomicity |
| **2NF**     | 1NF + full functional dependency on primary key | Remove partial dependencies                   |
| **3NF**     | 2NF + no transitive dependencies                | Remove transitive dependencies                |
| **BCNF**    | 3NF + every determinant is a candidate key      | Handle certain anomalies not covered by 3NF   |
| **4NF**     | BCNF + no multi-valued dependencies             | Eliminate multi-valued dependencies           |
| **5NF**     | 4NF + no join dependencies                      | Ensure data can be reconstructed without loss |

---

## Practical Tips for Normalization

1. **Start with Requirements:**

   - Understand the data requirements and how different entities relate to each other.

2. **Identify Entities and Relationships:**

   - Determine the primary entities and how they interact.

3. **Apply Normal Forms Sequentially:**

   - Start by ensuring 1NF, then proceed to 2NF, and so on.

4. **Use Primary Keys Effectively:**

   - Choose primary keys that uniquely identify records and support normalization.

5. **Balance Normalization with Performance:**

   - Over-normalization can lead to excessive table joins, impacting performance. Sometimes denormalization is necessary for optimization.

6. **Leverage Database Tools:**
   - Utilize ER diagrams and normalization tools to visualize and implement normalization.

---

Let's walk through a complete normalization process from an unnormalized table to BCNF.

**Scenario:**
A university records student enrollments in courses. Each student can enroll in multiple courses, and each course can have multiple students. Additionally, each course is taught by a single instructor, and instructors can teach multiple courses.

**Unnormalized Table:**

| StudentID | StudentName | CourseID | CourseName | InstructorName |
| --------- | ----------- | -------- | ---------- | -------------- |
| S001      | Alice       | C101     | Math       | Dr. Smith      |
| S001      | Alice       | C102     | Physics    | Dr. Brown      |
| S002      | Bob         | C101     | Math       | Dr. Smith      |
| S002      | Bob         | C103     | Chemistry  | Dr. White      |
| S003      | Charlie     | C102     | Physics    | Dr. Brown      |
| S003      | Charlie     | C103     | Chemistry  | Dr. White      |

**Step 1: Convert to 1NF**

Ensure atomicity.

**1NF Table:** (Already atomic; no repeating groups)

| StudentID | StudentName | CourseID | CourseName | InstructorName |
| --------- | ----------- | -------- | ---------- | -------------- |
| S001      | Alice       | C101     | Math       | Dr. Smith      |
| S001      | Alice       | C102     | Physics    | Dr. Brown      |
| S002      | Bob         | C101     | Math       | Dr. Smith      |
| S002      | Bob         | C103     | Chemistry  | Dr. White      |
| S003      | Charlie     | C102     | Physics    | Dr. Brown      |
| S003      | Charlie     | C103     | Chemistry  | Dr. White      |

**Step 2: Convert to 2NF**

Identify partial dependencies (since the primary key is composite: StudentID + CourseID).

**Partial Dependencies:**

- StudentName depends on StudentID.
- CourseName and InstructorName depend on CourseID.

**Create Separate Tables:**

**Students Table:**

| StudentID | StudentName |
| --------- | ----------- |
| S001      | Alice       |
| S002      | Bob         |
| S003      | Charlie     |

**Courses Table:**

| CourseID | CourseName | InstructorName |
| -------- | ---------- | -------------- |
| C101     | Math       | Dr. Smith      |
| C102     | Physics    | Dr. Brown      |
| C103     | Chemistry  | Dr. White      |

**Enrollments Table:**

| StudentID | CourseID |
| --------- | -------- |
| S001      | C101     |
| S001      | C102     |
| S002      | C101     |
| S002      | C103     |
| S003      | C102     |
| S003      | C103     |

**Step 3: Convert to 3NF**

Check for transitive dependencies in the Courses table.

**Functional Dependencies in Courses Table:**

- CourseID → CourseName, InstructorName

Assuming InstructorName depends solely on CourseID, there are no transitive dependencies within the Courses table, as InstructorName is directly dependent on CourseID.

However, if an instructor can teach multiple courses and we have additional attributes about instructors, it might be beneficial to normalize further.

**Assuming Instructors have unique details:**

**Instructors Table:**

| InstructorName | InstructorEmail      |
| -------------- | -------------------- |
| Dr. Smith      | smith@university.edu |
| Dr. Brown      | brown@university.edu |
| Dr. White      | white@university.edu |

**Updated Courses Table:**

| CourseID | CourseName | InstructorName |
| -------- | ---------- | -------------- |
| C101     | Math       | Dr. Smith      |
| C102     | Physics    | Dr. Brown      |
| C103     | Chemistry  | Dr. White      |

**Result:**

- Eliminates any potential transitive dependencies by separating instructor details into their own table.

**Step 4: Convert to BCNF**

Ensure every determinant is a candidate key.

In the **Courses** table:

- CourseID is the primary key.
- InstructorName is dependent on CourseID.
- No non-trivial dependencies where a non-key attribute determines another non-key attribute.

In the **Instructors** table:

- InstructorName is the primary key.
- InstructorEmail depends on InstructorName.

All tables now satisfy BCNF.
