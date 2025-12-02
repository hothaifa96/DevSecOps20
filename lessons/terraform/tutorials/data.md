# Terraform Data Sources

## What Are Data Sources?

Data sources allow Terraform to fetch information from external sources or existing infrastructure. They are read-only and don't create, update, or delete resources.

Think of data sources as queries that retrieve information you need to configure your resources.

## Data Source vs Resource

| Aspect | Resource | Data Source |
|--------|----------|-------------|
| Purpose | Create/manage infrastructure | Query existing information |
| Keyword | `resource` | `data` |
| State | Tracked in state file | Refreshed each run |
| Operations | Create, Read, Update, Delete | Read only |

## Basic Syntax

```hcl
data "provider_type" "name" {
  # Query parameters
  filter_argument = "value"
}

# Reference the result
resource "aws_instance" "example" {
  ami = data.provider_type.name.attribute
}
```

## Common AWS Data Sources

### AWS AMI

Find the latest Amazon Linux 2 AMI:

```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}

# Use it
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

### AWS Availability Zones

Get available AZs in the current region:

```hcl
data "aws_availability_zones" "available" {
  state = "available"
  
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

# Use in subnet creation
resource "aws_subnet" "public" {
  count             = length(data.aws_availability_zones.available.names)
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
}
```

### AWS VPC

Reference an existing VPC:

```hcl
# By ID
data "aws_vpc" "selected" {
  id = "vpc-12345678"
}

# By tag
data "aws_vpc" "production" {
  tags = {
    Environment = "production"
  }
}

# By filter
data "aws_vpc" "default" {
  default = true
}

# Use it
resource "aws_subnet" "example" {
  vpc_id     = data.aws_vpc.selected.id
  cidr_block = "10.0.1.0/24"
}
```

### AWS Subnet

Find subnets in a VPC:

```hcl
data "aws_subnets" "private" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }

  tags = {
    Tier = "private"
  }
}

# Get details of each subnet
data "aws_subnet" "private" {
  for_each = toset(data.aws_subnets.private.ids)
  id       = each.value
}

# Use in auto scaling group
resource "aws_autoscaling_group" "web" {
  vpc_zone_identifier = data.aws_subnets.private.ids
  # ...
}
```

### AWS Security Group

Reference existing security groups:

```hcl
data "aws_security_group" "default" {
  vpc_id = var.vpc_id
  name   = "default"
}

data "aws_security_groups" "web" {
  tags = {
    Application = "web"
  }
}
```

### AWS IAM

```hcl
# Current AWS account
data "aws_caller_identity" "current" {}

# Current region
data "aws_region" "current" {}

# IAM policy document
data "aws_iam_policy_document" "assume_role" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}

# Use the policy document
resource "aws_iam_role" "ec2_role" {
  name               = "ec2-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}
```

### AWS Route53

```hcl
data "aws_route53_zone" "main" {
  name         = "example.com"
  private_zone = false
}

resource "aws_route53_record" "www" {
  zone_id = data.aws_route53_zone.main.zone_id
  name    = "www.example.com"
  type    = "A"
  ttl     = "300"
  records = [aws_instance.web.public_ip]
}
```

## Data Source Attributes

Each data source provides different attributes. Common patterns:

```hcl
# Single value attributes
data.aws_ami.example.id
data.aws_ami.example.name
data.aws_ami.example.arn

# List attributes
data.aws_availability_zones.available.names
data.aws_subnets.private.ids

# Map attributes
data.aws_vpc.main.tags
```

## Filtering Data Sources

### Using filter blocks

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]  # Canonical

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}
```

### Using tags

```hcl
data "aws_vpc" "production" {
  tags = {
    Environment = "production"
    Team        = "platform"
  }
}
```

### Using specific IDs

```hcl
data "aws_instance" "web" {
  instance_id = "i-1234567890abcdef0"
}
```

## Multiple Results with for_each

```hcl
# Get all subnet IDs
data "aws_subnets" "all" {
  filter {
    name   = "vpc-id"
    values = [var.vpc_id]
  }
}

# Get details for each subnet
data "aws_subnet" "details" {
  for_each = toset(data.aws_subnets.all.ids)
  id       = each.value
}

# Use in output
output "subnet_cidrs" {
  value = { for k, v in data.aws_subnet.details : k => v.cidr_block }
}
```

## The aws_caller_identity Data Source

Very useful for getting current account information:

```hcl
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
  region     = data.aws_region.current.name
  
  # Construct ARNs
  bucket_arn = "arn:aws:s3:::${local.account_id}-${local.region}-logs"
}

output "account_info" {
  value = {
    account_id = data.aws_caller_identity.current.account_id
    caller_arn = data.aws_caller_identity.current.arn
    user_id    = data.aws_caller_identity.current.user_id
    region     = data.aws_region.current.name
  }
}
```

## External Data Source

Run external programs and use the output:

```hcl
data "external" "git_hash" {
  program = ["bash", "-c", "echo '{\"hash\": \"'$(git rev-parse --short HEAD)'\"}'"]
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"

  tags = {
    GitCommit = data.external.git_hash.result.hash
  }
}
```

## Best Practices

### Use Data Sources When

- Referencing existing infrastructure not managed by Terraform
- Looking up dynamic values (latest AMI, available AZs)
- Sharing data between Terraform configurations
- Avoiding hardcoded values that might change

### Avoid Data Sources When

- You're creating the resource in the same configuration
- The value is static and well-known
- It introduces unnecessary dependencies

### Example: Good Use

```hcl
# Good: Dynamic AMI lookup
data "aws_ami" "latest" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*"]
  }
}
```

### Example: Unnecessary Use

```hcl
# Unnecessary: Querying a resource you just created
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

# Don't do this - just use aws_vpc.main.id directly
data "aws_vpc" "main" {
  id = aws_vpc.main.id
}
```
