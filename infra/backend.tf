terraform {
  backend "s3" {
    bucket = "randomize-it-688567305851-us-east-1-an"
    key    = "terraform.tfstate"
    region = "us-east-1"


    # Habilita el bloqueo de estado nativo de S3 (sin necesidad de DynamoDB)
    use_lockfile = true
  }
  required_version = ">= 1.0"
}
