#!/usr/bin/python3
"""build a web application on flask"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """the method that display on host"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """method that display hbnb on host"""
    return "HBNB"


if __name__ == "__main__":
    app.run('0.0.0.0')
