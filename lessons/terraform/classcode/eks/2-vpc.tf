#AZ - 

data "aws_availability_zones" "az" {
  state = "available"
}

# output "az" {
#   value = data.aws_availability_zones.az.names
# }

resource "aws_vpc" "terraform-eks-demo" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = true
  tags = {
    Name = "eks-tf-demo"
  }
}

# output "az-names" {
#   value = data.aws_availability_zones.az.names[0]
# }

resource "aws_subnet" "public-subnet-1" {
    vpc_id = aws_vpc.terraform-eks-demo.id
    cidr_block = cidrsubnet(var.cidr_block,8,0) # 10.10.0.0/24
    availability_zone = data.aws_availability_zones.az.names[0] # us-east-1a
    tags = {
        Name = "public-subnet-1"
    }
}
resource "aws_subnet" "public-subnet-2" {
    vpc_id = aws_vpc.terraform-eks-demo.id
    cidr_block = cidrsubnet(var.cidr_block,8,2) # 10.10.2.0/24
    availability_zone = data.aws_availability_zones.az.names[1] # us-east-1b
    tags = {
        Name = "public-subnet-2"
    }
}


resource "aws_subnet" "private-subnet-1" {
    vpc_id = aws_vpc.terraform-eks-demo.id
    cidr_block = cidrsubnet(var.cidr_block,8,1) # 10.10.1.0/24
    availability_zone = data.aws_availability_zones.az.names[0] # us-east-1b
    tags = {
        Name = "private-subnet-2"
    }
}

resource "aws_subnet" "private-subnet-2" {
    vpc_id = aws_vpc.terraform-eks-demo.id
    cidr_block = cidrsubnet(var.cidr_block,8,3) # 10.10.3.0/24
    availability_zone = data.aws_availability_zones.az.names[1] # us-east-1b
    tags = {
        Name = "private-subnet-2"
    }
}

resource "aws_internet_gateway" "eks-igw" {
  vpc_id = aws_vpc.terraform-eks-demo.id
  tags = {
    Name= "eks-igw"
  }
}

resource "aws_internet_gateway" "eks-igw2" {
  vpc_id = aws_vpc.terraform-eks-demo.id
  tags = {
    Name= "eks-igw2"
  }
}

resource "aws_route_table" "public-rt" {
  vpc_id = aws_vpc.terraform-eks-demo.id

  route {
    cidr_block = var.cidr_block
    gateway_id = aws_internet_gateway.eks-igw.id
  }
}

# associate rt to subnet
resource "aws_route_table_association" "public-rt-assoc-1" {
  subnet_id = aws_subnet.public-subnet-1.id
  route_table_id = aws_route_table.public-rt.id
}
resource "aws_route_table_association" "public-rt-assoc-2" {
  subnet_id = aws_subnet.public-subnet-2.id
  route_table_id = aws_route_table.public-rt.id
}

