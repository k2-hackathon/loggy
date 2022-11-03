variable "project_name" {
  description = "Name of the project."
  type        = string
  default     = "loggy"
}

variable "environment" {
  description = "Name of the environment."
  type        = string
  default     = "d0"
}

variable "resource_tags" {
  description = "Tags to set for all resources"
  type        = map(string)
  default = {
    env     = "dev"
    service = "loggy"
    created = "terraform"
  }
}
