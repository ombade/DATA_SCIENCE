from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def test():
    return "ombade"


@app.route("/login")
def login():
    return("lohi")


@app.route("/test1")
def test1():
    data = request.args.get('x')
    return "hello{}".format(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
