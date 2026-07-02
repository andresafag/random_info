output "repository_url" {
  value = aws_ecr_repository.this.repository_url
}

# output "image_push_id" {
#   value = null_resource.docker_build_and_push.id
# }
