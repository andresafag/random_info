terraform {
  backend "s3" {
    key          = "terraform.tfstate"
    use_lockfile = true
  }
  required_version = ">= 1.0"
}
