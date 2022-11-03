locals {
  subnet_required_tags = {}
  subnet_tags          = merge(var.resource_tags, local.subnet_required_tags)

  public_subnet_a_id = resource.aws_subnet.public-subnet-a.id
  public_subnet_c_id = resource.aws_subnet.public-subnet-c.id
}

# NOTE: application public-subnet-a
resource "aws_subnet" "public-subnet-a" {
  vpc_id = aws_vpc.vpc.id

  cidr_block        = "10.2.1.0/26"
  availability_zone = "ap-northeast-1a"

  map_public_ip_on_launch = true

  depends_on = [
    aws_internet_gateway.igw
  ]

  tags = local.subnet_tags
}

# NOTE: application public-subnet-c
resource "aws_subnet" "public-subnet-c" {
  vpc_id = aws_vpc.vpc.id

  cidr_block        = "10.2.2.0/26"
  availability_zone = "ap-northeast-1c"

  map_public_ip_on_launch = true

  depends_on = [
    aws_internet_gateway.igw
  ]

  tags = local.subnet_tags
}
