data "aws_caller_identity" "current" {}

resource "aws_ecr_repository" "this" {
  name = var.name
  image_tag_mutability = "MUTABLE"
  force_delete = true
  image_scanning_configuration {
    scan_on_push = true
  }
}

resource "null_resource" "docker_build_and_push" {
  provisioner "local-exec" {
    command     = <<EOT
  aws ecr get-login-password --region ${var.aws_region} | docker login --username AWS --password-stdin ${data.aws_caller_identity.current.account_id}.dkr.ecr.${var.aws_region}.amazonaws.com
  if [ -n "${var.dockerfile}" ]; then
    docker build --platform ${var.platform} --provenance=false --output type=docker -f "${var.dockerfile}" -t ${aws_ecr_repository.this.repository_url}:${var.image_tag} "${var.build_context}"
  else
    docker build --platform ${var.platform} --provenance=false --output type=docker -t ${aws_ecr_repository.this.repository_url}:${var.image_tag} "${var.build_context}"
  fi
  docker push ${aws_ecr_repository.this.repository_url}:${var.image_tag}
  EOT
    interpreter = ["/bin/bash", "-c"]
    environment = {
      AWS_DEFAULT_REGION = var.aws_region
    }
  }

  depends_on = [aws_ecr_repository.this]
}
