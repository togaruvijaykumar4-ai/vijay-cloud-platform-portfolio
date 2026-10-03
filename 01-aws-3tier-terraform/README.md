# 01 — AWS 3-Tier Production Infrastructure

## Goal
Demonstrate production-style AWS networking, compute, load balancing, managed database infrastructure, IAM, monitoring, and Terraform.

## Architecture

```text
Internet
   |
Route 53
   |
ALB (public subnets)
   |
EC2 Auto Scaling Group (private subnets)
   |
RDS (private DB subnets)

S3 -> static/assets
CloudWatch -> metrics/alarms
IAM -> least privilege
```

## Terraform

```text
terraform/
├── versions.tf
├── variables.tf
├── main.tf
├── outputs.tf
└── security.tf
```

## Commands

```bash
terraform init
terraform fmt -recursive
terraform validate
terraform plan
terraform apply
# test
terraform destroy
```

Do not apply without reviewing cost and the plan.
