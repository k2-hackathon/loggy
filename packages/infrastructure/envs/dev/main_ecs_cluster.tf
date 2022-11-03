locals {
  ecs_cluster_required_tags = {}
  ecs_cluster_tags          = merge(var.resource_tags, local.ecs_cluster_required_tags)

  ecs_cluster_name = local.prefix
  ecs_task_family  = local.prefix

  ecs_cluster_arn     = module.ecs_cluster.cluster_arn
  task_definition_arn = resource.aws_ecs_task_definition.ecs_task_definition.arn
}

module "ecs_cluster" {
  # ref: https://registry.terraform.io/modules/terraform-aws-modules/ecs/aws/latest
  source  = "terraform-aws-modules/ecs/aws"
  version = "4.1.0"

  cluster_name = local.ecs_cluster_name

  fargate_capacity_providers = {
    FARGATE = {
    }
  }

  tags = local.ecs_cluster_tags
}

data "template_file" "task_definitions" {
  # ref: https://registry.terraform.io/providers/hashicorp/template/latest
  template = file("./task_definition.json")

  vars = {
    container_nginx_name    = "loggy-nginx"
    container_nginx_image   = "${local.account_id}.dkr.ecr.ap-northeast-1.amazonaws.com/d0-loggy-nginx"
    container_fastapi_name  = "loggy-fastapi"
    container_fastapi_image = "${local.account_id}.dkr.ecr.ap-northeast-1.amazonaws.com/d0-loggy-fastiapi"
  }
}

resource "aws_ecs_task_definition" "ecs_task_definition" {
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_task_definition
  family = local.ecs_task_family

  requires_compatibilities = ["FARGATE"]

  cpu          = 256
  memory       = 512
  network_mode = "awsvpc"

  task_role_arn      = local.iam_role_task_execution_arn
  execution_role_arn = local.iam_role_task_execution_arn

  container_definitions = data.template_file.task_definitions.rendered

  lifecycle {
    ignore_changes = [
      container_definitions,
    ]
  }

  tags = local.ecs_cluster_tags
}
