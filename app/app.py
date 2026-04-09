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

if __name__ == "__main__":
    app.run(debug=True)