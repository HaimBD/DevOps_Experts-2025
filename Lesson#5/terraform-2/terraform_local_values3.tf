variable "environment" {
  default = "dev"
}
locals {
  env_prefix = "${var.environment}-app"
}

resource "aws_instance" "example3" {
  ami           = "ami-0e86e20dae9224db8"
  instance_type = "t2.micro"

  tags = {
    Name = local.env_prefix
  }
}