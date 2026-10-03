# 08 — Serverless AI / Bedrock Platform

```text
Client
  |
API Gateway
  |
Lambda (Python)
  |---- DynamoDB
  |---- S3
  |
Amazon Bedrock
```

The Bedrock call is intentionally isolated in a helper so the application can be tested without invoking a model. Never hard-code credentials.
