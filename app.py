from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 🔽 ここが重要
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Renderが使うPORTを自動取得
    app.run(host='0.0.0.0', port=port)
