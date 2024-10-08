---
title: "Linux Basic Commands"
---
**LINUX Commands**


**Troubleshooting** is crucial for **DevOps engineers** managing Linux environments!


Here’s an expanded list of commonly used troubleshooting commands with more examples:


1.  **dmesg:** Kernel messages for hardware and system errors.

- Example: ```dmesg | grep -i error```
    


1.  **top/htop:** Real-time system resource monitoring.

- Example: ```htop```
    


1.  **free:** Memory usage overview.
    


 — Example: ```free -m```


1.  **df:** Disk space usage analysis.

- Example: ```df -hT```
    


1.  **netstat:** Network connections and routing tables.

- Example: ```netstat -tuln```, ```netstat -s```
    


1.  **ping:** Testing network connectivity.
    


 — Example: ```ping -c 4 google.com```


1.  **traceroute/mtr:** Tracing network routes and latency.

- Example: ```mtr google.com```
    


1.  **ifconfig/ip:** Network interface configuration.

- Example: ```ip addr show```, ```ifconfig -a```
    


1.  **journalctl:** Viewing system logs.
    


 — Example: ```journalctl -u sshd.service```


1.  **lsof:** Checking open files and associated processes.

- Example: ```lsof -i :port\_number```
    


1.  **ps:** Process status and information.
    


 — Example: ```ps 
- Ef | grep process\_name```


1.  **systemctl:** Managing systemd services.

- Example: ```systemctl start/restart/stop service\_name```
    


**13.grep:** Searches for patterns in files.


— Example: grep "pattern" file.txt, grep -r "pattern" directory/


**Here are some Linux commands that are commonly used on a daily basis along with examples:**


1.  **ls:** Lists files and directories in the current directory.

- Example: ```ls```, ```ls -l```, ```ls -a```
    


1.  **cd:** Changes the current directory.
    


 — Example: ```cd Documents```, ```cd ..``` (moves up one directory)


1.  **pwd:** Prints the current working directory.

- Example: ```pwd```
    


1.  **mkdir:** Creates a new directory.

- Example: ```mkdir new\_folder```
    


1.  **rm:** Removes files or directories.

- Example: ```rm file.txt```, ```rm -r directory```
    


1.  **cp:** Copies files or directories.

- Example: ```cp file.txt new\_location/```
    


1.  **mv:** Moves or renames files or directories.
    


 — Example: ```mv file.txt new\_location/```, ```mv old\_name.txt new\_name.txt```


1.  **touch:** Creates a new empty file.

- Example: ```touch new\_file.txt```
    


1.  **grep:** Searches for patterns in files.
    


 — Example: ```grep “pattern” file.txt```, ```grep -r “pattern” directory/```


1.  **cat:** Displays the contents of a file.

- Example: ```cat file.txt```
    


1.  **nano or vim:** Text editors for creating and editing files.

- Example: ```nano file.txt```, ```vim file.txt```
    


1.  **chmod:** Changes file permissions.
    


 — Example: ```chmod +x script.sh``` (gives execute permission to a script)


1.  **sudo:** Executes a command with superuser privileges.

- Example: ```sudo apt update```, ```sudo rm protected\_file```
    


1.  **apt or yum:** Package managers for installing, updating, and removing software packages.
    


 — Example: ```sudo apt install package\_name```, ```sudo yum install package\_name```


1.  **find:** Searches for files in a directory hierarchy.
    


 — Example: ```find . -name “\*.txt”```


**Some other commands along with examples:**


1.  **clear:** Clears the terminal screen.

- Example: ```clear```
    


1.  **man:** Displays the manual pages for a command.

- Example: ```man ls``` (displays the manual for the ```ls``` command)
    


1.  **history:** Displays the command history of the current session.

- Example: ```history```
    


1.  **date:** Prints the current date and time.
    


 — Example: ```date```


1.  **sleep:** Delays execution for a specified amount of time.

- Example: ```sleep 5``` (pauses for 5 seconds)
    


1.  **uptime:** Displays system uptime and load average.

- Example: ```uptime```
    


1.  **whoami:** Prints the current username.
    


 — Example: ```whoami```


1.  **id:** Displays user and group information for the current user or specified user.

- Example: ```id```
    


1.  **groups:** Lists the groups the current user belongs to.
    


 — Example: ```groups```


1.  **passwd:** Allows users to change their passwords.

- Example: ```passwd```
    


1.  **who:** Shows who is logged on.
    


 — Example: ```who```


1.  **last:** Displays a list of last logged in users.

- Example: ```last```
    


1.  **kill:** Sends a signal to terminate a process.

- Example: ```kill PID``` (where PID is the process ID)
    


1.  **cat:** Concatenates and displays the content of files.
- Example: ```cat file.txt```
    


1.  **more:** Displays the content of a file one page at a time.

- Example: ```more file.txt```
    


1.  **rm:** Removes files or directories.
    


 — Example: ```rm file.txt```


1.  **ln:** Creates links between files.

- Example: ```ln -s /path/to/file /path/to/link```
    


1.  **hostname:** Prints or sets the system’s hostname.

- Example: ```hostname```, ```hostname new\_host\_name```
    


These commands are fundamental for managing and interacting with a Linux system. Experiment with them to get familiar with their functionalities!
