variable "environment" {
  default = "dev"
}

locals {
  instance_type = var.environment == "prod" ? "t2.medium" : "t2.micro"
}

resource "aws_instance" "example" {
  ami           = "ami-0e86e20dae9224db8"
  instance_type = local.instance_type

  tags = {
    Name = "${var.environment}-instance"
  }
}
