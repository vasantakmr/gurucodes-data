---
title: "ansible handlers & notifiers"
---

Ansible notifiers and handlers are powerful mechanisms that allow you to trigger custom actions based on specific conditions within your playbooks. They provide flexibility and control over how your automation tasks are executed.

**Notifiers:**

*   Notifiers are used to send notifications about the status of your playbook execution.
    
*   They can be configured to send notifications through various channels, such as email, SMS, Slack, or custom scripts.
    
*   Notifiers are typically triggered when a playbook starts, completes successfully, or fails.
    
*   You can define multiple notifiers within a playbook to send notifications to different recipients or through different channels.
    

**Handlers:**

*   Handlers are used to define custom actions that can be triggered based on specific conditions within a playbook.
    
*   They are typically triggered when a task changes the state of a system, such as creating a file, restarting a service, or modifying a configuration.
    
*   Handlers can perform a variety of actions, such as sending notifications, running scripts, or executing other Ansible tasks.
    
*   You can define multiple handlers within a playbook and associate them with specific tasks or conditions.


### Make sure index.html file is present at path given

```
---
- name: Simple Apache Setup hosts: webservers
  become: yes
  vars:
   apache_package: apache2 
   apache_service: apache2 
   web_content: /var/www/html/index.html
   web_content_src: /home/ubuntu/index.html
   tasks:
   - name: Install Apache 
     apt:
      name: "{{ apache_package }}" 
      state: present

   - name: Deploy web content 
     copy:
      src: "{{ web_content_src }}" 
      dest: "{{ web_content }}" 
      notify: Restart Apache

handlers:
 - name: Restart Apache 
   service:
     name: "{{ apache_service }}" 
     state: restarted
```



