provider "aws" {
  region = var.aws_region
}

module "ecr" {
  source        = "./modules/ecr"
  name          = var.ecr_repo_name
  image_tag     = var.image_tag
  aws_region    = var.aws_region
  build_context = abspath("${path.module}/..")
  dockerfile    = abspath("${path.module}/../Dockerfile")
}

module "iam" {
  source      = "./modules/iam"
  lambda_name = var.lambda_name
}

module "lambda" {
  source         = "./modules/lambda"
  function_name  = var.lambda_name
  repository_url = module.ecr.repository_url
  image_tag      = var.image_tag
  role_arn       = module.iam.role_arn
  depends_on     = [module.ecr, module.iam]
}

module "apigateway" {
  source              = "./modules/apigateway"
  lambda_function_arn = module.lambda.lambda_invoke_arn
  lambda_name         = module.lambda.function_name
  aws_region          = var.aws_region
  depends_on          = [module.lambda]
}

