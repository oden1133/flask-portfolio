from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>はじめてのポートフォリオ</h1>
    <p>こんにちは！農学部で統計を学んでいる大学生です。</p>
    <p>PythonとFlaskを使って、自分の紹介ページを作っています！</p>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
