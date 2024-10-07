---
title: "terraform state file"
---
**Terraform State**

##### **What is Terraform State :**

state of your infrastructure as defined by your Terraform configuration files. This state file, typically named _**“terraform.tfstate”**_, contains information about the resources you’ve created, their current status, and any dependencies between them.

##### **Importance of Terraform State file :**

1.  **Resource Tracking**: Terraform state files keep track of all the resources managed by Terraform, including their IDs and attributes. This helps Terraform understand what is currently deployed and how it maps to the configuration files.
    
2.  **Change Management**: When you run commands like terraform apply, Terraform compares the desired state (from your configuration files) to the actual state (from the state file). It then determines what changes need to be made to align the actual state with the desired state.
    
3.  **Efficient Operations**: By maintaining a state file, Terraform can perform operations more efficiently. It avoids querying the cloud provider or other services for information about existing resources, which speeds up operations.
    
4.  **Collaboration**: In a team environment, the state file can be stored remotely (e.g., in an S3 bucket, Azure Blob Storage, etc.) to allow multiple people to work on the same infrastructure and ensure they are working with the same state.
    
5.  **Resource Metadata**: The state file contains metadata about resources, which is used by Terraform to manage dependencies and understand how resources are related.
    

State files are often stored locally by default, but in a collaborative setting or in production environments, they are usually stored in a remote backend for better reliability and consistency.

##### **Drawbacks of Terraform State file :**

1.  **Security Risks**: It might contain sensitive data like resource IDs or secrets, which can be risky if not protected.
    
2.  **Corruption Risk**: If the state file gets corrupted, it can cause problems with managing your resources.
    
3.  **Complex to Manage**: Making manual changes to the state file can be tricky and error-prone.
    
4.  **Sync Issues**: When using a remote state file, multiple users or processes might cause conflicts if not properly synchronized.
    
5.  **Performance Problems**: Very large state files can slow down Terraform operations.
    
6.  **Version Control**: Tracking changes and recovering from mistakes can be difficult if the state file isn't properly backed up or versioned.
    
7.  **Backup Needs**: Without proper backups, recovering from accidental deletions or corruption can be hard.
    

**How to Overcome the Drawbacks of Terraform State file :**

#### **State locking in Terraform:**

Terraform state locking is a feature that helps prevent multiple people from making changes to your infrastructure at the same time, which could cause conflicts or corruption.

**What it does:** When you run commands (like terraform apply or terraform plan), that change your infrastructure, Terraform locks the state file. This means no one else can make changes until the lock is released.

**Why it’s important:** It ensures that only one set of changes is applied at a time, keeping your infrastructure consistent and preventing errors.

**How it works:** The lock is automatically applied when you run commands (like terraform apply or terraform plan). If someone else tries to run these commands while the state is locked, they’ll have to wait until the lock is released.

**Unlocking:** The lock is usually released automatically when the command finishes. If something goes wrong and the lock isn’t released, you can manually unlock it using the _**“terraform force-unlock”**_ command.

