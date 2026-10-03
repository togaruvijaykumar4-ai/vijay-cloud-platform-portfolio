```mermaid
flowchart LR
  C[Commit] --> GA[GitHub Actions]
  GA --> REG[Container Registry]
  C --> GIT[GitOps Manifests]
  GIT --> AR[Argo CD]
  AR --> K8[Kubernetes]
  REG --> K8
```
