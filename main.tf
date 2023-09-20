terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-north-1"
}

resource "aws_security_group" "my_sec_grp" {
  name = "my_sec_grp"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "app_server" {
  # ami           = var.ami_id
  ami           = "ami-0c147c2e2b026f094"
  instance_type = "t3.micro"
  key_name = "ec2-user"
  security_groups = ["${aws_security_group.my_sec_grp.name}"]
  tags = {
    Name = var.instance_name
  }
}
resource "null_resource" "remote"{
connection {
       type = "ssh"
       user = "ec2-user"
       private_key = file("/home/surya/Documents/terraform/terraform1/ec2-user.pem")
       host  = aws_instance.app_server.public_dns
 }
}
resource "null_resource" "ansible_inventory" {
  depends_on = [aws_instance.app_server]

  provisioner "local-exec" {
    command = "echo '[all]' > inventory.ini && echo 'ansible_user=ec2-user' >> inventory.ini && echo '${aws_instance.app_server.public_dns}' >> inventory.ini"
  }

  triggers = {
    instance_id = aws_instance.app_server.id
  }
}

