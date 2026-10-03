# 05 — AWS Security Monitoring & Automated Remediation

## Flow

```text
CloudTrail
   |
EventBridge
   |
Lambda (Python)
   |
remediation action
   |
CloudWatch / SNS / S3 audit trail
```

Only automate narrowly defined, reversible actions. Test in a dedicated sandbox account.
