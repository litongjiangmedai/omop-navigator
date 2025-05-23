
from flask import Flask, request, jsonify
import sqlite3
import traceback

app = Flask(__name__)

@app.route("/api/query", methods=["POST"])
def query():
    sql = request.json.get("sql")
    conn = sqlite3.connect("data/node1.sqlite")
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
        return jsonify({"result": rows})
    except Exception as e:
        traceback.print_exc()  # ✅ 打印完整错误栈
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(port=5001)
