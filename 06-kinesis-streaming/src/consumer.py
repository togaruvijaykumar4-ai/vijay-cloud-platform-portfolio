import base64
import json

def handler(event, context):
    records = []
    for item in event.get("Records", []):
        raw = base64.b64decode(item["kinesis"]["data"]).decode()
        records.append(json.loads(raw))
    print(json.dumps({"records": records}))
    return {"processed": len(records)}
