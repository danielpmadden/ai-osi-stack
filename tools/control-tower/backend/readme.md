<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Governance Control Tower API

Run locally:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Environment variables:
- `GOVERNANCE_SLACK_WEBHOOK` – optional Slack webhook for alerts.
- `GOVERNANCE_GITHUB_WEBHOOK` – optional GitHub webhook endpoint.
