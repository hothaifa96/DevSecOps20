terraform {
    required_providers {
        local = {
            source = "hashicorp/local"
            version = "~> 2.5"
        }
        # aws = {
        #     source = "hashicorp/aws"
        #     version = "~> 6.0"
        # }
        # google = {
        #     source = "hashicorp/google"
        # }
    }
}

provider "local" {
  # conf
}

# *resource* *resource_type* *name*

variable "file_name" {
    type = string
    default = "hello.txt"
}

variable "is_sensitve" {
    type = bool
    default = true
  
}

resource "local_file" "hello_world" {
    filename = var.file_name
    content = "hello wolrd !!! \n yabadaba doooo"
    file_permission = "0777"
}

resource "local_file" "file_lists" {
    filename = "ls.txt"
    content = local_file.hello_world.id
}

resource "local_sensitive_file" "secret" {
    filename = "secrets.txt"
    content = "pizza"
}

output "secret_id" {
  value = var.is_sensitve ? local_sensitive_file.secret.id : "noope"
}

output "file_lists" {
  value = local_file.hello_world.content_base64sha256
}