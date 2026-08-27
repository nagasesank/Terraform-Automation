# resource "null_resource" "remote" {
#   connection {
#     type        = "ssh"
#     user        = "ec2-user"
#     private_key = file("path/to/private-key.pem")
#     host        = aws_instance.app_server.public_dns
#   }
# }
