Bootstrap and deploy instructions

1) Create backend resource (S3 bucket) in your regional account

From `infra/bootstrap` run:

```bash
cd infra/bootstrap
# If you want Terraform to create the bucket in this region/account:
terraform init
terraform apply -var='bucket_name=your-unique-bucket-name' -auto-approve

# If you already have a regional (account-scoped) bucket and want to use it
# instead of creating one, set create_bucket=false. The bootstrap will reference
# the existing bucket rather than attempting to create it.
terraform apply -var='bucket_name=existing-bucket-name' -var='create_bucket=false' -auto-approve
```

Note the output `bucket_name`.

2) Initialize the main infra with the backend config created above

From `infra` run:

```bash
cd infra
terraform init \
  -backend-config="bucket=THE_BUCKET_NAME" \
  -backend-config="region=us-east-1"

terraform apply -var='aws_region=us-east-1' -auto-approve
```

This will:
- create an ECR repository
- build & push the Docker image from the project root (requires Docker and AWS CLI credentials locally)
- create a Lambda function (container image) using the pushed image
- create an API Gateway HTTP API that routes all inbound requests to the Lambda

Notes & cautions:
- The `null_resource` uses `local-exec` to run `docker build` and `docker push` using your local Docker and AWS CLI credentials.
- Ensure `docker` and `aws` CLI are installed and authenticated prior to running `terraform apply`.
- For CI pipelines, prefer building/pushing the image in the pipeline and set `image_tag` to the pushed image tag, then run Terraform without the local-exec step.
