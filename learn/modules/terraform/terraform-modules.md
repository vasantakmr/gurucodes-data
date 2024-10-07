---
title: "terraform count and lifecycle"
---
What is a Terraform module?
---------------------------

A _Terraform module_ is a collection of standard configuration files in a dedicated directory. Terraform modules encapsulate groups of resources dedicated to one task, reducing the amount of code you have to develop for similar infrastructure components.

Some say that Terraform modules are a way of extending your present Terraform configuration with existing parts of reusable code reducing the amount of code you have to develop for similar infrastructure components. Others say that the Terraform module definition is a single or many .tf files stacked together in their own directory. Both are correct.

Module blocks can also be used to force compliance on other resources—to deploy databases with encrypted disks, for example. By hard-coding the encryption configuration and not exposing it through variables, you’re making sure that every time the module is used, the disks are going to be encrypted. 

A typical module can look like this:

```
├── main.tf  
├── outputs.tf  
├── README.md  
└── variables.tf
```

As you can see, practically any Terraform configuration is already a module in itself. If you run Terraform in this directory, those configuration files would be considered a **root module**. It means that this configuration is the base of your operation, a core that you can expand further.

### What is the difference between resources and modules in Terraform?

A resource in Terraform describes a piece of infrastructure that is going to be created (e.g., a VPC, a subnet, an ec2 instance, etc), whereas a module is a collection of resources that are used together to achieve a reusable use case.

Types of Terraform modules
--------------------------

Modules are used to create reusable components inside your infrastructure. There are primarily two types of modules depending on how they are written (root and child modules), and depending if they are published or not, we identify two different types as well (local and published).

### Root module

The root module consists of all the resources defined in the _.tf files_ in a Terraform configuration, meaning that all Terraform configurations have their own root module. 

Even if you are simply creating a _main.tf_ that has just a _locals block_ inside of it with a local variable, that is still considered a root module. 

This can be confusing, but keep in mind that every Terraform configuration can become a reusable module for other configurations. Every module can call other modules, and all of the modules called inside another module are considered **child modules**.

### Child module

Calling a child module means to include all the resources defined in that module in the current configuration. This is done by using a module block inside your Terraform configuration:

```
module "webservers" 
{     
    source = "../webservers" 
}   
 ```

You can call the same module as many times as you want and configure it to your liking.

### Local module

A local module is a module that wasn’t published in any registry and when it is sourced, it is using the path to that particular module.

### Published module

A published module refers to a module that has been pushed to a Terraform Registry, or even simply on a VCS and has a tag associated with it. When a published module is sourced, the URL of that module is used either from the registry or from the VCS itself.

When should you use Terraform modules?
--------------------------------------

The short answer to this question is always, but depending on your organization and where you are in the infrastructure as code journey, this may vary.

The best way to think about writing Terraform code is to keep reusability in mind. HCL, being a declarative language, can be very wordy, so repeating the same configuration over and over again will be cumbersome. So usually, if you can, start by defining modules from the beginning and then try to use them as much as possible for maximum reusability. 

If you are just starting with Terraform or IaC in general, you can omit using modules until you get a grasp of how Terraform works.
