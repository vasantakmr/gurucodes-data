---
title: "Common Git Commands"
---

- `git init`
```bash
  git init
```
Initializes a new Git repository in the current directory. This sets up the necessary Git metadata.

- `git clone [url]`
    
```bash
    git clone https://github.com/user/repo.git 
``` 
Clones a repository from a remote server to your local machine. This creates a full copy of the repository.


-   `git add [file]`
```bash
    `git add index.html` 
```
Stages a file for commit. This prepares the file to be included in the next commit.
    
-   `git commit -m "message"`
    
    ```bash
    `git commit -m "Add new feature to user authentication"` 
    ```
Commits changes with a descriptive message. This creates a snapshot of the staged changes.
    
-   `git status`
    
    ```bash
    
    `git status` 
    ```
Displays the status of changes in your working directory and staging area. It shows which files have been modified, staged, or are untracked.
    
-   `git pull`
    
    ```bash
    
    `git pull origin main` 
    ```
Fetches and merges changes from the remote repository into your local branch. This updates your branch with the latest changes from the remote.
    
-   `git push`
    
    ```bash
    `git push origin main` 
    ```
Uploads your local commits to the remote repository. This shares your changes with other collaborators.

-   `git branch`
    
    ```bash
    
    `git branch new-feature` 
    ```
Lists, creates, or deletes branches. To create a new branch, use `git branch [branch-name]`.
    
-   `git checkout [branch]`
    
    ```bash

    `git checkout new-feature` 
    ```    
Switches to a different branch. Use this command to start working on a new branch.
    
-   `git merge [branch]`
    
    ```bash
    
    `git merge new-feature` 
    ```
Merges changes from the specified branch into the current branch. This integrates the changes from one branch into another.
    
-   `git rebase [branch]`
    
    ```bash
    `git rebase main` 
    ```
Reapplies commits from your current branch on top of another branch. This creates a linear history of changes.
    
-   `git stash`
    
    ```bash
    
    `git stash
    git stash pop` 
    ```
Temporarily saves changes that are not yet ready to be committed. You can apply stashed changes later using `git stash pop`.
    
-   `git cherry-pick [commit]`
    
    ```bash
    
    `git cherry-pick abc1234` 
    ```
Applies the changes from a specific commit onto your current branch. This is useful for applying individual changes without merging entire branches.