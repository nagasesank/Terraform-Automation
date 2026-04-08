# Terraform Automation for AWS and Ansible

This project demonstrates an end-to-end infrastructure automation workflow using Terraform, Ansible, and Python. It provisions an AWS EC2 instance, prepares dynamic inventory for Ansible, runs a configuration playbook, and then tears the infrastructure down.

## Overview

The repository is built as a simple automation pipeline:

1. Terraform initializes and creates AWS resources.
2. A Python inventory script reads Terraform output.
3. Ansible connects to the provisioned host and applies configuration.
4. The Python orchestration script destroys the infrastructure after execution.

This makes the project a useful example of combining infrastructure as code with configuration management in one workflow.

## What This Project Does

- Provisions an EC2 instance in AWS using Terraform
- Creates a security group that allows SSH access
- Generates inventory data for Ansible from Terraform output
- Runs an Ansible playbook against the provisioned instance
- Demonstrates short-lived infrastructure automation from one command

## Tech Stack

- Terraform
- Ansible
- Python 3
- AWS EC2

## Repository Structure

```text
.
|-- auto_ec2.py          # Orchestrates terraform apply, ansible execution, and terraform destroy
|-- main.tf              # Core Terraform resources for AWS infrastructure
|-- outputs.tf           # Terraform outputs used by the inventory script
|-- python.py            # Generates dynamic inventory from terraform output
|-- playbook.yaml        # Ansible playbook executed against the EC2 instance
|-- remote.tf            # SSH connection configuration example
|-- varibales.tf         # Terraform variables used by the deployment
`-- inventory.ini        # Generated local inventory file
```

## Prerequisites

Before running the project, make sure you have:

- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed
- [Ansible](https://docs.ansible.com/) installed
- Python 3 installed
- An AWS account with credentials configured locally
- An EC2 key pair available for SSH access
- The matching `.pem` file stored in the project directory

## Configuration

Update the project to match your AWS environment before running it:

- Review `main.tf` for region, AMI, instance type, and key pair name
- Confirm the private key filename referenced in the Terraform and inventory files
- Make sure your AWS credentials are configured with the permissions needed to create EC2 resources
- Review `playbook.yaml` and adapt the software installation steps if needed

## How It Works

The main workflow lives in `auto_ec2.py`.

- `terraform init` prepares the working directory
- `terraform apply -auto-approve` provisions the infrastructure
- `ansible-playbook -i python.py playbook.yaml` runs the Ansible playbook
- `terraform destroy -auto-approve` removes the resources after the run

## Usage

Clone the repository and move into the project directory:

```bash
git clone https://github.com/nagasesank/Terraform-Automation.git
cd Terraform-Automation
```

Run the automation script:

```bash
python3 auto_ec2.py
```

## Example Use Case

This repository is useful as a learning and portfolio project for:

- automating AWS infrastructure provisioning
- combining Terraform and Ansible in one workflow
- demonstrating cloud automation skills in a practical setup
- testing repeatable configuration changes on short-lived infrastructure

## Notes

- The current workflow destroys the infrastructure after the Ansible playbook completes
- Review security group rules before using this in a wider environment
- Avoid committing sensitive files such as private keys or real Terraform state in production projects

## Improvements to Consider

- Add variable validation and parameterization for AMI, region, and instance type
- Move secrets handling to environment variables or secure secret storage
- Add a `.gitignore` for Terraform state and private key files
- Add screenshots or sample output for the provisioning workflow
- Add GitHub Actions for linting or validation

## Contributing

Contributions, issues, and suggestions are welcome. If you would like to improve the automation flow, documentation, or Terraform structure, feel free to open an issue or submit a pull request.
