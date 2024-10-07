---
title: "terraform provisioners"
---
**PROVISIONERS in Terraform**
-----------------------------

Provisioners in Terraform are used to execute scripts on a local or remote machine during the creation or destruction of resources. They are particularly useful for tasks that cannot be accomplished with Terraform’s declarative syntax alone

###### **Types of Provisioners**

1.  **local-exec** **Provisioner:** Executes a command or script on the machine where Terraform is running.

```
resource "null_resource" "example" {
    provisioner "local-exec" {
        command = "echo hello world"
    }
}
```

**null_resource**: This is a special type of resource in Terraform that doesn’t actually create any infrastructure. Instead, it can be used to execute provisioners or manage dependencies.

**"example"**: This is the name of the resource. It’s a reference you can use to refer to this resource within your Terraform configuration.

**local-exec**: This provisioner runs commands on the machine where Terraform is being executed, not on the target infrastructure (e.g., EC2 instances).

**command = "echo Hello, World!"**: This command will be executed by the local-exec provisioner. In this case, it simply prints "Hello, World!" to the console or terminal where Terraform is run.

###### **What This Script Does**

*   When you run terraform apply, Terraform will create the null_resource and execute the local-exec provisioner.
    
*   The local-exec provisioner will run the command echo Hello, World! on your local machine (the machine where Terraform is executed).
    
*   As a result, you will see "Hello, World!" printed to the terminal or console.
    

2.  **remote-exec** **Provisioner:**
    

Executes a command or script on the remote resource being created. Requires SSH or WinRM access to the target machine.

Useful for configuring instances after they are provisioned, such as installing software or setting up services.

```
resource "aws_instance" "web" {
  # ...

  # Establishes connection to be used by all
  # generic remote provisioners (i.e. file/remote-exec)
  connection {
    type     = "ssh"
    user     = "root"
    password = var.root_password
    host     = self.public_ip
  }

  provisioner "remote-exec" {
    inline = [
      "puppet apply",
      "consul join ${aws_instance.web.private_ip}",
    ]
  }
}

```

**remote-exec**: A provisioner that runs commands on the EC2 instance after it has been created.

**inline**: A list of commands to run on the EC2 instance.
    
3.   **​file** **Provisioner:** The file provisioner is used to copy files or directories from the local machine to a remote machine. This is useful for deploying configuration files, scripts, or other assets to a provisioned instance.


```
resource "aws_instance" "web" {
  # ...

  # Copies the myapp.conf file to /etc/myapp.conf
  provisioner "file" {
    source      = "conf/myapp.conf"
    destination = "/etc/myapp.conf"
  }

  # Copies the string in content into /tmp/file.log
  provisioner "file" {
    content     = "ami used: ${self.ami}"
    destination = "/tmp/file.log"
  }

  # Copies the configs.d folder to /etc/configs.d
  provisioner "file" {
    source      = "conf/configs.d"
    destination = "/etc"
  }

  # Copies all files and folders in apps/app1 to D:/IIS/webapp1
  provisioner "file" {
    source      = "apps/app1/"
    destination = "D:/IIS/webapp1"
  }
}

```
**file**: This provisioner copies a file from your local machine to the remote EC2 instance.

*   **source**: The path to the file on your local machine.
    
*   **destination**: The path on the EC2 instance where the file will be placed.
