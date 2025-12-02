# Terraform Local Provider

## What is the Local Provider?

The Local provider is used to manage local resources such as files and directories on the machine where Terraform runs. It's useful for generating configuration files, scripts, or any local artifacts as part of your infrastructure deployment.

## Provider Configuration

```hcl
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

# No configuration needed - the local provider works out of the box
provider "local" {}
```

## Resources

### local_file

Creates a file with the given content.

#### Basic Usage

```hcl
resource "local_file" "example" {
  content  = "Hello, World!"
  filename = "${path.module}/hello.txt"
}
```

#### With Permissions

```hcl
resource "local_file" "script" {
  content         = "#!/bin/bash\necho 'Hello from script'"
  filename        = "${path.module}/scripts/run.sh"
  file_permission = "0755"  # Executable
}
```

#### All Arguments

```hcl
resource "local_file" "complete" {
  content              = "File content here"
  filename             = "${path.module}/output/config.txt"
  file_permission      = "0644"
  directory_permission = "0755"
}
```

| Argument | Description | Default |
|----------|-------------|---------|
| `content` | Content of the file | Required (or use `content_base64` or `source`) |
| `content_base64` | Base64 encoded content | - |
| `source` | Path to source file to copy | - |
| `filename` | Path to the file to create | Required |
| `file_permission` | File permissions (octal) | `0777` |
| `directory_permission` | Directory permissions | `0777` |

### local_sensitive_file

Same as `local_file` but marks content as sensitive (won't show in logs).

```hcl
resource "local_sensitive_file" "private_key" {
  content         = tls_private_key.example.private_key_pem
  filename        = "${path.module}/keys/private.pem"
  file_permission = "0600"
}
```

## Data Sources

### local_file

Reads an existing file.

```hcl
data "local_file" "config" {
  filename = "${path.module}/configs/app.conf"
}

output "file_content" {
  value = data.local_file.config.content
}
```

#### Attributes

| Attribute | Description |
|-----------|-------------|
| `content` | Raw content of the file |
| `content_base64` | Base64 encoded content |
| `content_md5` | MD5 hash of the content |
| `content_sha1` | SHA1 hash of the content |
| `content_sha256` | SHA256 hash of the content |
| `content_base64sha256` | Base64 encoded SHA256 |
| `content_sha512` | SHA512 hash of the content |
| `content_base64sha512` | Base64 encoded SHA512 |

### local_sensitive_file (Data Source)

Reads a file without exposing content in logs.

```hcl
data "local_sensitive_file" "secret" {
  filename = "${path.module}/secrets/api_key.txt"
}
```

## Common Use Cases

### 1. Generate Configuration Files

```hcl
resource "local_file" "nginx_config" {
  filename = "${path.module}/output/nginx.conf"
  content  = <<-EOT
    server {
      listen 80;
      server_name ${var.domain_name};
      
      location / {
        proxy_pass http://${aws_instance.web.private_ip}:8080;
      }
    }
  EOT
}
```

### 2. Create Ansible Inventory

```hcl
resource "local_file" "ansible_inventory" {
  filename = "${path.module}/inventory/hosts.ini"
  content  = <<-EOT
    [webservers]
    %{ for instance in aws_instance.web ~}
    ${instance.tags.Name} ansible_host=${instance.public_ip} ansible_user=ec2-user
    %{ endfor ~}
    
    [databases]
    %{ for instance in aws_instance.db ~}
    ${instance.tags.Name} ansible_host=${instance.private_ip} ansible_user=ec2-user
    %{ endfor ~}
    
    [all:vars]
    ansible_ssh_private_key_file=~/.ssh/deployer.pem
  EOT
}
```

### 3. Generate SSH Config

```hcl
resource "local_file" "ssh_config" {
  filename        = "${path.module}/output/ssh_config"
  file_permission = "0600"
  content         = <<-EOT
    %{ for name, instance in aws_instance.servers ~}
    Host ${name}
      HostName ${instance.public_ip}
      User ec2-user
      IdentityFile ~/.ssh/deployer.pem
      StrictHostKeyChecking no
    
    %{ endfor ~}
  EOT
}
```

### 4. Create Kubernetes Manifests

```hcl
resource "local_file" "k8s_deployment" {
  filename = "${path.module}/k8s/deployment.yaml"
  content  = yamlencode({
    apiVersion = "apps/v1"
    kind       = "Deployment"
    metadata = {
      name = var.app_name
      labels = {
        app = var.app_name
      }
    }
    spec = {
      replicas = var.replica_count
      selector = {
        matchLabels = {
          app = var.app_name
        }
      }
      template = {
        metadata = {
          labels = {
            app = var.app_name
          }
        }
        spec = {
          containers = [{
            name  = var.app_name
            image = "${var.ecr_repo}:${var.image_tag}"
            ports = [{
              containerPort = 8080
            }]
          }]
        }
      }
    }
  })
}
```

### 5. Generate Environment Files

```hcl
resource "local_file" "env_file" {
  filename = "${path.module}/output/.env"
  content  = <<-EOT
    # Auto-generated by Terraform
    DATABASE_HOST=${aws_db_instance.main.address}
    DATABASE_PORT=${aws_db_instance.main.port}
    DATABASE_NAME=${aws_db_instance.main.db_name}
    REDIS_HOST=${aws_elasticache_cluster.main.cache_nodes[0].address}
    S3_BUCKET=${aws_s3_bucket.assets.id}
    AWS_REGION=${var.aws_region}
  EOT
}
```

### 6. Store Private Keys

```hcl
resource "tls_private_key" "deployer" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "deployer" {
  key_name   = "deployer-key"
  public_key = tls_private_key.deployer.public_key_openssh
}

resource "local_sensitive_file" "private_key" {
  content         = tls_private_key.deployer.private_key_pem
  filename        = "${path.module}/keys/deployer.pem"
  file_permission = "0600"
}

output "private_key_path" {
  value = local_sensitive_file.private_key.filename
}
```

### 7. Create Shell Scripts

```hcl
resource "local_file" "deploy_script" {
  filename        = "${path.module}/scripts/deploy.sh"
  file_permission = "0755"
  content         = <<-EOT
    #!/bin/bash
    set -e
    
    # Auto-generated deployment script
    CLUSTER_NAME="${aws_ecs_cluster.main.name}"
    SERVICE_NAME="${aws_ecs_service.app.name}"
    REGION="${var.aws_region}"
    
    echo "Deploying to ECS..."
    aws ecs update-service \
      --cluster $CLUSTER_NAME \
      --service $SERVICE_NAME \
      --force-new-deployment \
      --region $REGION
    
    echo "Waiting for deployment..."
    aws ecs wait services-stable \
      --cluster $CLUSTER_NAME \
      --services $SERVICE_NAME \
      --region $REGION
    
    echo "Deployment complete!"
  EOT
}
```

### 8. Generate JSON Configuration

```hcl
resource "local_file" "app_config" {
  filename = "${path.module}/output/config.json"
  content  = jsonencode({
    database = {
      host     = aws_db_instance.main.address
      port     = aws_db_instance.main.port
      name     = var.db_name
      ssl      = true
    }
    cache = {
      host = aws_elasticache_cluster.main.cache_nodes[0].address
      port = 6379
    }
    storage = {
      bucket = aws_s3_bucket.main.id
      region = var.aws_region
    }
    features = var.feature_flags
  })
}
```

## Using templatefile with local_file

```hcl
# templates/config.yaml.tpl
database:
  host: ${db_host}
  port: ${db_port}
  name: ${db_name}
  
servers:
%{ for server in servers ~}
  - name: ${server.name}
    ip: ${server.ip}
    role: ${server.role}
%{ endfor ~}
```

```hcl
resource "local_file" "config" {
  filename = "${path.module}/output/config.yaml"
  content  = templatefile("${path.module}/templates/config.yaml.tpl", {
    db_host = aws_db_instance.main.address
    db_port = aws_db_instance.main.port
    db_name = var.db_name
    servers = [
      for instance in aws_instance.web : {
        name = instance.tags.Name
        ip   = instance.private_ip
        role = "web"
      }
    ]
  })
}
```

## Best Practices

### Do's

```hcl
# Use path.module for relative paths
resource "local_file" "config" {
  filename = "${path.module}/output/config.txt"
  content  = "content"
}

# Set appropriate permissions
resource "local_file" "script" {
  filename        = "${path.module}/scripts/run.sh"
  file_permission = "0755"
  content         = "#!/bin/bash\necho hello"
}

# Use local_sensitive_file for secrets
resource "local_sensitive_file" "credentials" {
  filename        = "${path.module}/secrets/creds.json"
  file_permission = "0600"
  content         = jsonencode({
    api_key = var.api_key
  })
}
```

### Don'ts

```hcl
# Don't use absolute paths
resource "local_file" "bad" {
  filename = "/tmp/config.txt"  # May not work across systems
  content  = "content"
}

# Don't store secrets in regular local_file
resource "local_file" "insecure" {
  filename = "secret.txt"
  content  = var.password  # Will show in logs!
}
```

## Gitignore for Local Files

```gitignore
# Terraform generated local files
*.pem
.env
output/
keys/
secrets/
inventory/hosts.ini
```

