from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__, template_folder="templates")

APP_NAME = os.getenv("APP_NAME", "Fake  Service")
APP_VERSION = os.getenv("APP_VERSION", "1.2")  # default 1.2

@app.get("/")
def home():
    # GUI page
    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        now=datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        health="healthy" if APP_VERSION != "1.3" else "unhealthy",
    )

@app.get("/health")
def health():
    # Health endpoint (1.3 simulates failure)
    if APP_VERSION == "1.3":
        return jsonify(status="unhealthy", version=APP_VERSION), 500
    return jsonify(status="healthy", version=APP_VERSION), 200

@app.get("/version")
def version():
    return jsonify(version=APP_VERSION), 200

if __name__ == "__main__":
    # Important: bind to 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=8080)
