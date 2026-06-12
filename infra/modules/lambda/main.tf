resource "aws_lambda_function" "app" {
  function_name = var.function_name
  package_type  = "Image"
  image_uri     = var.image_digest != "" ? "${var.repository_url}@${var.image_digest}" : "${var.repository_url}:${var.image_tag}"
  role          = var.role_arn
  architectures = ["x86_64"]
  timeout       = 30
  memory_size   = 512
}
