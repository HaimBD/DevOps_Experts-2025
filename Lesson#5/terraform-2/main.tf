provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0e86e20dae9224db8"
  instance_type = "t2.micro"
}

output "instance_ip" {
  value = aws_instance.example.public_ip
}
