import json
import os
import boto3

s3 = boto3.client("s3")

def handler(event, context):
    # Portfolio-safe example: record the event rather than making destructive changes.
    bucket = os.environ.get("AUDIT_BUCKET")
    record = {
        "source": event.get("source"),
        "detail_type": event.get("detail-type"),
        "detail": event.get("detail", {}),
    }

    if bucket:
        key = f"security-events/{context.aws_request_id}.json"
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=json.dumps(record).encode("utf-8"),
            ContentType="application/json",
        )

    return {"statusCode": 200, "body": json.dumps({"recorded": True})}
