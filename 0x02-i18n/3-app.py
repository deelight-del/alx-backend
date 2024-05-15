#!/usr/bin/env python3
"""In This module we
implements a flask application for different
internationalization and localization behaviour"""


from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """The configuration class for our application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Function to get the best matched
    locale depending on our LANGUAGES"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """Renders html template from the
    3-html file in the templates"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
