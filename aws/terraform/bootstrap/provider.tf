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
}
