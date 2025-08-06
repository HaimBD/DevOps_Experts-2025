provider "aws" {
  region = "us-east-1"
}

# VPC A
resource "aws_vpc" "vpc_a" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "VPC A"
  }
}

# Internet Gateway for VPC A
resource "aws_internet_gateway" "igw_a" {
  vpc_id = aws_vpc.vpc_a.id

  tags = {
    Name = "VPC A Internet Gateway"
  }
}

# Subnet for VPC A (public subnet)
resource "aws_subnet" "subnet_a" {
  vpc_id     = aws_vpc.vpc_a.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true  # Automatically assign public IPs on launch
  tags = {
    Name = "VPC A Public Subnet"
  }
}

# Route Table for VPC A with Internet Gateway route
resource "aws_route_table" "route_table_a" {
  vpc_id = aws_vpc.vpc_a.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw_a.id  # Route traffic to the internet
  }

  tags = {
    Name = "VPC A Public Route Table"
  }
}

# Associate Route Table with Subnet A (public)
resource "aws_route_table_association" "subnet_a_association" {
  subnet_id      = aws_subnet.subnet_a.id
  route_table_id = aws_route_table.route_table_a.id
}

# Security Group for VPC A (allow SSH and inter-VPC traffic)
resource "aws_security_group" "sg_a" {
  vpc_id = aws_vpc.vpc_a.id

  # Allow SSH from the internet
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow SSH from anywhere (adjust as needed)
  }

  # Allow traffic from VPC B
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["10.1.0.0/16"]  # Allow traffic from VPC B
  }

  # Allow ICMP (ping) from VPC B
  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["10.1.0.0/16"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Allow SSH and Peering traffic in VPC A"
  }
}

# EC2 Instance in VPC A with a public IP
resource "aws_instance" "instance_a" {
  ami           = "ami-0e86e20dae9224db8"  # Example Ubuntu AMI ID
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet_a.id
  vpc_security_group_ids = [aws_security_group.sg_a.id]  # Use security group ID
  key_name      = aws_key_pair.my_key.key_name
  associate_public_ip_address = true  # Ensure public IP is assigned

  tags = {
    Name = "Instance in VPC A"
  }
}

# VPC B
resource "aws_vpc" "vpc_b" {
  cidr_block = "10.1.0.0/16"
  tags = {
    Name = "VPC B"
  }
}

# Internet Gateway for VPC B
resource "aws_internet_gateway" "igw_b" {
  vpc_id = aws_vpc.vpc_b.id

  tags = {
    Name = "VPC B Internet Gateway"
  }
}

# Subnet for VPC B (public subnet)
resource "aws_subnet" "subnet_b" {
  vpc_id     = aws_vpc.vpc_b.id
  cidr_block = "10.1.1.0/24"
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true  # Automatically assign public IPs on launch
  tags = {
    Name = "VPC B Public Subnet"
  }
}

# Route Table for VPC B with Internet Gateway route
resource "aws_route_table" "route_table_b" {
  vpc_id = aws_vpc.vpc_b.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw_b.id  # Route traffic to the internet
  }

  tags = {
    Name = "VPC B Public Route Table"
  }
}

# Associate Route Table with Subnet B (public)
resource "aws_route_table_association" "subnet_b_association" {
  subnet_id      = aws_subnet.subnet_b.id
  route_table_id = aws_route_table.route_table_b.id
}

# Security Group for VPC B (allow SSH and inter-VPC traffic)
resource "aws_security_group" "sg_b" {
  vpc_id = aws_vpc.vpc_b.id

  # Allow SSH from the internet
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Allow SSH from anywhere (adjust as needed)
  }

  # Allow traffic from VPC A
  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]  # Allow traffic from VPC A
  }

  # Allow ICMP (ping) from VPC A
  ingress {
    from_port   = -1
    to_port     = -1
    protocol    = "icmp"
    cidr_blocks = ["10.0.0.0/16"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Allow SSH and Peering traffic in VPC B"
  }
}

# EC2 Instance in VPC B with a public IP
resource "aws_instance" "instance_b" {
  ami           = "ami-0e86e20dae9224db8"  # Example Ubuntu AMI ID
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet_b.id
  vpc_security_group_ids = [aws_security_group.sg_b.id]  # Use security group ID
  key_name      = aws_key_pair.my_key.key_name
  associate_public_ip_address = true  # Ensure public IP is assigned

  tags = {
    Name = "Instance in VPC B"
  }
}

# Create a VPC Peering Connection between VPC A and VPC B
resource "aws_vpc_peering_connection" "vpc_peering" {
  vpc_id        = aws_vpc.vpc_a.id
  peer_vpc_id   = aws_vpc.vpc_b.id
  auto_accept   = true

  tags = {
    Name = "VPC A to VPC B Peering"
  }
}

# Add a route in VPC A's Route Table to route traffic to VPC B via the Peering Connection
resource "aws_route" "route_to_vpc_b" {
  route_table_id         = aws_route_table.route_table_a.id
  destination_cidr_block = "10.1.0.0/16"
  vpc_peering_connection_id = aws_vpc_peering_connection.vpc_peering.id
}

# Add a route in VPC B's Route Table to route traffic to VPC A via the Peering Connection
resource "aws_route" "route_to_vpc_a" {
  route_table_id         = aws_route_table.route_table_b.id
  destination_cidr_block = "10.0.0.0/16"
  vpc_peering_connection_id = aws_vpc_peering_connection.vpc_peering.id
}

# Create a Key Pair for SSH Access
resource "aws_key_pair" "my_key" {
  key_name   = "hbd-kp"
  public_key = file("~/.ssh/id_rsa.pub")
}