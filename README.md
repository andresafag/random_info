# Random Rush 🌩️

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Faker](https://img.shields.io/badge/Faker-40.19.1-ff6f00)](https://faker.readthedocs.io/)
[![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?logo=terraform&logoColor=white)](https://www.terraform.io/)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/lambda/)
[![Amazon ECR](https://img.shields.io/badge/AWS-ECR-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/ecr/)
[![API Gateway](https://img.shields.io/badge/AWS-API%20Gateway-FF9900?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/api-gateway/)
[![Docker](https://img.shields.io/badge/Docker-container-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

![Random Rush](./static/randomrush.png)

## Overview

**Random Rush** is a serverless web application that generates random fake data across multiple categories using the [Faker](https://faker.readthedocs.io/) library. Select a category, choose how many results you need, pick a locale, and download everything as a CSV — all from a browser, no setup required.

🔗 **Live app:** [https://i6ie3zeuy7.execute-api.us-east-1.amazonaws.com](https://i6ie3zeuy7.execute-api.us-east-1.amazonaws.com)

---

## Features

- Generate random data for: `name`, `address`, `date`, `text`, `credit_card`, `email`, `phone_number`, `colors`, `company`
- Locale support for internationalized fake data
- Download results as a CSV file
- Fully serverless — no servers to manage

---

## Tech Stack

| Layer | Technology |
|---|---|
| Application | Python 3.11, Flask 3.1.3, Faker |
| Containerization | Docker (AWS Lambda base image) |
| Container Registry | Amazon ECR |
| Compute | AWS Lambda (container image) |
| HTTP Endpoint | Amazon API Gateway HTTP API (v2) |
| IAM | AWS IAM role with `AWSLambdaBasicExecutionRole` |
| Infrastructure as Code | Terraform |
| State Backend | S3 (with native S3 locking) |

---

## Architecture

```
User → API Gateway HTTP API → Lambda (container) → Flask app
                                      ↑
                               Image pulled from ECR
```

Terraform provisions all resources in the correct dependency order:

1. **ECR repository** — stores the Docker image
2. **Docker build & push** — builds the image locally and pushes it to ECR
3. **IAM role** — execution role for Lambda
4. **Lambda function** — runs the container image
5. **API Gateway** — HTTP API with a `$default` catch-all route to Lambda

---

## Infrastructure Deployment

### Prerequisites

- [Terraform](https://developer.hashicorp.com/terraform/install) >= 1.0
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) configured with credentials that have permissions for ECR, Lambda, IAM, and API Gateway

### 1. Create the S3 backend bucket

```bash
cd infra/bootstrap
terraform init
terraform apply -var='bucket_name=your-unique-bucket-name' -auto-approve
```

Note the `bucket_name` output.

### 2. Deploy the full stack

```bash
cd infra
terraform init \
  -backend-config="bucket=YOUR_BUCKET_NAME" \
  -backend-config="region=us-east-1"

terraform apply -var='aws_region=us-east-1' -auto-approve
```

Terraform will:
- Create the ECR repository
- Build the Docker image from the project root and push it to ECR
- Create the Lambda function using the pushed image
- Create the API Gateway HTTP API wired to Lambda

The `api_endpoint` output is your live URL.

### Tear down

```bash
terraform destroy -var='aws_region=us-east-1' -auto-approve
```

### Updating the application

After modifying application code, rebuild and push the image, then update Lambda:

```bash
cd infra
terraform taint module.ecr.null_resource.docker_build_and_push
terraform apply -var='aws_region=us-east-1' -auto-approve

aws lambda update-function-code \
  --function-name random-info-web-adapter \
  --image-uri <account>.dkr.ecr.us-east-1.amazonaws.com/random-info-app:latest \
  --region us-east-1
```

---

## Terraform Module Reference

| Module | Purpose |
|---|---|
| `modules/ecr` | Creates the ECR repo and runs `docker build` + `docker push` via `local-exec` |
| `modules/iam` | Creates the Lambda execution IAM role |
| `modules/lambda` | Creates the Lambda function from the ECR container image |
| `modules/apigateway` | Creates the HTTP API, integration, route, stage, and Lambda permission |

### Key variables (`infra/variable.tf`)

| Variable | Default | Description |
|---|---|---|
| `aws_region` | `us-east-1` | AWS region |
| `ecr_repo_name` | `random-info-app` | ECR repository name |
| `image_tag` | `latest` | Docker image tag |
| `lambda_name` | `random-info-web-adapter` | Lambda function name |

---

## Application Routes

| Route | Description |
|---|---|
| `GET /` | Landing page |
| `GET /allow/<category>` | Selection page for a category |
| `GET /allow/<category>/<count>/<locale>` | Generate `count` items using Faker locale |
| `GET /allow/<category>/<count>/<start>/<end>/` | Generate random dates between two dates |
| `POST /download/` | Download current results as CSV |

---

## Notes

- Docker and AWS CLI must be available locally when running `terraform apply` — the ECR module uses `local-exec` to build and push the image.
- For CI/CD pipelines, build and push the image in the pipeline first, then run `terraform apply` with the image already in ECR.
- Lambda uses `x86_64` architecture matching the `linux/amd64` Docker build platform.
- The WSGI adapter is `serverless-wsgi`, which handles API Gateway HTTP API v2 payload format natively.
