from flask import Flask, Response, send_from_directory
app = Flask(__name__)

@app.route("/<path:path>")
def hello(path):
    if path is None or len(path) is 0:
        path = "index.html"
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
