locals {
  sg_required_tags = {}
  sg_tags          = merge(var.resource_tags, local.sg_required_tags)

  security_group_ecs_name       = "${local.prefix}-ecs-sg"
  security_group_alb_http_name  = "${local.prefix}-alb-http-sg"
  security_group_alb_https_name = "${local.prefix}-alb-https-sg"

  security_group_ecs_id       = module.security_group_ecs.security_group_id
  security_group_alb_http_id  = module.security_group_alb_http.security_group_id
  security_group_alb_https_id = module.security_group_alb_https.security_group_id
}

module "security_group_ecs" {
  # ref: https://registry.terraform.io/modules/terraform-aws-modules/security-group/aws/latest
  source = "terraform-aws-modules/security-group/aws"

  name   = local.security_group_ecs_name
  vpc_id = aws_vpc.vpc.id

  ingress_cidr_blocks = ["0.0.0.0/0"]
  /** TODO: ロードバランサー経由のみを許可するように修正 */
  ingress_rules = ["http-80-tcp", "https-443-tcp"]

  egress_cidr_blocks = ["0.0.0.0/0"]
  egress_rules       = ["all-all"]
}

module "security_group_alb_http" {
  # ref: https://registry.terraform.io/modules/terraform-aws-modules/security-group/aws/latest
  source = "terraform-aws-modules/security-group/aws"

  name   = local.security_group_alb_http_name
  vpc_id = aws_vpc.vpc.id

  ingress_cidr_blocks = ["0.0.0.0/0"]
  ingress_rules       = ["http-80-tcp"]

  egress_cidr_blocks = ["0.0.0.0/0"]
  egress_rules       = ["all-all"]
}


module "security_group_alb_https" {
  # ref: https://registry.terraform.io/modules/terraform-aws-modules/security-group/aws/latest
  source = "terraform-aws-modules/security-group/aws"

  name   = local.security_group_alb_https_name
  vpc_id = aws_vpc.vpc.id

  ingress_cidr_blocks = ["0.0.0.0/0"]
  ingress_rules       = ["https-443-tcp"]

  egress_cidr_blocks = ["0.0.0.0/0"]
  egress_rules       = ["all-all"]
}
