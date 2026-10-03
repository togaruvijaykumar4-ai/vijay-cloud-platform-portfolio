# 07 — AWS + GCP Multi-Cloud Reference Architecture

## Service mapping

| Capability | AWS | GCP |
|---|---|---|
| Compute | EC2 | Compute Engine |
| Kubernetes | EKS | GKE |
| Object storage | S3 | Cloud Storage |
| Serverless | Lambda | Cloud Run / Cloud Functions |
| IAM | IAM | Cloud IAM |
| Monitoring | CloudWatch | Cloud Monitoring |
| Logging | CloudWatch Logs | Cloud Logging |
| Streaming | Kinesis | Pub/Sub |
| Registry | ECR | Artifact Registry |
| DNS | Route 53 | Cloud DNS |

The goal is to show platform design thinking without claiming a production cross-cloud deployment.
