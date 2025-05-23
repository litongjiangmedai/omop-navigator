
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/query", methods=["POST"])
def query():
    return jsonify({"error": "Simulated server error"}), 500

if __name__ == "__main__":
    app.run(port=5003)
