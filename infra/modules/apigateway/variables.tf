variable "lambda_function_arn" {
  description = "The Lambda function ARN (or name) to integrate with API Gateway"
  type        = string
}

variable "lambda_name" {
  description = "Lambda name used to name API"
  type        = string
  default     = "random_info_web_adapter"
}

variable "aws_region" {
  description = "AWS region where API and Lambda live"
  type        = string
}
