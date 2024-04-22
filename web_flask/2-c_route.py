#!/usr/bin/python3
"""this module define three routes on flask web app"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """this methods return route /"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """this method return hbnb"""
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    """this method use a variable"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"
