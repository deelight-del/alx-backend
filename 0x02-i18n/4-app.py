#!/usr/bin/env python3
"""This module implements a flask application"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


app = Flask(__name__)
babel = Babel(app)


class Config:
    """The configuration class for our application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Function to get the best matched
    locale depending on our LANGUAGES"""
    if (
        request.args.get('locale') is not None
        and request.args.get('locale') in
        app.config["LANGUAGES"]
            ):

        return request.args.get('locale')
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def hello_world():
    """Renders html template"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
