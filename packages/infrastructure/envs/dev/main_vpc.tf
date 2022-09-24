locals {
  vpc_required_tags = {}
  vpc_tags          = merge(var.resource_tags, local.vpc_required_tags)
  igw_required_tags = {
    Name : "igw"
  }
  igw_tags = merge(var.resource_tags, local.igw_required_tags)

  vpc_name = "${local.prefix}-vpc"
}

resource "aws_vpc" "vpc" {
  cidr_block = "10.2.0.0/16"
  tags       = local.vpc_tags
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id
  tags   = local.igw_tags
}
