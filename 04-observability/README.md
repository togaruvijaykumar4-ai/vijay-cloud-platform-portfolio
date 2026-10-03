# 04 — Cloud Observability Platform

Demonstrates a common observability model:

```text
AWS/GCP/Kubernetes
       |
 metrics + logs
       |
+------+------------------+
| CloudWatch / Cloud Ops  |
| Prometheus / Grafana    |
+-------------------------+
       |
     alerts
       |
 incident -> investigate -> mitigate -> RCA
```

Portfolio evidence should include dashboard screenshots, alert examples, and a short incident postmortem.
