---
title: "Linux Basic Commands"
---
**LINUX Commands**


_**Troubleshooting**_ is crucial for _**DevOps engineers**_ managing Linux environments!


Here’s an expanded list of commonly used troubleshooting commands with more examples:


1.  _**dmesg:**_ Kernel messages for hardware and system errors.  — Example: \`dmesg | grep -i error\`
    


1.  _**top/htop:**_ Real-time system resource monitoring.  — Example: \`htop\`
    


1.  _**free:**_ Memory usage overview.
    


 — Example: \`free -m\`


1.  _**df:**_ Disk space usage analysis.  — Example: \`df -hT\`
    


1.  _**netstat:**_ Network connections and routing tables.  — Example: \`netstat -tuln\`, \`netstat -s\`
    


1.  _**ping:**_ Testing network connectivity.
    


 — Example: \`ping -c 4 google.com\`


1.  _**traceroute/mtr:**_ Tracing network routes and latency.  — Example: \`mtr google.com\`
    


1.  _**ifconfig/ip:**_ Network interface configuration.  — Example: \`ip addr show\`, \`ifconfig -a\`
    


1.  _**journalctl:**_ Viewing system logs.
    


 — Example: \`journalctl -u sshd.service\`


1.  _**lsof:**_ Checking open files and associated processes.  — Example: \`lsof -i :port\_number\`
    


1.  _**ps:**_ Process status and information.
    


 — Example: \`ps -ef | grep process\_name\`


1.  _**systemctl:**_ Managing systemd services.  — Example: \`systemctl start/restart/stop service\_name\`
    


_**13.grep:**_ Searches for patterns in files.


— Example: grep "pattern" file.txt, grep -r "pattern" directory/


**Here are some Linux commands that are commonly used on a daily basis along with examples:**


1.  _**ls:**_ Lists files and directories in the current directory.  — Example: \`ls\`, \`ls -l\`, \`ls -a\`
    


1.  _**cd:**_ Changes the current directory.
    


 — Example: \`cd Documents\`, \`cd ..\` (moves up one directory)


1.  _**pwd:**_ Prints the current working directory.  — Example: \`pwd\`
    


1.  _**mkdir:**_ Creates a new directory.  — Example: \`mkdir new\_folder\`
    


1.  _**rm:**_ Removes files or directories.  — Example: \`rm file.txt\`, \`rm -r directory\`
    


1.  _**cp:**_ Copies files or directories.  — Example: \`cp file.txt new\_location/\`
    


1.  _**mv:**_ Moves or renames files or directories.
    


 — Example: \`mv file.txt new\_location/\`, \`mv old\_name.txt new\_name.txt\`


1.  _**touch:**_ Creates a new empty file.  — Example: \`touch new\_file.txt\`
    


1.  _**grep:**_ Searches for patterns in files.
    


 — Example: \`grep “pattern” file.txt\`, \`grep -r “pattern” directory/\`


1.  _**cat:**_ Displays the contents of a file.  — Example: \`cat file.txt\`
    


1.  _**nano or vim:**_ Text editors for creating and editing files.  — Example: \`nano file.txt\`, \`vim file.txt\`
    


1.  _**chmod:**_ Changes file permissions.
    


 — Example: \`chmod +x script.sh\` (gives execute permission to a script)


1.  _**sudo:**_ Executes a command with superuser privileges.  — Example: \`sudo apt update\`, \`sudo rm protected\_file\`
    


1.  _**apt or yum:**_ Package managers for installing, updating, and removing software packages.
    


 — Example: \`sudo apt install package\_name\`, \`sudo yum install package\_name\`


1.  _**find:**_ Searches for files in a directory hierarchy.
    


 — Example: \`find . -name “\*.txt”\`


**Some other commands along with examples:**


1.  _**clear:**_ Clears the terminal screen.  — Example: \`clear\`
    


1.  _**man:**_ Displays the manual pages for a command.  — Example: \`man ls\` (displays the manual for the \`ls\` command)
    


1.  _**history:**_ Displays the command history of the current session.  — Example: \`history\`
    


1.  _**date:**_ Prints the current date and time.
    


 — Example: \`date\`


1.  _**sleep:**_ Delays execution for a specified amount of time.  — Example: \`sleep 5\` (pauses for 5 seconds)
    


1.  _**uptime:**_ Displays system uptime and load average.  — Example: \`uptime\`
    


1.  _**whoami:**_ Prints the current username.
    


 — Example: \`whoami\`


1.  _**id:**_ Displays user and group information for the current user or specified user.  — Example: \`id\`
    


1.  _**groups:**_ Lists the groups the current user belongs to.
    


 — Example: \`groups\`


1.  _**passwd:**_ Allows users to change their passwords.  — Example: \`passwd\`
    


1.  _**who:**_ Shows who is logged on.
    


 — Example: \`who\`


1.  _**last:**_ Displays a list of last logged in users.  — Example: \`last\`
    


1.  _**kill:**_ Sends a signal to terminate a process.  — Example: \`kill PID\` (where PID is the process ID)
    


1.  _**cat:**_ Concatenates and displays the content of files.  — Example: \`cat file.txt\`
    


1.  _**more:**_ Displays the content of a file one page at a time.  — Example: \`more file.txt\`
    


1.  _**rm:**_ Removes files or directories.
    


 — Example: \`rm file.txt\`


1.  _**ln:**_ Creates links between files.  — Example: \`ln -s /path/to/file /path/to/link\`
    


1.  _**hostname:**_ Prints or sets the system’s hostname.  — Example: \`hostname\`, \`hostname new\_host\_name\`
    


These commands are fundamental for managing and interacting with a Linux system. Experiment with them to get familiar with their functionalities!
