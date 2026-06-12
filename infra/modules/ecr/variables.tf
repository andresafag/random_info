variable "name" {
  description = "ECR repository name"
  type        = string
}

variable "image_tag" {
  description = "Image tag to build and push"
  type        = string
}

variable "aws_region" {
  description = "AWS region for docker login"
  type        = string
}

variable "build_context" {
  description = "Filesystem path to the Docker build context (will be used as the docker build directory)"
  type        = string
}

variable "dockerfile" {
  description = "Optional path to the Dockerfile to use for building (absolute or relative to build_context). If empty, `docker build` will use the default Dockerfile in the context."
  type        = string
  default     = ""
}

variable "platform" {
  description = "Optional Docker build platform to force (example: linux/amd64). If empty, Docker will use the default platform on the host."
  type        = string
  default     = "linux/amd64"
}
