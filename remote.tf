# resource "null_resource" "remote"{
# connection {
#        type = "ssh"
#        user = "ec2-user"
#        private_key = file("/home/surya/Documents/terraform/terraform1/surya.pem")
#        host  = aws_instance.app_server.public_dns
#  }
# }