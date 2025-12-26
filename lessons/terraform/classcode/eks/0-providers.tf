terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

}


locals {
  h = 1
}
provider "aws" {
  region = var.region
}


