terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
  backend "s3" {
    region = "ap-northeast-1"
    bucket = "k2-tfstate"
    key    = "dev/loggy-dev-iam.tfstate"
  }
}

provider "aws" {
  region = "ap-northeast-1"
}
