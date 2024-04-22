#!/usr/bin/python3
"""this module display multiple pages"""

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
@app.route("/python")
def python(text="is cool"):
    """the python method"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.route("/number/<int:n>")
def number(n):
    """method to print number"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
