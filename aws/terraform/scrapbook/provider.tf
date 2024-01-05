terraform {
  required_version = "= 1.6.4"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "= 5.26.0"
    }
  }
}

provider "aws" {
  region = "ap-northeast-1"
  profile = "8-admin"
  assume_role {
    role_arn     = "arn:aws:iam::645223824092:role/TerraformApplyRole"
    session_name = "terraform-scrapbook"
  }
}
