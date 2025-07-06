from flask import Flask, render_template
import os  # ← 追加

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 🔽 ここが超重要！！
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Renderが自動で指定するポートを取得
    app.run(host='0.0.0.0', port=port)  # ここで公開サーバとして起動
