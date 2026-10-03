# 03 — Kubernetes GitOps CI/CD

## Pipeline

```text
Git push
  |
GitHub Actions
  |-- test
  |-- build
  |-- docker build
  |-- push image
  |
GitOps repository / manifests
  |
Argo CD
  |
EKS/GKE
```

## Local validation

```bash
docker build -t cloud-demo:local app
docker run -p 8080:8080 cloud-demo:local
```
