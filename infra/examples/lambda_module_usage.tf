// Example: pass image_digest directly (pin to a specific digest)
module "random_info_lambda_pinned" {
  source = "../modules/lambda"

  function_name  = "random-info-web-adapter"
  repository_url = "688567305851.dkr.ecr.us-east-1.amazonaws.com/random-info-app"
  image_tag      = "latest"
  # Set image_digest to the sha256 digest returned by ECR (preferred for Lambda)
  image_digest   = "" # e.g. "sha256:012345..."
  role_arn       = aws_iam_role.lambda_role.arn
}

// Example: lookup the digest from ECR and pass it to the module
data "aws_ecr_image" "app_latest" {
  repository_name = "random-info-app"
  image_tag       = "latest"
}

module "random_info_lambda_from_ecr" {
  source = "../modules/lambda"

  function_name  = "random-info-web-adapter"
  repository_url = "688567305851.dkr.ecr.us-east-1.amazonaws.com/random-info-app"
  image_tag      = "latest"
  image_digest   = data.aws_ecr_image.app_latest.image_digest
  role_arn       = aws_iam_role.lambda_role.arn
}

// Notes:
// - If `image_digest` is non-empty the module will use `repository@sha256:...`.
// - The `data.aws_ecr_image` data source requires the calling IAM identity to
//   have `ecr:DescribeImages` permission for the repository.
