terraform {
  backend "s3" {
    key          = "terraform.tfstate"
    use_lockfile = true
    region       = "us-east-1"
  }
  required_version = ">= 1.0"
}
