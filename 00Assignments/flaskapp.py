from flask import Flask
from flask import request

app = Flask(__name__)
@app.route("/")
def test ():
    return "<h1>hello World!</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")