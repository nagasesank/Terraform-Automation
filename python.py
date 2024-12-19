#!/usr/bin/env python3

import json
import subprocess

def get_terraform_output():
    cmd = 'terraform output -json'
    output = subprocess.check_output(cmd.split()).decode('utf-8')
    return json.loads(output)

def create_ansible_inventory(tf_output):
    ip = tf_output['instance_public_ip']['value']

    inventory = {
        "aws_instance": {
            "hosts": [ip],
            "vars": {
                "ansible_ssh_user": "ec2-user",
                "ansible_ssh_private_key_file": "ec2-user.pem"
            }
        }
    }
    return inventory

if __name__ == '__main__':
    tf_output = get_terraform_output()
    inventory = create_ansible_inventory(tf_output)
    print(json.dumps(inventory, indent=2))


