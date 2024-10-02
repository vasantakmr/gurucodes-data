---
title: "Linux Advanced Commands"
---

1.  **File Operations:**
    


*   ls: Lists all fles and directories in the present working directory
    


*   ls -R: Lists fles in sub-directories as well
    


*   ls -a: Shows hidden fles
    


*   ls -al: Lists fles and directories with detailed information like permissions, size, owner, etc.
    


*   cd directoryname: Changes the directory
    


*   cd ..: Moves one level up
    


*   pwd: Displays the present working directory
    


*   cat > filename: Creates a new fle
    


*   cat filename: Displays the fle content
    


*   cat file1 file2 > file3: Joins two fles (fle1 and fle2) and stores the output in a new fle (fle3)
    


*   touch filename: Creates or modifes a fle
    


*   rm filename: Deletes a fle
    


*   cp source destination: Copies fles from the source path to the destination path
    


*   mv source destination: Moves fles from the source path to the destination path
    


*   find / -name filename: Finds a fle or a directory by its name starting from root
    


*   file filename: Determines the fle type
    


*   less filename: Views the fle content page by page
    


*   head filename: Views the frst ten lines of a fle
    


*   tail filename: Views the last ten lines of a fle
    


*   lsof: Shows which fles are opened by which process.
    


*   du -h --max-depth=1: Shows the size of each directory. Use --max-depth=1 to limit the output to the current directory and its immediate children.


*   fdisk: Disk partition manipulation command.
    





1.  **Directory Operations:**
    


*   mkdir directoryname: Creates a new directory in the present working directory
    


*   rmdir directoryname: Deletes a directory
    


*   cp -r source destination: Copies directories recursively
    


*   mv olddir newdir: Renames directories
    


*   find / -type d -name directoryname: Finds a directory starting from root
    


1.  **Process Operations:**
    


*   ps: Displays your currently active processes
    


*   top: Displays all running processes
    


*   kill pid: Kills the process with given pid
    


*   pkill name: Kills the process with the given name
    


*   bg: Resumes suspended jobs without bringing them to foreground
    


*   fg: Brings the most recent job to foreground
    


*   fg n: Brings job n to the foreground
    


*   renice +n \[pid\]: Change the priority of a running process.
    


*   &>filename: Redirects both the stdout and the stderr to the fle flename.
    


*   1>filename: Redirect the stdout to fle flename.
    


*   2>filename: Redirect stderr to fle flename.
    


1.  **File Permissions:**
    


*   chmod octal filename: Change the permissions of fle to octal, which can be between 0 (no permissions) to 7 (full permissions)
    


*   chown ownername filename: Change fle owner
    


*   chgrp groupname filename: Change group owner
    





1.  **Networking:**
    


*   ping host: Ping a host and outputs results
    


*   whois domain: Get whois information for domain
    


*   dig domain: Get DNS information for domain
    


*   netstat -pnltu: Display various network related information such as network connections, routing tables, interface statistics etc.
    


*   ifconfig: Displays IP addresses of all network interfaces
    


*   ssh user@host: Remote login into the host as user
    


*   scp: Transfers fles between hosts over ssh
    


*   wget url: Download fles from the web
    


*   curl url: Sends a request to a URL and returns the response
    


*   traceroute domain: Prints the route that a packet takes to reach the domain.
    


*   mtr domain: mtr combines the functionality of the traceroute and ping programs in a single network diagnostic tool.
    


*   ss: Another utility to investigate sockets. It's a more modern alternative to netstat.
    


*   nmap: Network exploration tool and security scanner.
    


1.  **Archives and Compression:**
    


*   tar cf file.tar files: Create a tar named fle.tar containing fles
    


*   tar xf file.tar: Extract the fles from fle.tar
    


*   gzip file: Compresses fle and renames it to fle.gz
    


*   gzip -d file.gz: Decompresses fle.gz back to fle
    


*   zip -r file.zip files: Create a zip archive named fle.zip
    


*   unzip file.zip: Extract the contents of a zip fle
    


1.  **Text Processing:**
    


*   grep pattern files: Search for pattern in fles
    


*   grep -r pattern dir: Search recursively for pattern in dir
    





*   command | grep pattern: Pipe the output of command to grep for searching
    


*   echo 'text': Prints text
    


*   sed 's/string1/string2/g' filename: Replaces string1 with string2 in flename
    


*   diff file1 file2: Compares two fles and shows the differences
    


*   wc filename: Count lines, words, and characters in a fle
    


*   awk: A versatile programming language for working on fles.
    


*   sed -i 's/string1/string2/g' filename: Replace string1 with string2 in flename. The -i option edits the fle in-place.
    


*   cut -d':' -f1 /etc/passwd: Cut out the frst feld of each line in /etc/passwd, using colon as a feld delimiter.
    


1.  **Disk Usage:**
    


*   df: Shows disk usage
    


*   du: Shows directory space usage
    


*   free: Show memory and swap usage
    


*   whereis app: Show possible locations of app
    


1.  **System Info:**
    


*   date: Show the current date and time
    


*   cal: Show this month's calendar
    


*   uptime: Show current uptime
    


*   w: Display who is online
    


*   whoami: Who you are logged in as
    


*   uname -a: Show kernel information
    


*   df -h: Disk usage in human readable format
    


*   du -sh: Disk usage of current directory in human readable format
    


*   free -m: Show free and used memory in MB
    





1.  **Package Installations:**
    


*   sudo apt-get update: Updates package lists for upgrades
    


*   sudo apt-get upgrade: Upgrades all upgradable packages
    


*   sudo apt-get install pkgname: Install pkgname
    


*   sudo apt-get remove pkgname: Removes pkgname
    


1.  **Others (mostly used in scripts):**
    


*   command1 ; command2: Run command1 and then command2
    


*   command1 && command2: Run command2 if command1 is successful
    


*   command1 || command2: Run command2 if command1 is not successful
    


*   command &: Run command in background
    


1.  **Version Control (Git commands):**
    


*   git init: Initialize a local git repository
    


*   git clone url: Create a local copy of a remote repository
    


*   git add filename: Add a fle to the staging area
    


*   git commit -m "Commit message": Commit changes with a message
    


*   git status: Check the status of the working directory
    


*   git pull: Pull latest changes from the remote repository
    


*   git push: Push changes to the remote repository
    


*   git branch: List all local branches
    


*   git branch branchname: Create a new branch
    


*   git checkout branchname: Switch to a branch
    


*   git merge branchname: Merge a branch into the active branch
    


*   git stash: Stash changes in a dirty working directory
    


*   git stash apply: Apply changes from a stash
    


*   git log: View commit history
    


*   git reset: Reset your HEAD pointer to a previous commit
    


*   git rm filename: Remove a fle from version control
    


*   git rebase: Reapply commits on top of another base tip.
    





*   git revert: Create a new commit that undoes all of the changes made in a particular commit, then apply it to the current branch.
    


*   git cherry-pick commitID: Apply the changes introduced by some existing commits.
    


1.  **Environment Variables:**
    


*   env: Display all environment variables
    


*   echo $VARIABLE: Display the value of an environment variable
    


*   export VARIABLE=value: Set the value of an environment variable
    


*   alias new\_command='old\_command options': Create a new command that executes the old command with the specifed options.
    


*   echo $PATH: Print the PATH environment variable.
    


*   export PATH=$PATH:/new/path: Add /new/path to the PATH.
    


1.  **Job Scheduling (Cron Jobs):**
    


*   crontab -l: List all your cron jobs
    


*   crontab -e: Edit your cron jobs
    


*   crontab -r: Remove all your cron jobs
    


*   crontab -v: Display the last time you edited your cron jobs
    


*   crontab file: Install a cron job from a fle
    


*   @reboot command: Schedule a job to run at startup
    


1.  **Package Installations (using pip, a Python package installer):**
    


*   pip install packagename: Install a Python package.
    


*   pip uninstall packagename: Uninstall a Python package.
    


*   pip freeze > requirements.txt: Freeze the installed packages into a requirements fle.
    


*   pip install -r requirements.txt: Install packages from a requirements fle.
    





1.  **Shell Scripting:**
    


*   #!/bin/bash: Shebang line to specify the script interpreter.
    


*   $0, $1, ..., $9, ${10}, ${11}: Script arguments.
    


*   if \[condition\]; then ... fi: if statement in bash scripts.
    


*   for i in {1..10}; do ... done: for loop in bash scripts.
    


*   while \[condition\]; do ... done: while loop in bash scripts.
    


*   function name() {...}: Defne a function.
    


1.  **System Monitoring and Performance:**
    


*   iostat: Reports Central Processing Unit (CPU) statistics and input/output statistics for devices, partitions, and network flesystems.
    


*   vmstat: Reports information about processes, memory, paging, block IO, traps, disks, and CPU activity.
    


*   htop: An interactive process viewer for Unix systems. It's a more user-friendly alternative to top.
    


1.  **Search and Find:**
    


*   locate filename: Find a fle by its name. The database updated by updatedb command.
    


*   whereis programname: Locate the binary, source, and manual page fles for a command.
    


*   which commandname: Shows the full path of (shell) commands.
    


1.  **Compression / Archives:**
    


*   tar -cvf archive.tar dirname/: Create a tar archive.
    


*   tar -xvf archive.tar: Extract a tar archive.
    


*   tar -jcvf archive.tar.bz2 dirname/: Create a compressed bz2 archive.
    


*   tar -jxvf archive.tar.bz2: Extract a bz2 archive.
    





1.  **Disk Usage:**
    


*   dd if=/dev/zero of=/tmp/output.img bs=8k count=256k: Create a fle of a certain size for testing disk speed.
    


*   hdparm -Tt /dev/sda: Measure the read speed of your hard drive.
    


1.  **Others:**
    


*   yes > /dev/null &: Use this command to push a system to its limit.
    


*   :(){ :|:& };:: A fork bomb – handle with care. Do not run this command on a production system.
    


Remember, you can always use the man command (e.g. man ls) to get more information about each command.



