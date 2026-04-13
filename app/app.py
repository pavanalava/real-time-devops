from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Industrial Monitoring App Running<br>CI/CD Practice Round 2"

@app.route("/data")
def data():
    return {
        "status": "OK",
        "system": "running"
    }

@app.route("/data/<devops>")
def data_name(devops):
    return {
        "message": f"Hello {devops}",
        "status": "running"
    }

from datetime import datetime

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)