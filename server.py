import os
import subprocess
import sys

from flask import Flask, Response, send_from_directory

app = Flask(__name__)


# 경로 설정: index.html을 루트에서 서빙
@app.route("/")
def index():
    return send_from_directory(".", "index.html")


# /run 경로: main.py 실행
@app.route("/run")
def run_script():
    try:
        # 현재 실행 중인 Python 인터프리터를 사용하여 실행
        result = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        output = result.stdout + "\n" + result.stderr
        return Response(output, mimetype="text/plain")
    except Exception as e:
        return Response(f"Exception occurred:\n{str(e)}", mimetype="text/plain")


# 서버 실행
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
