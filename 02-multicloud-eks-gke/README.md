# 02 — Multi-Cloud Kubernetes Platform: EKS + GKE

## Goal
Demonstrate AWS/GCP Kubernetes platform engineering, Terraform, Helm, containerization, networking, and workload portability.

```text
                 GitHub
                   |
          +--------+--------+
          |                 |
       Terraform          GitOps
          |                 |
      +---+---+         +---+---+
      | AWS   |         | GCP   |
      | EKS   |         | GKE   |
      +---+---+         +---+---+
          |                 |
       app pods           app pods
```

The starter Terraform files are intentionally small and reviewable. Add provider-specific cluster modules after validating cloud quotas and costs.
