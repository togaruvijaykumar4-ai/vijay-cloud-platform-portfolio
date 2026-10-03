# Portfolio Architecture

```text
                         +-----------------------+
                         |       GitHub          |
                         | source + IaC + CI/CD  |
                         +-----------+-----------+
                                     |
                       +-------------+-------------+
                       | GitHub Actions / GitOps   |
                       +-------------+-------------+
                                     |
             +-----------------------+-----------------------+
             |                                               |
      +------v------+                                  +-----v------+
      |     AWS     |                                  |    GCP     |
      | VPC / EKS   |                                  | VPC / GKE  |
      | EC2 / RDS   |                                  | GCE / GCS  |
      +------+------+\                                  +-----+------+
             |                                               |
      +------v------+                                  +-----v------+
      | Monitoring  |                                  | Monitoring |
      | CloudWatch  |                                  | Cloud Ops  |
      +-------------+                                  +-----------+
```

The portfolio intentionally demonstrates the same platform-engineering lifecycle:
**plan → provision → secure → deploy → observe → troubleshoot → recover → destroy**.
