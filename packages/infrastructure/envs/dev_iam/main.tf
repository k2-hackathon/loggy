locals {
  required_tags = {}
  tags          = merge(var.resource_tags, local.required_tags)
  prefix        = "${var.environment}-${var.project_name}"
}

# NOTE: sample policy
module "resource_group_full_access_policy" {
  # ref:  https://registry.terraform.io/modules/terraform-aws-modules/iam/aws/latest
  source  = "terraform-aws-modules/iam/aws//modules/iam-policy"
  version = "3.6.0"

  name        = "resource_group_full_access"
  path        = "/"
  description = "This policy is for use with loggy iam terraform."

  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:Describe*"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}
