from flask import Flask, jsonify
from flask_cors import CORS
import os
import socket
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "DevOps Platform API",
        "hostname": socket.gethostname(),
        "time": datetime.utcnow().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/api/info")
def info():
    return jsonify({
        "app": "devops-platform",
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
