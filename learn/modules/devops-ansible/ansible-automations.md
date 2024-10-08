---
title: "Ansible:A to Z of Automations"
---


### Install Ansible on EC2 instance - 
**yum install ansible -y**

### Automation1 - Play to install apache apache_install.yml 

**ansible-playbook apache_install.yml**

```
---
- name: Ensure web server is installed 
  hosts: demo
  become: yes 
  tasks:
    - name: Install Apache 
      apt:
       name: apache2 
       state: present 
      when: ansible_os_family == "Debian"


    - name: Ensure Apache is running 
      service:
        name: apache2 
        state: started
        enabled: yes
```

### Automation2 - Play to copy files copy_files.yml 

**ansible-playbook copy_files.yml**

```
---
- name: Copy file and create user dev grp
  hosts: webservers
  become: yes # Ensure the task runs sudo 
  tasks:
    - name: Copy file to remote host 
      copy:
        src: /home/ubuntu/myfile.txt dest: /home/ubuntu/myfile.txt owner: codedale
        group: dev 
        mode: '0644' 
        backup: true
```

### Automation3 - Play to copy files copy_files.yml 

**ansible-playbook copy_files.yml**

Make sure the user is created in node

```
---
- name: create the file in remote servers
  hosts: webservers
  become: yes 
  tasks:
    - name: create file file:
      path: /home/ubuntu/new_file.txt state: absent
      owner: codedale 
      group: codedale
      mode: u=rwx,g=r,o=r

    - name: create directory file:
      path: /home/ubuntu/playbookfiles state: directory
```

### Automation4 - Play to copy files cron.yml 

**ansible-playbook cron.yml**

```
create test.sh file in node
test.sh
#!/bin/bash
echo “hello buddy”
touch testfile
give execute permissions
sudo chmod u+x test.sh
```

```
---
- name: cron jobs 
  hosts: webservers 
  tasks:
    - name: cron jobs 
      cron:
        name: cron job for remote server
        minute: 30
        hour: 18
        day: 15 
        month: "*" 
        weekday: "*"
        job: /home/ubuntu/test.sh
```

### Automation5 - Play to copy files download.yml 

**ansible-playbook download.yml**

```
---
- name: Downlaod files
  hosts: all
  tasks:
    - name: Download file
      get_url:
      url: https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tar.xz
      dest: /tmp/script/
      owner: appu
      group: appu
      mode: 0777
 ```
### Automation6 - Play with variables files variables.yml 

**ansible-playbook variables.yml**

```
---
- name: Install and configure Apache 
  hosts: webservers
  become: yes
  vars:
   apache_package: apache2
   apache_service: apache2
  tasks:
    - name: Ensure Apache is insalled
     apt:
      name: "{{ apache_package }}"
      state: present
      update_cache: yes
    - name: Ensure Apache started
      service:
        name: "{{ apache_service }}"
        state: started
        enabled: yes
```
