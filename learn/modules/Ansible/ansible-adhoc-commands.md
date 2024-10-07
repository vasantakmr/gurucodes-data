---
title: "ansible adhoc commands"
---

Ansible ad-hoc commands are a quick and efficient way to execute tasks on multiple systems without creating a full-fledged playbook. They are ideal for one-off tasks or simple configurations.

**Syntax:**

ansible -m -a ""

*   **:** Specifies the target hosts. It can be a hostname, IP address, group name, or a pattern using regular expressions.
    
*   **-m :** Specifies the Ansible module to use.
    
*   **-a "":** Specifies the arguments to pass to the module.
    

**Examples:**

1.  ansible all -m pingUse code
    
2.  ansible webserver -m shell -a "df -h"
    
3.  ansible webservers -m service -a "name=apache state=restarted"
    
4.  ansible all -m copy -a "src=/path/to/file dest=/remote/path/to/file"
    

**Additional options:**

*   **-u :** Specifies the username to use for authentication.
    
*   **-k:** Prompts for a password.
    
*   **-i :** Specifies the SSH key to use for authentication.
    
*   **-b:** Enables sudo.
    
*   **-c :** Specifies the connection method (ssh, local, etc.).

**Key points to remember:**

*   Ad-hoc commands are useful for simple, one-time tasks.
    
*   For more complex or recurring tasks, it's recommended to use playbooks.
    
*   Ad-hoc commands can be combined with other Ansible features like groups, roles, and variables.

