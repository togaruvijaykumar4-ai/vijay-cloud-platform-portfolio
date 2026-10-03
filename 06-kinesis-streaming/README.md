# 06 — AWS Kinesis Streaming Platform

```text
Producer -> Kinesis Data Stream -> Lambda -> S3
                                      |
                                      +-> OpenSearch (optional)
                                      |
                                  CloudWatch
```

Use small test workloads and delete the stream, Lambda, buckets, and OpenSearch resources after validation.
