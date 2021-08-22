variable "region" {
  default     = "us-east-1"
  description = "AWS US Virginia region"
}

provider "aws" {
  profile = "default"
  region  = var.region
}

locals {
  cluster_name = "my-eks"
  vpc_id       = "vpc-d8f23ea5"
  subnets      = ["subnet-73ffbf3e", "subnet-3d0db062"]
}

terraform {
  backend "s3" {
    bucket  = "eks-terraform-state-files"
    key     = "eks-terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}
