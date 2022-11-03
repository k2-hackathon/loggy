locals {
  resource_group_required_tags = {}
  resource_group_tags          = merge(var.resource_tags, local.resource_group_required_tags)

  resource_group_name = local.prefix
}

resource "aws_resourcegroups_group" "resource_group" {
  # https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/resourcegroups_group
  name = local.resource_group_name

  resource_query {
    query = jsonencode({
      ResourceTypeFilters = ["AWS::AllSupported"],
      TagFilters = [
        for key, value in local.resource_group_tags :
        {
          Key : key,
          Values : [value],
        }
      ]
    })
  }

  tags = local.resource_group_tags
}
