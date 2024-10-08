---
title: "ansible roles"
---
**Ansible roles** are a powerful mechanism for organizing and reusing tasks and variables within your Ansible playbooks. They provide a modular approach to building complex automation workflows, making your code more manageable, maintainable, and reusable.

**Key components of an Ansible role:**

*   **Tasks:** A list of Ansible tasks that define the actions to be performed.
    
*   **Variables:** A dictionary of variables that can be used within the role.
    
*   **Templates:** Templates that can be used to create files dynamically.
    
*   **Handlers:** Handlers that can be triggered based on specific conditions.
    

**Role structure:**

An Ansible role is typically organized into a directory structure that follows a specific convention:

```
roles/
├── role_name
│ ├── tasks
│ │ ├── main.yml
│ ├── vars
│ │ ├── main.yml
│ ├── templates
│ │ ├── file.j2
│ ├── handlers
│ │ ├── main.yml
│ └── defaults
│ └── main.yml
```

*   **roles/role_name:** The directory containing the role's files.
    
*   **tasks/main.yml:** The main task file for the role.
    
*   **vars/main.yml:** The main variable file for the role.
    
*   **templates/file.j2:** A template file that can be used to create files dynamically.
    
*   **handlers/main.yml:** The main handler file for the role.
    
*   **defaults/main.yml:** The default variable file for the role.
    

**Using roles in playbooks:**

To use a role in a playbook, you simply include the role name in the include_role statement:

```
---
- name: Deploy web server
  hosts: webservers
  roles:
    - webserver
```

*   **Benefits of using Ansible roles:**
    
*   **Modularity:**
    
*   Breaks down complex playbooks into smaller, reusable components.
    
*   **Organization:** Improves code readability and maintainability.
    
*   **Reusability:** Roles can be easily reused across different projects.
    
*   **Version control:** Roles can be version-controlled, making it easy to track changes and manage dependencies.
    
*   **Collaboration:** Facilitates collaboration among teams by promoting code sharing and standardization.
    
*   **Additional features of Ansible roles:**
    
*   **Role dependencies:**
    
*   Roles can depend on other roles, creating a hierarchical structure.
    
*   **Role inheritance:** Roles can inherit variables and tasks from other roles.
    
*   **Role parameters:** Roles can accept parameters, making them more flexible and adaptable.

