---
title: "ansible setup and playbooks"
---
An Ansible playbook is a configuration management file written in YAML format that defines a series of tasks to be executed on one or more target systems. It provides a structured and reusable way to automate IT workflows.

**Key components of an Ansible playbook:**

*   **Hosts:** Defines the target systems or groups of systems.
    
*   **Tasks:** Specifies the actions to be performed on the target systems.
    
*   **Variables:** Stores data that can be used throughout the playbook.
    
*   **Templates:** Creates files dynamically based on templates and variables.
    
*   **Handlers:** Defines actions to be triggered based on specific conditions.
    

**Example playbook:**

YAML


```
---  
- name: Install Apache web server    hosts: webservers    
tasks:      
  - name: Ensure Apache installed        
    apt: name=apache2 state=present      
  - name: Start Apache service             service: name=apache2 state=started
```

**Explanation:**

*   **Hosts:** Specifies the group of hosts named "webservers".
    
*   **Tasks:** Defines two tasks:
    
    *   Installs the Apache web server package using the apt module.
        
    *   Starts the Apache service using the service module.
        

**Key benefits of using Ansible playbooks:**

*   **Automation:** Automates repetitive tasks, saving time and effort.
    
*   **Consistency:** Ensures that systems are configured consistently across different environments.
    
*   **Idempotency:** Guarantees that changes are applied only once, even if a playbook is run multiple times.
    
*   **Reusability:** Playbooks can be reused and shared across different projects.
    
*   **Version control:** Playbooks can be version-controlled, making it easy to track changes and revert to previous states.
    

**Additional features of Ansible playbooks:**

*   **Roles:** Modularize playbooks by organizing tasks and variables into reusable units.
    
*   **Includes:** Include other playbooks or roles within a main playbook.
    
*   **Loops:** Iterate over lists of items and perform tasks on each item.
    
*   **Conditionals:** Execute tasks based on specific conditions.
    
*   **Callbacks:** Trigger custom actions based on events.