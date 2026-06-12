variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-east-1"
}

variable "ecr_repo_name" {
  description = "Name of the ECR repository"
  type        = string
  default     = "random-info-app"
}

variable "image_tag" {
  description = "Tag to push/use for the Docker image"
  type        = string
  default     = "latest"
}

variable "lambda_name" {
  description = "Name for the Lambda function"
  type        = string
  default     = "random-info-web-adapter"
}


variable "backend_bucket" {
  description = "(bootstrap) S3 bucket for Terraform state; used during init as backend-config"
  type        = string
  default     = ""
}

variable "backend_table" {
  description = "(bootstrap) DynamoDB table for Terraform locks; used during init as backend-config"
  type        = string
  default     = ""
}

