#!/usr/bin/env python3
import sys
import subprocess
import time
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if process.returncode != 0:
        print(f"Error executing command: {command}\n{err.decode()}")
        return False
    return True

def run_terraform(terraform_file_path):
    # Initialize Terraform
    print("Initializing Terraform...")
    run_command("terraform init")
    
    # Apply Terraform configuration
    print(f"Applying Terraform file: {terraform_file_path}")
    result = run_command("terraform apply -auto-approve")
    if result:
        print("Terraform applied successfully!")
    else:
        print("Error applying Terraform")


def destroy_terraform():
    # Destroy Terraform resources
    print("Destroying Terraform resources...")
    result = run_command("terraform destroy -auto-approve")
    if result:
        print("Terraform resources destroyed successfully!")
    else:
        print("Error destroying Terraform resources")


def run_ansible(ansible_playbook_path,inventory_script="python.py"):
    # Execute Ansible playbook
    print(f"Running Ansible playbook: {ansible_playbook_path}")
    cmd = ["ansible-playbook", "-i", inventory_script, ansible_playbook_path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("Ansible playbook executed successfully!")
        print(f"Ansible Output:\n {result.stdout}") 
    else:
        print("Error executing Ansible playbook")

if __name__ == "__main__":
    terraform_file_path = "main.tf" 
    ansible_playbook_path = "playbook.yaml" 
    run_terraform(terraform_file_path)
    
    #print(json.dumps(inventory, indent=2))

    run_ansible(ansible_playbook_path)
    
    time.sleep(50)
    destroy_terraform()
