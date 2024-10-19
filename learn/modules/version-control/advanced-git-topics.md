---
title: "Advanced Git Topics"
---

-   **Rebase:** Rewriting commit history to create a linear project history can simplify the understanding of the commit history. Rebasing is often used to integrate changes from the main branch into a feature branch.
    
    ```bash
    `git rebase main` 
    ```
    _Example:_ Update your feature branch with the latest changes from the `main` branch.
    
-   **Cherry-pick:** This allows you to apply changes from a specific commit from another branch, enabling selective integration of changes.
    
    ```bash
    
    `git cherry-pick abc1234` 
    ```
    _Example:_ Apply a bug fix from a different branch without merging all changes.
    
-   **Stashing:** Save your work-in-progress changes temporarily and apply them later. This is useful when you need to switch branches or work on something else without losing your current changes.
    
    ```bash
    `git stash
    git stash pop` 
    ```
    _Example:_ Save changes, switch to a different branch, and then reapply the saved changes.
    
-   **Interactive Rebase:** Allows you to edit, reorder, and squash commits. This is useful for cleaning up commit history before merging a feature branch.
    
    ```bash
    `git rebase -i main` 
    ```
    _Example:_ Reorder or combine commits to create a cleaner commit history.

### Real-Life Example of Git in a Project

    Consider a development team working on a complex web application:

1.  **Project Initialization:**
    
    -   The team initializes a Git repository with `git init` and creates a remote repository on GitHub.
2.  **Feature Development:**
    
    -   A developer creates a new branch for a feature, e.g., `git branch feature/payment-integration`.
    -   They switch to this branch (`git checkout feature/payment-integration`) and implement the payment integration feature.
3.  **Staging and Committing:**
    
    -   After implementing the feature, the developer stages changes (`git add .`) and commits them (`git commit -m "Integrate payment gateway"`).
4.  **Integrating Changes:**
    
    -   The developer switches back to the `main` branch (`git checkout main`) and merges the feature branch (`git merge feature/payment-integration`).
5.  **Collaboration:**
    
    -   The developer pushes the changes to the remote repository (`git push origin main`), allowing other team members to review and collaborate.
6.  **Handling Conflicts:**
    
    -   If conflicts arise during merging, Git highlights them. The developer manually resolves the conflicts, stages the resolved files, and commits the changes.
7.  **Version Control and Rollback:**
    
    -   If a new feature introduces a bug, the team can roll back to a previous stable commit using `git revert` or check out a previous commit to restore a stable version.