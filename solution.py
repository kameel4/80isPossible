from flask import *

app = Flask(__name__)


@app.route("/")
def views():
    return open("static/index.html", "r", encoding="UTF-8").read()


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
