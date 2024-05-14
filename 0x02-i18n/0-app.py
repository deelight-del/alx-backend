#!/usr/bin/env python3
"""This module implements a flask application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    """Renders html template"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
