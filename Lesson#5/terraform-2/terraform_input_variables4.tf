variable "instance_config" {
  type = object({
    instance_type = string
    instance_count = number
    enable_monitoring = bool
  })
  default = {
    instance_type     = "t2.micro"
    instance_count    = 2
    enable_monitoring = false
  }
}
resource "aws_instance" "example" {
  count         = var.instance_config.instance_count
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = var.instance_config.instance_type
  monitoring    = var.instance_config.enable_monitoring
}
