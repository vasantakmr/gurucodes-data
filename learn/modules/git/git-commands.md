---
title: "Git Commands"
---

**Top Git Commands with Examples**
==================================

1.  **git init**
    
    *   Initializes a new Git repository.
        
    *   Example: git init
        
2.  **git clone \[repository-url\]**
    
    *   Clones a repository from a URL.
        
    *   Example: git clone
        

https://github.com/user/repo.git

1.  **git status**
    
    *   Shows the working directory status.
        
    *   Example: git status
        
2.  **git add \[file\]**
    
    *   Stages a file for commit.
        
    *   Example: git add file.txt
        
3.  **git commit -m "\[message\]"**
    
    *   Commits staged changes with a message.
        
    *   Example: git commit -m "Initial commit"
        
4.  **git log**
    
    *   Shows the commit history.
        
    *   Example: git log
        
5.  **git diff**
    
    *   Shows differences between working directory and index.
        
    *   Example: git diff
        
6.  **git branch**
    
    *   Lists all branches.
        
    *   Example: git branch
        
7.  **git branch \[branch-name\]**
    
    *   Creates a new branch.
        
    *   Example: git branch feature-branch
        
8.  **git checkout \[branch-name\]**
    
    *   Switches to a different branch.
        
    *   Example: git checkout feature-branch
        
9.  **git merge \[branch-name\]**
    
    *   Merges a branch into the current branch.
        
    *   Example: git merge feature-branch
        
10.  **git pull**
    
    *   Fetches and merges changes from the remote repository.
        
    *   Example: git pull origin main
        
11.  **git push**
    
    *   Pushes changes to the remote repository.
        
    *   Example: git push origin main
        
12.  **git remote -v**
    
    *   Lists remote repositories.
        
    *   Example: git remote -v
        
13.  **git fetch**
    
    *   Fetches changes from the remote repository.
        
    *   Example: git fetch origin
        
14.  **git reset \[file\]**
    
    *   Unstages a file.
        
    *   Example: git reset file.txt
        
15.  **git rm \[file\]**
    
    *   Removes a file from the working directory and staging area.
        
    *   Example: git rm file.txt
        
16.  **git stash**
    
    *   Stashes changes in a dirty working directory.
        
    *   Example: git stash
        
17.  **git stash apply**
    
    *   Applies stashed changes.
        
    *   Example: git stash apply
        
18.  **git tag \[tag-name\]**
    
    *   Creates a new tag.
        
    *   Example: git tag v1.0
        
19.  **git tag -d \[tag-name\]**
    
    *   Deletes a tag.
        
    *   Example: git tag -d v1.0
        
20.  **git rebase \[branch-name\]**
    
    *   Re-applies commits on top of another base tip.
        
    *   Example: git rebase feature-branch
        
21.  **git cherry-pick \[commit-hash\]**
    
    *   Applies the changes from a specific commit.
        
    *   Example: git cherry-pick a1b2c3d
        
22.  **git log --oneline**
    
    *   Shows the commit history in a simplified format.
        
    *   Example: git log --oneline
        
23.  **git log --graph**
    
    *   Displays a graphical representation of the commit history.
        
    *   Example: git log --graph
        
24.  **git log --pretty=format:"%h - %an, %ar : %s"**
    
    *   Customizes the format of log output.
        
    *   Example: git log --pretty=format:"%h - %an,
        

%ar : %s"

1.  **git diff --staged**
    
    *   Shows differences between staged changes and the last commit.
        
    *   Example: git diff --staged
        
2.  **git diff \[branch1\] \[branch2\]**
    
    *   Shows differences between two branches.
        
    *   Example: git diff main feature-branch
        
3.  **git config --global user.name "\[name\]"**
    
    *   Sets the Git username.
        
    *   Example: git config --global user.name "John Doe"
        
4.  **git config --global user.email "\[email\]"**
    
    *   Sets the Git email address.
        
    *   Example: git config --global user.email ["john](mailto:john.doe@example.com).[doe@example.com"](mailto:john.doe@example.com)