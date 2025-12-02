# Introduction to Infrastructure as Code (IaC)

## What is Infrastructure as Code?

Infrastructure as Code (IaC) is the practice of managing and provisioning computing infrastructure through machine-readable configuration files rather than through manual processes or interactive configuration tools.

## Why IaC Matters

### Traditional Infrastructure Management

In traditional environments, infrastructure was managed through:
- Manual server configuration
- Point-and-click interfaces (AWS Console, Azure Portal)
- Custom scripts with no version control
- Tribal knowledge and documentation

### Problems with Manual Management

| Problem | Impact |
|---------|--------|
| Configuration Drift | Servers become inconsistent over time |
| No Audit Trail | Hard to track who changed what |
| Slow Provisioning | Manual steps take hours or days |
| Human Error | Typos and mistakes are common |
| No Reproducibility | Difficult to recreate environments |

## Benefits of IaC

### 1. Version Control
Store your infrastructure configuration in Git alongside your application code. Track every change, review pull requests, and roll back when needed.

### 2. Consistency
The same configuration produces the same infrastructure every time. Development, staging, and production can be identical.

### 3. Speed and Efficiency
Provision entire environments in minutes instead of days. Automate repetitive tasks.

### 4. Documentation
Your code IS your documentation. No more outdated wikis or runbooks.

### 5. Cost Management
Easily spin up and tear down environments. Only pay for what you need.

## IaC Tools Landscape

### Declarative vs Imperative

**Declarative** (What you want):
- Terraform
- CloudFormation
- Pulumi

**Imperative** (How to get it):
- Ansible
- Chef
- Puppet

### Why Terraform?

Terraform stands out because it is:

- **Cloud Agnostic**: Works with AWS, Azure, GCP, and 1000+ providers
- **Declarative**: You describe the desired state
- **Open Source**: Large community and ecosystem
- **State Management**: Tracks real-world resources
- **Plan Before Apply**: Preview changes before making them

## Core Terraform Concepts

### 1. Providers
Plugins that interact with cloud platforms and services.

### 2. Resources
The infrastructure components you want to create (EC2 instances, S3 buckets, etc.).

### 3. State
Terraform's record of what infrastructure exists.

### 4. Plan
A preview of what Terraform will do.

### 5. Apply
Execute the planned changes.

## The Terraform Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Write     │────▶│    Plan     │────▶│   Apply     │
│   Config    │     │  (Preview)  │     │  (Execute)  │
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │
       ▼                   ▼                   ▼
   .tf files          terraform.plan      Infrastructure
```

## Getting Started

### Installation

**macOS (Homebrew):**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

**Ubuntu/Debian:**
```bash
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

**Windows (Chocolatey):**
```powershell
choco install terraform
```

### Verify Installation

```bash
terraform version
```

## Basic Commands

| Command | Description |
|---------|-------------|
| `terraform init` | Initialize a working directory |
| `terraform plan` | Preview changes |
| `terraform apply` | Apply changes |
| `terraform destroy` | Remove all resources |
| `terraform fmt` | Format configuration files |
| `terraform validate` | Validate configuration syntax |

