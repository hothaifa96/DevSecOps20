# Terraform Project Structure and Architecture

## File Naming Conventions

Terraform loads all `.tf` files in a directory. While you can put everything in one file, best practice is to organize your code into logical files.

## Standard File Structure

```
my-terraform-project/
├── main.tf           # Primary resource definitions
├── variables.tf      # Input variable declarations
├── outputs.tf        # Output value declarations
├── providers.tf      # Provider configuration
├── locals.tf         # Local value definitions
├── data.tf           # Data source definitions
├── versions.tf       # Terraform and provider version constraints
├── terraform.tfvars  # Variable values (don't commit secrets!)
└── README.md         # Documentation
```

## File Purposes

### main.tf
Contains the primary resource definitions for your infrastructure.

```hcl
resource "aws_instance" "web_server" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  tags = local.common_tags
}
```

### variables.tf
Declares all input variables your configuration accepts.

```hcl
variable "ami_id" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}
```

### outputs.tf
Defines values to display after apply or share with other configurations.

```hcl
output "instance_public_ip" {
  description = "Public IP of the web server"
  value       = aws_instance.web_server.public_ip
}
```

### providers.tf
Configures the providers you're using.

```hcl
provider "aws" {
  region = var.aws_region
}
```

### locals.tf
Defines local values for reuse within your configuration.

```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    ManagedBy   = "Terraform"
  }
}
```

### data.tf
Contains data source definitions for fetching external information.

```hcl
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}
```

### versions.tf
Specifies required Terraform and provider versions.

```hcl
terraform {
  required_version = ">= 1.0.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

## Advanced Project Structures

### Multi-Environment Structure

```
infrastructure/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── staging/
│   │   ├── main.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   └── prod/
│       ├── main.tf
│       ├── terraform.tfvars
│       └── backend.tf
└── modules/
    ├── vpc/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── ec2/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── rds/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

### Module Structure

```
modules/
└── ec2-instance/
    ├── main.tf           # Resource definitions
    ├── variables.tf      # Input variables
    ├── outputs.tf        # Output values
    ├── versions.tf       # Version constraints
    ├── README.md         # Module documentation
    └── examples/
        └── basic/
            ├── main.tf
            └── outputs.tf
```

## State File Management

### Local State (Default)

```
my-project/
├── main.tf
├── terraform.tfstate        # Current state
└── terraform.tfstate.backup # Previous state
```

### Remote State (Recommended for Teams)

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

## Files to Ignore

Create a `.gitignore` file:

```gitignore
# Local .terraform directories
**/.terraform/*

# .tfstate files
*.tfstate
*.tfstate.*

# Crash log files
crash.log
crash.*.log

# Exclude all .tfvars files, which may contain sensitive data
*.tfvars
*.tfvars.json

# Ignore override files
override.tf
override.tf.json
*_override.tf
*_override.tf.json

# Ignore CLI configuration files
.terraformrc
terraform.rc
```

## Best Practices Summary

| Practice | Reason |
|----------|--------|
| One purpose per file | Easier navigation and maintenance |
| Consistent naming | Team alignment and predictability |
| Use modules | Reusability and DRY principle |
| Remote state | Team collaboration and security |
| Version constraints | Reproducible builds |
| README files | Self-documenting infrastructure |

