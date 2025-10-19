from flask import Flask, jsonify, request, Response
import requests, os

app = Flask(__name__)

@app.route("/model/<name>")
def get_model(name):
    url = f"https://stripchat.global/api/front/v2/models/username/{name}/cam"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://stripchat.global/",
        "Origin": "https://stripchat.global"
    }
    if "Cookie" in request.headers:
        headers["Cookie"] = request.headers["Cookie"]

    r = requests.get(url, headers=headers, timeout=10)
    return Response(r.content, status=r.status_code, content_type=r.headers.get("Content-Type", "application/json"))

@app.route("/health")
def health():
    return jsonify({"ok": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
