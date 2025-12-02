# Terraform Locals

## What Are Locals?

Local values (locals) are named expressions that you can reference multiple times within a module. They help you avoid repetition and make your configuration easier to read and maintain.

Think of locals as variables that are defined and computed within your configuration, rather than passed in from outside.

## Locals vs Variables

| Aspect | Variables | Locals |
|--------|-----------|--------|
| Source | External input | Computed internally |
| Purpose | Parameterize configuration | Reduce repetition |
| Can be overridden | Yes | No |
| Reference syntax | `var.name` | `local.name` |

## Basic Syntax

```hcl
locals {
  name = "expression"
}

# Reference
resource "example" "test" {
  attribute = local.name
}
```

## Common Use Cases

### 1. Common Tags

```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    Team        = var.team_name
    ManagedBy   = "Terraform"
    CostCenter  = var.cost_center
  }
}

resource "aws_instance" "web" {
  ami           = var.ami_id
  instance_type = var.instance_type
  
  tags = merge(local.common_tags, {
    Name = "web-server"
    Role = "web"
  })
}

resource "aws_s3_bucket" "logs" {
  bucket = "${var.project_name}-logs"
  
  tags = merge(local.common_tags, {
    Name = "log-bucket"
  })
}
```

### 2. Computed Values

```hcl
locals {
  # Combine variables
  full_name = "${var.project_name}-${var.environment}"
  
  # Calculate values
  instance_count = var.environment == "prod" ? 3 : 1
  
  # Construct resource names
  bucket_name = "${var.company}-${var.project_name}-${var.environment}-${var.aws_region}"
}

resource "aws_s3_bucket" "main" {
  bucket = local.bucket_name
}
```

### 3. Conditional Logic

```hcl
locals {
  # Environment-based settings
  is_production = var.environment == "prod"
  
  instance_type = local.is_production ? "t3.large" : "t3.micro"
  
  multi_az = local.is_production ? true : false
  
  backup_retention = local.is_production ? 30 : 7
}

resource "aws_db_instance" "main" {
  instance_class         = local.instance_type
  multi_az               = local.multi_az
  backup_retention_period = local.backup_retention
  # ...
}
```

### 4. Data Transformation

```hcl
variable "subnet_cidrs" {
  type = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

locals {
  # Create a map from list
  subnet_map = {
    for idx, cidr in var.subnet_cidrs :
    "subnet-${idx}" => cidr
  }
  
  # Filter a list
  large_cidrs = [
    for cidr in var.subnet_cidrs :
    cidr if tonumber(split("/", cidr)[1]) < 24
  ]
  
  # Transform list to different format
  subnet_names = [
    for idx, _ in var.subnet_cidrs :
    "subnet-${var.environment}-${idx + 1}"
  ]
}
```

### 5. Complex Objects

```hcl
locals {
  environments = {
    dev = {
      instance_type    = "t3.micro"
      instance_count   = 1
      enable_monitoring = false
    }
    staging = {
      instance_type    = "t3.small"
      instance_count   = 2
      enable_monitoring = true
    }
    prod = {
      instance_type    = "t3.large"
      instance_count   = 3
      enable_monitoring = true
    }
  }
  
  # Get current environment config
  current_env = local.environments[var.environment]
}

resource "aws_instance" "web" {
  count         = local.current_env.instance_count
  ami           = var.ami_id
  instance_type = local.current_env.instance_type
  monitoring    = local.current_env.enable_monitoring
}
```

### 6. String Manipulation

```hcl
locals {
  # Remove spaces and lowercase
  normalized_name = lower(replace(var.project_name, " ", "-"))
  
  # Build ARN
  bucket_arn = "arn:aws:s3:::${local.bucket_name}"
  
  # Format timestamp
  timestamp = formatdate("YYYY-MM-DD", timestamp())
  
  # Join list into string
  az_string = join(", ", var.availability_zones)
}
```

### 7. Working with JSON/YAML

```hcl
locals {
  # Parse JSON file
  config = jsondecode(file("${path.module}/config.json"))
  
  # Parse YAML file
  settings = yamldecode(file("${path.module}/settings.yaml"))
  
  # Create JSON string
  policy_json = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject"]
        Resource = "${local.bucket_arn}/*"
      }
    ]
  })
}
```

## Multiple locals Blocks

You can have multiple locals blocks in a file:

```hcl
# Naming conventions
locals {
  name_prefix = "${var.project}-${var.environment}"
  name_suffix = var.aws_region
}

# Tags
locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
  }
}

# Computed values
locals {
  full_name = "${local.name_prefix}-${local.name_suffix}"
}
```

## Locals with Data Sources

```hcl
data "aws_caller_identity" "current" {}
data "aws_region" "current" {}

locals {
  account_id = data.aws_caller_identity.current.account_id
  region     = data.aws_region.current.name
  
  # Build account-specific resource names
  state_bucket = "terraform-state-${local.account_id}-${local.region}"
  
  # Construct IAM ARNs
  role_arn = "arn:aws:iam::${local.account_id}:role/${var.role_name}"
}
```

## For Expressions in Locals

### List Transformation

```hcl
variable "users" {
  type = list(string)
  default = ["alice", "bob", "charlie"]
}

locals {
  # Transform list
  user_emails = [for user in var.users : "${user}@example.com"]
  
  # Filter list
  admins = [for user in var.users : user if contains(var.admin_users, user)]
  
  # Create map from list
  user_map = {for user in var.users : user => "${user}@example.com"}
}
```

### Map Transformation

```hcl
variable "instances" {
  type = map(object({
    type = string
    az   = string
  }))
  default = {
    web = { type = "t3.micro", az = "us-east-1a" }
    api = { type = "t3.small", az = "us-east-1b" }
  }
}

locals {
  # Get all instance types
  instance_types = [for k, v in var.instances : v.type]
  
  # Filter instances
  micro_instances = {
    for k, v in var.instances :
    k => v if v.type == "t3.micro"
  }
  
  # Transform keys
  instance_names = {
    for k, v in var.instances :
    "${var.environment}-${k}" => v
  }
}
```

## Locals with Conditional Logic

```hcl
locals {
  # Simple ternary
  instance_type = var.environment == "prod" ? "t3.large" : "t3.micro"
  
  # Multiple conditions
  db_instance_class = (
    var.environment == "prod" ? "db.r5.large" :
    var.environment == "staging" ? "db.t3.medium" :
    "db.t3.micro"
  )
  
  # Conditional list
  availability_zones = var.multi_az ? [
    "${var.aws_region}a",
    "${var.aws_region}b",
    "${var.aws_region}c"
  ] : [
    "${var.aws_region}a"
  ]
  
  # Conditional map merge
  instance_tags = var.is_production ? merge(local.common_tags, {
    Backup    = "true"
    Monitored = "true"
  }) : local.common_tags
}
```

## Best Practices

### Do Use Locals For

```hcl
locals {
  # Repeated values
  common_tags = {
    Environment = var.environment
    Project     = var.project
  }
  
  # Complex expressions
  bucket_name = lower("${var.company}-${var.project}-${var.environment}")
  
  # Conditional logic
  instance_count = var.environment == "prod" ? 3 : 1
  
  # Data transformations
  subnet_ids = [for s in aws_subnet.main : s.id]
}
```

### Avoid

```hcl
locals {
  # Don't use for simple pass-through
  region = var.region  # Just use var.region directly
  
  # Don't create overly complex nested locals
  deeply_nested = local.level1.level2.level3.value
}
```

### Organization Tips

```hcl
# Group related locals together
locals {
  # Naming
  name_prefix = "${var.project}-${var.environment}"
}

locals {
  # Tags
  common_tags = {
    Project = var.project
  }
}

locals {
  # Computed settings
  settings = {
    instance_type = var.environment == "prod" ? "large" : "small"
  }
}
```

