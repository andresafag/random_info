output "api_endpoint" {
  description = "HTTP API endpoint (invoke this to reach the Lambda adapter)"
  value       = module.apigateway.api_endpoint
}

output "lambda_function_name" {
  description = "Deployed Lambda function name"
  value       = module.lambda.function_name
}

output "ecr_repository_url" {
  description = "ECR repository URL"
  value       = module.ecr.repository_url
}

output "lambda_invoke_arn" {
  description = "ARN to invoke the Lambda function"
  value       = module.lambda.lambda_invoke_arn
}

