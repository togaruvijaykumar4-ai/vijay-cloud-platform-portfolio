```mermaid
flowchart TD
  U[Internet] --> R[Route 53]
  R --> A[Application Load Balancer]
  A --> EC2[EC2 Auto Scaling]
  EC2 --> DB[RDS]
  EC2 --> S3[S3]
  EC2 --> CW[CloudWatch]
  EC2 --> IAM[IAM Role]
```
