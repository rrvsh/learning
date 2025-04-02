from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.get("/")
def home():
    return "home"


@app.route("/<username>")
def hello(username):
    # Use escape for user input to protect against injection attacks
    return f"hello, {escape(username)}"
