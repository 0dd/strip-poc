# Webhook Receiver Service

A Flask service for receiving and testing webhook integrations.

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## Endpoints

### POST /webhook
Receives webhook payloads from external services.

```bash
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"event": "test"}'
```

### GET /health
Health check endpoint.

```bash
curl http://localhost:5000/health
```

### GET /test-outbound
Tests if the service can send webhooks to external services.
Uses webhook.site as a test endpoint to verify outbound connectivity.

```bash
curl http://localhost:5000/test-outbound
```

This is useful for verifying firewall rules and network configuration
before integrating with production webhook providers.

## Development

The service includes a test webhook endpoint configured in the code
for validating outbound webhook delivery during development.
