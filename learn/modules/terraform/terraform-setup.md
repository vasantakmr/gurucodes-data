---
title: "Create resources in two regions terraform setup"
---

### **How Terraform will create resources in multi-region**

Terraform can manage resources across multiple regions by configuring the provider

blocks and specifying the regions where resources should be created.

1.  **Define Multiple Providers**
    
You need to define multiple provider blocks in your Terraform configuration file, each specifying a different region. Here’s an example for AWS:

```
provider "aws" 
{ 
    alias = "us_east_1"
    region = "us-east-1"
}
provider "aws" 
{ 
    alias = "us_west_1"
    region = "us-west-1"
}   
```

In this example, two providers are defined: one for the us-east-1 region and another for the us-west-1 region. You can make use of alias keyword to implement multi region infrastructure setup in terraform.

1.  **Specify Providers in Resource Definitions**
    

When defining resources, you need to specify which provider should be used. This is done using the provider argument within the resource block:

```
resource "aws_instance" "example_us_east" {
  provider = aws.us_east_1
  ami           = "ami-05cddo*****"
  instance_type = "t2.micro"
}

resource "aws_instance" "example_us_west" {
  provider = aws.us_west_1
  ami           = "ami-05cddo*****"
  instance_type = "t2.micro"
}

```

In this configuration:

*   The aws_instance.example_us_east resource will be created in the
    

us-east-1 region.

*   The aws_instance.example_us_west resource will be created in the
    
us-west-1 region.

1.  **Initialize and Apply**
    
After configuring the providers and resources, initialize your Terraform workspace and apply the configuration:

terraform init

terraform apply

Terraform will create resources in the specified regions based on your configuration.

###### **Summary**

*   **Define multiple providers**: Create separate provider blocks for each region you need.
    

**Reference providers in resources**: Use the provider argument within resource blocks to specify which provider (and thus which region) to use.

