# AWS authentication from Colab

Preferred approach: use temporary credentials or an identity mechanism rather than committing keys.

For a controlled sandbox only, environment variables can be used:

```python
import os
os.environ["AWS_ACCESS_KEY_ID"] = "TEMPORARY_VALUE"
os.environ["AWS_SECRET_ACCESS_KEY"] = "TEMPORARY_VALUE"
os.environ["AWS_SESSION_TOKEN"] = "TEMPORARY_VALUE"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
```

Never commit this cell with real credentials. Clear notebook outputs before sharing.
