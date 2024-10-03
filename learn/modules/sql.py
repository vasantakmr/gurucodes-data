import os 
import json

data = {
    "sql-introduction-to-sql": {
        "title": "Introduction to SQL",
        "description": "Learn the fundamentals of SQL, the standard language for managing and manipulating databases.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-introduction-to-sql",
        "chapters": [
            {
                "name": "What is SQL?",
                "slug": "what-is-sql"
            },
            {
                "name": "History and Evolution",
                "slug": "history-and-evolution"
            },
            {
                "name": "Importance of SQL in Databases",
                "slug": "importance-of-sql"
            },
            {
                "name": "Types of SQL Commands",
                "slug": "types-of-sql-commands"
            },
        ]
    },
    "sql-basic-sql-commands": {
        "title": "Basic SQL Commands",
        "description": "Understand and apply the basic SQL commands for creating databases and manipulating data.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-basic-sql-commands",
        "chapters": [
            {
                "name": "Creating a Database and Tables",
                "slug": "creating-database-and-tables"
            },
            {
                "name":"Data Types",
                "slug":"datatypes"
            },
            {
                "name":"Inserting Data",
                "slug":"inserting-data"
            },
            {
                "name":"Deleting Data",
                "slug":"delete"
            },
            {
                "name":"Selecting Data",
                "slug":"select"
            },
            {
                "name":"Updating Data",
                "slug":"update"
            }
        ]
    },
    "sql-functions-and-operators": {
        "title": "SQL Functions and Operators",
        "description": "Explore the various functions and operators in SQL to perform complex data operations.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-functions-and-operators",
        "chapters": [
            {
                "name": "String Functions",
                "slug": "string-functions"
            },
            {
                "name": "Numeric Functions",
                "slug": "numeric-functions"
            },
            {
                "name": "Date Functions",
                "slug": "date-functions"
            },
            {
                "name": "Operators",
                "slug": "operators"
            },
        ]
    },
    "sql-clauses": {
        "title": "SQL Clauses",
        "description": "Learn about the different clauses in SQL that help in querying and manipulating data effectively.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-clauses",
        "chapters": [
            {
                "name": "WHERE Clause",
                "slug": "where-clause"
            },
            {
                "name": "ORDER BY Clause",
                "slug": "order-by-clause"
            },
            {
                "name": "GROUP BY Clause",
                "slug": "group-by-clause"
            },
            {
                "name": "HAVING Clause",
                "slug": "having-clause"
            },
        ]
    },
    "sql-joins-and-subqueries": {
        "title": "Joins and Subqueries",
        "description": "Master the use of joins and subqueries in SQL to retrieve and manipulate related data across multiple tables.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-joins-and-subqueries",
        "chapters": [
            {
                "name": "INNER JOIN",
                "slug": "inner-join"
            },
            {
                "name": "LEFT JOIN",
                "slug": "left-join"
            },
            {
                "name": "RIGHT JOIN",
                "slug": "right-join"
            },
            {
                "name": "FULL JOIN",
                "slug": "full-join"
            },
            {
                "name": "CROSS JOIN",
                "slug": "cross-join"
            },
            {
                "name": "Single-Row Subqueries",
                "slug": "single-row-subqueries"
            },
            {
                "name": "Multi-Row Subqueries",
                "slug": "multi-row-subqueries"
            },
            {
                "name": "Correlated Subqueries",
                "slug": "correlated-subqueries"
            },
        ]
    },
    "sql-advanced-concepts": {
        "title": "Advanced SQL Concepts",
        "description": "Dive deeper into SQL with advanced concepts like views, indexes, stored procedures, triggers, and transactions.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-advanced-concepts",
        "chapters": [
            {
                "name": "Views",
                "slug": "views"
            },
            {
                "name": "Indexes",
                "slug": "indexes"
            },
            {
                "name": "Stored Procedures",
                "slug": "stored-procedures"
            },
            {
                "name": "Triggers",
                "slug": "triggers"
            },
            {
                "name": "Transactions",
                "slug": "transactions"
            },
        ]
    },
    "sql-performance-tuning-and-optimization": {
        "title": "Performance Tuning and Optimization",
        "description": "Learn how to optimize SQL queries and database structures for better performance.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-performance-tuning-and-optimization",
        "chapters": [
            {
                "name": "Query Optimization",
                "slug": "query-optimization"
            },
            {
                "name": "Database Normalization",
                "slug": "database-normalization"
            },
            {
                "name": "Normal Forms (1NF, 2NF, 3NF, BCNF)",
                "slug": "normal-forms"
            },
            {
                "name": "Common Performance Issues",
                "slug": "common-performance-issues"
            },
        ]
    },
    "sql-security": {
        "title": "SQL Security",
        "description": "Understand the principles of SQL security, including user management, roles, and permissions to protect your databases.",
        "image": "https://gurucodes-data.pages.dev/img/learn/roadmaps/data-analyst/data-analyst-overview.png",
        "slug": "sql-security",
        "chapters": [
            {
                "name": "User Management",
                "slug": "user-management"
            },
            {
                "name": "Roles and Permissions",
                "slug": "roles-and-permissions"
            },
        ]
    },
}

  
def create_folders_and_files(data):
    for folder_name, folder_data in data.items():
        # Create the folder based on the key
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
       
        # Iterate through chapters and create files
        chapters = folder_data.get("chapters", [])
        for chapter in chapters:
            file_name = f"{chapter['slug']}.md"
            file_path = os.path.join(folder_name, file_name)
           
            # Create and write to the file with the required format
            with open(file_path, "w") as file:
                file_content = f"---\ntitle: \"{chapter['name']}\"\n---\n"  # Frontmatter format
                file.write(file_content)
                print(f"File '{file_name}' created in folder '{folder_name}'.")

# Call the function to execute the folder and file creation
create_folders_and_files(data)
