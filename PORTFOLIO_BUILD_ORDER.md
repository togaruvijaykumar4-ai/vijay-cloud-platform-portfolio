# Recommended Build Order

## Phase 1 — Foundation
1. Create GitHub repository.
2. Upload this repository.
3. Build project 03 locally/in Colab first: Docker + Python + Kubernetes manifests.
4. Add screenshots and deployment evidence.

## Phase 2 — AWS
5. Build project 01: VPC + EC2/ALB/RDS.
6. Build project 05: CloudTrail/EventBridge/Lambda.
7. Build project 06: Kinesis/Lambda/S3.
8. Build project 09: backup and recovery test.

## Phase 3 — Kubernetes
9. Build project 02: EKS/GKE.
10. Connect project 03 GitOps deployment.
11. Add project 04 monitoring.

## Phase 4 — GCP + AI
12. Build project 07 multi-cloud reference.
13. Build project 08 serverless AI/Bedrock.

## Evidence to capture
- Terraform plan output
- AWS/GCP console architecture/resources
- Kubernetes pods/services
- GitHub Actions successful run
- Argo CD application status
- Monitoring dashboard
- CloudTrail security event
- Kinesis event processed
- Backup/restore test
- Final architecture diagrams

Never upload screenshots containing access keys, tokens, private IPs that you do not want public, or personal account information.
