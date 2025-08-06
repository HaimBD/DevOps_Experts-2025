provider "aws" {
  region = "us-east-1"
}
# variable "instance_tags" {
#   type        = map(string)
#   default     = {
#     Environment = "dev"
#     Owner       = "team"
#   }
#   description = "Tags to be applied to instances"
# }
# resource "aws_instance" "example" {
#   ami           = "ami-0e86e20dae9224db8"
#   instance_type = "t2.micro"
#
#   tags = var.instance_tags
# }
