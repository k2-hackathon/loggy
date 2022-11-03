locals {
  ecs_service_required_tags = {}
  ecs_service_tags          = merge(var.resource_tags, local.ecs_service_required_tags)

  ecs_service_api_name = "${local.prefix}-api"

  alb_api_name = "${local.prefix}-api-alb"
  #   alb_api_https_arns = module.alb_api.https_listener_arns
}

resource "aws_ecs_service" "ecs_service_api" {
  # ref: https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ecs_service
  cluster         = local.ecs_cluster_arn
  task_definition = local.task_definition_arn

  name = local.ecs_service_api_name

  desired_count    = 1
  launch_type      = "FARGATE"
  platform_version = "1.4.0"

  enable_execute_command = true

  health_check_grace_period_seconds = 60

  # deployment_controller {
  #   type = "CODE_DEPLOY"
  # }

  network_configuration {
    assign_public_ip = true

    subnets = [
      local.public_subnet_a_id,
      local.public_subnet_c_id,
    ]
    security_groups = [
      local.security_group_ecs_id,
    ]
  }

  load_balancer {
    target_group_arn = module.alb_api.target_group_arns[0]

    container_name = "loggy-nginx"
    container_port = 80
  }

  lifecycle {
    ignore_changes = [
      task_definition,
      desired_count,
      load_balancer,
    ]
  }

  tags = local.ecs_service_tags
}


module "alb_api" {
  # ref: https://registry.terraform.io/modules/terraform-aws-modules/alb/aws/latest
  source  = "terraform-aws-modules/alb/aws"
  version = "~> 6.0"

  name = local.alb_api_name

  load_balancer_type = "application"

  vpc_id = aws_vpc.vpc.id
  subnets = [
    local.public_subnet_a_id,
    local.public_subnet_c_id,
  ]
  security_groups = [
    local.security_group_alb_http_id,
    local.security_group_alb_https_id,
  ]

  idle_timeout = 30

  #   listener_ssl_policy_default = 

  #   access_logs = {
  #     bucket = 
  #   }

  target_groups = [
    {
      name = "${local.alb_api_name}-b"

      target_type = "ip"

      backend_port     = 80
      backend_protocol = "HTTP"

      deregistration_delay = 300

      health_check = {
        # port     = "traffic-port"
        # protocol = "HTTP"
        path    = "/"
        matcher = 200

        # healthy_threshold   = 5
        # unhealthy_threshold = 2

        # timeout  = 5
        # interval = 30
      }
    },
    {
      name = "${local.alb_api_name}-g"

      target_type = "ip"

      backend_port     = 80
      backend_protocol = "HTTP"

      deregistration_delay = 300

      health_check = {
        # port     = "traffic-port"
        # protocol = "HTTP"
        path    = "/"
        matcher = 200

        # healthy_threshold   = 5
        # unhealthy_threshold = 2

        # timeout  = 5
        # interval = 30
      }
    }
  ]

  #   https_listeners = [
  # {
  #   port     = 443
  #   protocol = "HTTPS"

  #   certificate_arn = local.certificate_arn

  #   target_group_index = 0
  # },
  #   ]

  http_tcp_listeners = [
    {
      port     = 80
      protocol = "HTTP"

      target_group_index = 0
    },
  ]
}
