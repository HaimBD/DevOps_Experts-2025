locals {
  instance_count = 5
  instance_type  = "t2.micro"
  instance_size  = local.instance_count * 10
}

resource "aws_instance" "example2" {
  count         = local.instance_count
  ami           = "ami-0e86e20dae9224db8"
  instance_type = local.instance_type

  tags = {
    Size = local.instance_size
  }
}