from flask import Flask, jsonify, request
import requests, time

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"ok": True})

@app.route("/model/<name>")
def model_status(name):
    start = time.time()
    url = f"https://stripchat.global/api/front/v2/models/username/{name}"
    r = requests.get(url)
    duration = round(time.time() - start, 2)
    
    if r.status_code != 200:
        return jsonify({
            "status": r.status_code,
            "model": name,
            "time": duration,
            "message": "API unreachable"
        }), r.status_code

    data = r.json().get("cam", {})
    return jsonify({
        "status": 200,
        "model": name,
        "time": duration,
        "isCamAvailable": data.get("isCamAvailable"),
        "streamName": data.get("streamName")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
