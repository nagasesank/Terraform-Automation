# Automation Of AWS Using Terraform and Ansible using Python
This repository provides tools and playbooks to automate [Terraform](https://www.terraform.io/) operations using [Ansible](https://www.ansible.com/).

## Overview
With the combination of Terraform's infrastructure as code (IaC) and Ansible's configuration management capabilities, this repository aims to simplify and automate infrastructure provisioning and management tasks.

## Features

1. **Automated Infrastructure Deployment**: Use Ansible playbooks to execute Terraform plans and apply configurations.
2. **State Management**: Handle Terraform state files securely.
3. **Configuration**: Utilize Ansible's templating for dynamic Terraform configurations.
4. **Validation & Testing**: Integrate with tools like tflint for configuration validation.

## Prerequisites
1. [Terraform](https://www.terraform.io/) installed.
2. [Ansible](https://www.ansible.com/). installed.
3. Create *Access Key* and *Sceret key* from Your AWS Console Management. you can create here [AWS Console](https://portal.aws.amazon.com/billing/signup#/start/email)
4. Create Public/Private key pair to make ssh to the **AWS Console**
5. Create a *Playbook.yaml* file to run the configuration in the EC2 Instance.
6. No Need to Create *inventory.ini* to ansible configuration file. It will automate the hosts that comes from the EC2 instance.

## Installation

- Clone this repository:
   - git clone https://github.com/nagasesank/Terraform-Automation.git
- Navigate to the project directory:
   - cd Terraform_Ansible_Automation

## Note:
* Before Going to run the script make sure you *.pem* file should be download into the same folder.
* Make sure the permissions are proper for the *.pem* file.

## Usage
Make sure you've set up necessary authentication for Terraform providers (e.g., AWS CLI configured for AWS provider).
1. **Set up Terraform variables**: Edit the *variables.tf* or respective variable files as per your infrastructure requirements.
2. **Execute** the auto_ec2.py to run the file using the command
<pre><code>$ python3 auto_ec2.py </code></pre>


## References
- [Medium Reference ](https://medium.com/geekculture/the-most-simplified-integration-of-ansible-and-terraform-49f130b9fc8)
- Refer to individual playbook and script documentation for detailed usage and customization options.

## Contributing
* Contributions, issues, and feature requests are welcome! For major changes, please open an issue first to discuss the proposed change.
