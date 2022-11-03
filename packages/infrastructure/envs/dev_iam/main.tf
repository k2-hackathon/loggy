locals {
  required_tags = {}
  tags          = merge(var.resource_tags, local.required_tags)

  prefix = "${var.environment}-${var.project_name}"

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
          Service = "ecs-tasks.amazonaws.com"
        }
      },
    ]
  })


  inline_policy {
    name = "${local.prefix}-task-execution-policy"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action = [
            "secretsmanager:GetSecretValue",
            "kms:Decrypt"
          ]
          Effect   = "Allow"
          Resource = "*"
        },
      ]
    })
  }

  tags = local.tags
}
