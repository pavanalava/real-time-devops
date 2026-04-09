from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Industrial Monitoring App Running"

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

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)