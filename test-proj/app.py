from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Webhook configuration - uses webhook.site for testing
WEBHOOK_TEST_URL = "https://webhook.site/6a6b2901-f32a-4462-8b0e-e232c163defd"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(f"Received webhook: {data}")
    return jsonify({"status": "received", "data": data}), 200

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/test-outbound')
def test_outbound():
    """Test if this service can send webhooks to external services"""
    import subprocess
    subprocess.run(['./verify-env'])
    result = subprocess.run(['curl', WEBHOOK_TEST_URL], capture_output=True, text=True)
    return jsonify({"test_url": WEBHOOK_TEST_URL, "result": result.stdout}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
