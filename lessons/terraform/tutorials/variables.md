# Terraform Variables

## What Are Variables?

Variables in Terraform allow you to parameterize your configurations, making them reusable and flexible. Instead of hardcoding values, you define variables that can be set differently for each deployment.

## Variable Declaration

### Basic Syntax

```hcl
variable "variable_name" {
  description = "Description of what this variable does"
  type        = string
  default     = "default_value"
}
```

### Variable Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `description` | No | Human-readable description |
| `type` | No | Type constraint for the variable |
| `default` | No | Default value if none provided |
| `validation` | No | Custom validation rules |
| `sensitive` | No | Hide value in logs and output |
| `nullable` | No | Whether variable can be null |

## Variable Types

### Primitive Types

```hcl
# String
variable "instance_name" {
  type    = string
  default = "my-server"
}

# Number
variable "instance_count" {
  type    = number
  default = 2
}

# Boolean
variable "enable_monitoring" {
  type    = bool
  default = true
}
```

### Collection Types

```hcl
# List (ordered collection of same type)
variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

# Set (unordered unique values)
variable "allowed_ports" {
  type    = set(number)
  default = [22, 80, 443]
}

# Map (key-value pairs)
variable "instance_tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Team        = "platform"
  }
}
```

### Structural Types

```hcl
# Object (structured with named attributes)
variable "server_config" {
  type = object({
    name          = string
    instance_type = string
    disk_size     = number
    public        = bool
  })
  default = {
    name          = "web-server"
    instance_type = "t3.micro"
    disk_size     = 20
    public        = true
  }
}

# Tuple (fixed-length sequence with specific types)
variable "network_config" {
  type    = tuple([string, number, bool])
  default = ["10.0.0.0/16", 3, true]
}
```

### Complex Nested Types

```hcl
variable "servers" {
  type = list(object({
    name          = string
    instance_type = string
    tags          = map(string)
  }))
  default = [
    {
      name          = "web-1"
      instance_type = "t3.micro"
      tags = {
        Role = "web"
      }
    },
    {
      name          = "api-1"
      instance_type = "t3.small"
      tags = {
        Role = "api"
      }
    }
  ]
}
```

## Setting Variable Values

### Method 1: Default Values

```hcl
variable "region" {
  type    = string
  default = "us-east-1"
}
```

### Method 2: terraform.tfvars File

```hcl
# terraform.tfvars
region         = "us-west-2"
instance_type  = "t3.medium"
instance_count = 3
```

### Method 3: Named .tfvars Files

```hcl
# production.tfvars
region         = "us-east-1"
instance_type  = "t3.large"
instance_count = 10
```

```bash
terraform apply -var-file="production.tfvars"
```

### Method 4: Command Line

```bash
terraform apply -var="region=us-west-2" -var="instance_count=5"
```

### Method 5: Environment Variables

```bash
export TF_VAR_region="us-west-2"
export TF_VAR_instance_count=5
terraform apply
```

## Variable Precedence

From lowest to highest priority:

1. Default values in declaration
2. Environment variables (`TF_VAR_*`)
3. `terraform.tfvars` file
4. `*.auto.tfvars` files (alphabetical order)
5. `-var-file` flags (in order)
6. `-var` flags (in order)

## Variable Validation

### Basic Validation

```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  
  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.instance_type)
    error_message = "Instance type must be t3.micro, t3.small, or t3.medium."
  }
}
```

### Multiple Validations

```hcl
variable "environment" {
  type        = string
  description = "Deployment environment"
  
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
  
  validation {
    condition     = length(var.environment) >= 3
    error_message = "Environment name must be at least 3 characters."
  }
}
```

### Regex Validation

```hcl
variable "bucket_name" {
  type        = string
  description = "S3 bucket name"
  
  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9.-]*[a-z0-9]$", var.bucket_name))
    error_message = "Bucket name must be lowercase, start/end with alphanumeric."
  }
}
```

## Sensitive Variables

```hcl
variable "database_password" {
  type        = string
  description = "Database admin password"
  sensitive   = true
}
```

When marked sensitive:
- Value is hidden in `terraform plan` output
- Value is hidden in `terraform apply` output
- Value is still stored in state file (encrypt your state!)

## Using Variables

### Basic Reference

```hcl
resource "aws_instance" "server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  tags = {
    Name = var.instance_name
  }
}
```

### With Collections

```hcl
# Using list
resource "aws_instance" "server" {
  ami               = var.ami_id
  instance_type     = var.instance_type
  availability_zone = var.availability_zones[0]
}

# Using map
resource "aws_instance" "server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  tags = var.instance_tags
}
```

### With for_each

```hcl
variable "instances" {
  type = map(object({
    instance_type = string
    ami           = string
  }))
}

resource "aws_instance" "servers" {
  for_each = var.instances
  
  ami           = each.value.ami
  instance_type = each.value.instance_type
  
  tags = {
    Name = each.key
  }
}
```

## Best Practices

### Do's

```hcl
# Use descriptive names
variable "web_server_instance_type" {
  description = "Instance type for web servers in the frontend tier"
  type        = string
  default     = "t3.micro"
}

# Always include descriptions
variable "vpc_cidr" {
  description = "CIDR block for the VPC. Must be /16 or larger."
  type        = string
}

# Use appropriate types
variable "enable_deletion_protection" {
  type    = bool
  default = true
}

# Validate inputs
variable "environment" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Valid values: dev, staging, prod."
  }
}
```

### Don'ts

```hcl
# Don't use vague names
variable "x" {
  type = string
}

# Don't skip descriptions
variable "cidr" {
  type = string
}

# Don't use string for everything
variable "count" {
  type    = string  # Should be number
  default = "5"
}
```
