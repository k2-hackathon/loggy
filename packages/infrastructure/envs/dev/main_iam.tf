locals {
  iam_required_tags = {}
  iam_tags          = merge(var.resource_tags, local.iam_required_tags)

  iam_role_task_execution_name = "${local.prefix}-iam_role_task_execution"

  iam_role_task_execution_arn = resource.aws_iam_role.iam_role_task_execution.arn
}

# NOTE: sample policy
resource "aws_iam_role" "iam_role_task_execution" {
  name = local.iam_role_task_execution_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "ec2.amazonaws.com"
        }
      },
    ]
  })


  inline_policy {
    name = "inline_${local.iam_role_task_execution_name}"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action   = ["ec2:Describe*"]
          Effect   = "Allow"
          Resource = "*"
        },
      ]
    })
  }

  tags = local.iam_tags
}
