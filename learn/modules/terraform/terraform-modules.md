---
title: "terraform count and lifecycle"
---

**What are Terraform Modules?**

Think of Terraform modules as pre-built LEGO sets. They're reusable blocks of infrastructure code that you can plug and play into your main Terraform configuration. This helps you:

*   **Organize your code:** Break down complex infrastructure into smaller, manageable parts.
    
*   **Reuse code:** Avoid writing the same code multiple times, saving time and reducing errors.
    
*   **Share code:** Share modules with others or publish them to public registries.
    
**Creating a Module**

1.  **Create a new directory:** This will be the root of your module for example ec2 directory.
    
2.  **Create a main.tf file:** This is where you'll define the resources and variables that make up your module.
    
3.  **Define variables (optional):** Use variable blocks to accept input values from your main configuration.
    
4.  **Define resources:** Use resource blocks to define the infrastructure components you want to create.
    
**Example Module (Creating an EC2 instance):**

Terraform

## main.tf  

```
variable "ami" 
{    type        = string    
description = "AMI ID of the EC2 instance"  
}  
variable "instance_type" 
{    
    type        = string    
    description = "Instance type of the EC2 instance"     
}  
resource "aws_instance" "example" {    ami           = var.ami    
instance_type = var.instance_type  
}  

```

**Using a Module in Your Main Configuration**

1.  **Add the module to your main configuration:** Use the module block to reference your module.
    
2.  **Provide input values:** Pass the required values for your module's variables.
    

**Example Main Configuration:**

```
module "ec2_instance" 
{    
  source = "./modules/ec2"    
  ami           = "ami-0c55b159cbfafe1f0"    instance_type = "t2.micro"  
}  
```

**Benefits of Using Modules**

*   **Modularity:** Break down complex infrastructure into smaller, manageable parts.
    
*   **Reusability:** Avoid writing the same code multiple times, saving time and reducing errors.
    
*   **Shareability:** Share modules with others or publish them to public registries.
    
*   **Version Control:** Track changes to modules and manage different versions.
    
*   **Maintainability:** Easier to update and manage modules compared to modifying a large main configuration.
    

By using Terraform modules, you can create more organized, efficient, and reusable infrastructure code.