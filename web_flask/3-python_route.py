#!/usr/bin/python3
"""this module display a various thing"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """hello method"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """method hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    """text method"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"


@app.route("/python/<text>")
def python(text="is cool"):
    """the python method"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
