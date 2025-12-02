# Terraform Providers

## What Are Providers?

Providers are plugins that Terraform uses to interact with cloud platforms, SaaS providers, and other APIs. They are responsible for understanding API interactions and exposing resources.

Think of providers as the "translators" between Terraform and the services you want to manage.

## Provider Architecture

```
┌─────────────────────────────────────────┐
│           Terraform Core                │
└─────────────────┬───────────────────────┘
                  │
    ┌─────────────┼─────────────┐
    ▼             ▼             ▼
┌────────┐  ┌──────────┐  ┌──────────┐
│  AWS   │  │  Azure   │  │   GCP    │
│Provider│  │ Provider │  │ Provider │
└────┬───┘  └────┬─────┘  └────┬─────┘
     │           │              │
     ▼           ▼              ▼
┌────────┐  ┌──────────┐  ┌──────────┐
│AWS API │  │Azure API │  │ GCP API  │
└────────┘  └──────────┘  └──────────┘
```

## Provider Configuration

### Basic AWS Provider

```hcl
# providers.tf
provider "aws" {
  region = "us-east-1"
}
```

### With Authentication

```hcl
# Using static credentials (NOT recommended for production)
provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAIOSFODNN7EXAMPLE"
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}

# Using shared credentials file (recommended)
provider "aws" {
  region                   = "us-east-1"
  shared_credentials_files = ["~/.aws/credentials"]
  profile                  = "production"
}

# Using environment variables (recommended for CI/CD)
# Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
provider "aws" {
  region = "us-east-1"
}

# Using IAM role (recommended for EC2/ECS)
provider "aws" {
  region = "us-east-1"
  # Automatically uses instance profile
}
```

### Assume Role

```hcl
provider "aws" {
  region = "us-east-1"
  
  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/TerraformRole"
    session_name = "terraform-session"
    external_id  = "my-external-id"
  }
}
```

## Version Constraints

### Specifying Provider Versions

```hcl
# versions.tf
terraform {
  required_version = ">= 1.0.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = ">= 3.0.0, < 4.0.0"
    }
  }
}
```

### Version Constraint Syntax

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Exact version | `= 5.0.0` |
| `!=` | Not equal | `!= 5.0.0` |
| `>` | Greater than | `> 5.0.0` |
| `>=` | Greater or equal | `>= 5.0.0` |
| `<` | Less than | `< 6.0.0` |
| `<=` | Less or equal | `<= 5.9.0` |
| `~>` | Pessimistic (minor) | `~> 5.0` allows 5.x |

### Recommended Approach

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"  # Allows 5.x but not 6.0
    }
  }
}
```

## Multiple Provider Configurations

### Alias for Multiple Regions

```hcl
# Default provider (no alias)
provider "aws" {
  region = "us-east-1"
}

# Aliased provider for another region
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

provider "aws" {
  alias  = "eu"
  region = "eu-west-1"
}

# Use default provider
resource "aws_instance" "east_server" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
}

# Use aliased provider
resource "aws_instance" "west_server" {
  provider      = aws.west
  ami           = "ami-87654321"
  instance_type = "t3.micro"
}

resource "aws_s3_bucket" "eu_bucket" {
  provider = aws.eu
  bucket   = "my-eu-bucket"
}
```

### Multiple AWS Accounts

```hcl
provider "aws" {
  alias  = "production"
  region = "us-east-1"
  
  assume_role {
    role_arn = "arn:aws:iam::111111111111:role/TerraformRole"
  }
}

provider "aws" {
  alias  = "staging"
  region = "us-east-1"
  
  assume_role {
    role_arn = "arn:aws:iam::222222222222:role/TerraformRole"
  }
}

resource "aws_instance" "prod_server" {
  provider      = aws.production
  ami           = var.ami_id
  instance_type = "t3.large"
}

resource "aws_instance" "staging_server" {
  provider      = aws.staging
  ami           = var.ami_id
  instance_type = "t3.micro"
}
```

## Common Providers

### AWS Provider

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = var.project_name
    }
  }
}
```

### Azure Provider

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
  
  subscription_id = var.subscription_id
  tenant_id       = var.tenant_id
}
```

### Google Cloud Provider

```hcl
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
```

### Kubernetes Provider

```hcl
terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.0"
    }
  }
}

provider "kubernetes" {
  config_path = "~/.kube/config"
  # Or use in-cluster config
  # host = "https://kubernetes.default.svc"
}
```

## Provider Features

### AWS Default Tags

```hcl
provider "aws" {
  region = "us-east-1"
  
  default_tags {
    tags = {
      Environment = "production"
      Team        = "platform"
      ManagedBy   = "Terraform"
    }
  }
}

# All resources automatically get these tags
resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = "t3.micro"
  
  tags = {
    Name = "web-server"  # Additional tag
  }
  # Gets Environment, Team, ManagedBy automatically
}
```

### Ignoring Tags

```hcl
provider "aws" {
  region = "us-east-1"
  
  ignore_tags {
    keys = ["LastScannedAt", "aws:cloudformation:*"]
  }
}
```

## Provider Initialization

### terraform init

```bash
# Initialize and download providers
terraform init

# Upgrade providers to latest allowed versions
terraform init -upgrade

# Use a specific plugin directory
terraform init -plugin-dir=/path/to/plugins
```

### Lock File

After `terraform init`, a `.terraform.lock.hcl` file is created:

```hcl
# .terraform.lock.hcl
provider "registry.terraform.io/hashicorp/aws" {
  version     = "5.31.0"
  constraints = "~> 5.0"
  hashes = [
    "h1:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX=",
    "zh:YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY",
  ]
}
```

Commit this file to ensure consistent provider versions across team members.

## Best Practices

### 1. Pin Provider Versions

```hcl
# Do this
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Avoid this
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      # No version constraint - dangerous!
    }
  }
}
```

### 2. Use Environment Variables for Credentials

```bash
# Set in your shell or CI/CD
export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_REGION="us-east-1"
```

### 3. Separate Provider Configuration

```hcl
# providers.tf - Provider configurations
provider "aws" {
  region = var.aws_region
}

# versions.tf - Version constraints
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

### 4. Use Default Tags

```hcl
provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = local.common_tags
  }
}
```
