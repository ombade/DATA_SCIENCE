from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def test():
    return "<h1> WELLCOME TO ABC CORPORATION</h1>"


@app.route("/welcome")
def welcome(): return """<p>  Company Name: ABC Corporation
                Location: India
                 Contact Detail: 999-999-9999 </p>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0")
