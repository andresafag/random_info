variable "function_name" {
  description = "Lambda function name"
  type        = string
}

variable "repository_url" {
  description = "ECR repository URL (without tag)"
  type        = string
}

variable "image_tag" {
  description = "Image tag to use for the Lambda image"
  type        = string
}

variable "image_digest" {
  description = "Optional image digest (sha256:...). If set, this will be used instead of tag for image_uri."
  type        = string
  default     = ""
}

variable "role_arn" {
  description = "IAM role ARN for Lambda to assume"
  type        = string
}
