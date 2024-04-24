#!/usr/bin/python3
"""this module uses the html body"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """hello method"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """hbnb method"""
    return "HBNB"


@app.route("/c/<text>")
def text(text):
    """text method"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/(<text>)")
@app.route("/python")
def python(text="is cool"):
    """pythjon methood"""
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def number(n):
    """number method"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def template(n):
    """template method"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_number(n):
    """the odd even method"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", num=n, type='even')
    else:
        return render_template("6-number_odd_or_even.html", num=n, type='odd')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
