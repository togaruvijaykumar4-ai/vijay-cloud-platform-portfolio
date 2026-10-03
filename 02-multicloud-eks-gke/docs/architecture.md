```mermaid
flowchart LR
  G[GitHub] --> T[Terraform]
  T --> E[EKS]
  T --> K[GKE]
  E --> A[AWS Workloads]
  K --> B[GCP Workloads]
  A --> M[Cloud Monitoring]
  B --> M
```
