# GCP authentication from Colab

For interactive experimentation:

```python
from google.colab import auth
auth.authenticate_user()
```

Then use the authenticated Google identity with the GCP tooling. Do not upload service-account JSON files to GitHub.
