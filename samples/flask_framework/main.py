from flask import Flask
from config import START_PORT

app = Flask(__name__)


@app.route("/")
def hello():
    return "This is a Flask application!"


if __name__ == '__main__':
    app.run(port=START_PORT)
