# ECR
locals {
  ecr_required_tags = {}
  ecr_tags          = merge(var.resource_tags, local.ecr_required_tags)

  fastapi_ecr_name = "${local.prefix}-fastapi"
  nginx_ecr_name   = "${local.prefix}-nginx"
}

resource "aws_ecr_repository" "fastapi" {
  name                 = local.fastapi_ecr_name
  image_tag_mutability = "MUTABLE"

  tags = local.ecr_tags
}

resource "aws_ecr_repository" "nginx" {
  name                 = local.nginx_ecr_name
  image_tag_mutability = "MUTABLE"

  tags = local.ecr_tags
}

