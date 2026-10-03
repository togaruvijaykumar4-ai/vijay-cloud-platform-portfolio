import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
bedrock = boto3.client("bedrock-runtime")

def handler(event, context):
    body = json.loads(event.get("body") or "{}")
    prompt = body.get("prompt", "Explain cloud infrastructure in one sentence.")

    # Keep model invocation disabled until a model/access policy is configured.
    result = {
        "prompt": prompt,
        "status": "ready",
        "message": "Configure Bedrock model access and IAM before enabling inference."
    }

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(result)
    }
