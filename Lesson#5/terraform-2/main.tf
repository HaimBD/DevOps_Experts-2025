# provider "aws" {
#   region = "us-east-1"
# }
#
# resource "aws_instance" "example-1" {
#   ami           = "ami-020cba7c55df1f615"
#   instance_type = "t2.micro"
# }
#
# output "instance_ip" {
#   value = aws_instance.example-1.public_ip
# }