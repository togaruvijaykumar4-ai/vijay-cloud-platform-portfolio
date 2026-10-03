import json
import os
import random
import time
import boto3

stream = os.environ["KINESIS_STREAM"]
client = boto3.client("kinesis")

for i in range(10):
    event = {
        "event_id": i,
        "product": random.choice(["cloud", "devops", "data"]),
        "value": random.randint(1, 100),
        "timestamp": int(time.time())
    }
    client.put_record(
        StreamName=stream,
        Data=json.dumps(event).encode(),
        PartitionKey=str(event["event_id"])
    )
    print(event)
