# Vijay Kumar Togaru — AWS / GCP Cloud Platform Engineering Portfolio

A hands-on, GitHub-ready portfolio demonstrating cloud platform engineering across AWS and Google Cloud Platform.

## Portfolio map

| # | Project | Main technologies |
|---|---|---|
| 01 | AWS 3-Tier Production Infrastructure | AWS, Terraform, EC2, ALB, RDS, VPC, IAM |
| 02 | Multi-Cloud EKS/GKE Platform | AWS, GCP, Terraform, EKS, GKE, Kubernetes |
| 03 | Kubernetes GitOps CI/CD | Docker, ECR, EKS, Helm, Argo CD, GitHub Actions |
| 04 | Cloud Observability Platform | CloudWatch, GCP Monitoring/Logging, Prometheus, Grafana |
| 05 | AWS Security Monitoring & Remediation | IAM, CloudTrail, EventBridge, Lambda, Python |
| 06 | AWS Kinesis Streaming Platform | Kinesis, Lambda, S3, OpenSearch, Python |
| 07 | AWS + GCP Multi-Cloud Reference Architecture | AWS, GCP, Terraform, networking, IAM |
| 08 | Serverless AI / Bedrock Platform | Lambda, API Gateway, DynamoDB, S3, Bedrock |
| 09 | Cloud Disaster Recovery | AWS Backup, RDS, Route 53, Terraform, CloudFormation |

## Skills demonstrated

AWS • GCP • Terraform • Kubernetes • EKS • GKE • Docker • Helm • Argo CD • GitHub Actions • Python • Bash • Linux • IAM • VPC • DNS • Load Balancing • CloudWatch • Cloud Logging • Prometheus • Grafana • CloudTrail • EventBridge • Kinesis • OpenSearch • Serverless • Disaster Recovery • GitOps

## Important

This repository is a portfolio of hands-on projects. It does **not** represent 5–8 years of professional employment experience.

## Colab workflow

1. Open Google Colab.
2. Clone this repository.
3. Run the project-specific `colab/setup.sh` commands in Colab cells using `!`.
4. Authenticate to AWS/GCP only when you intentionally deploy.
5. Run `terraform fmt`, `terraform validate`, and `terraform plan` before applying.
6. Destroy cloud resources after testing to control cost.

## Cost discipline

Many components in this portfolio can create billable resources. Never run `terraform apply` blindly. Review the plan, use the smallest practical instance/node sizes, set budgets/alerts, and destroy temporary environments after testing.
