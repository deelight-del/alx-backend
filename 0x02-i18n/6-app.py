#!/usr/bin/env python3
"""This module implements a flask application"""


from flask import Flask, render_template, request
from flask_babel import Babel, _
import flask


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Function that will get a user in a given
    request session"""
    user_id = request.args.get('login_as')
    if user_id is not None and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """Function to run before every request"""
    if get_user():
        flask.g.user = get_user()


@app.route("/", strict_slashes=False)
def hello_world():
    """Renders html template from the 4th index
    html page in the templates folder"""
    return render_template('5-index.html', user=flask.g.user)


if __name__ == "__main__":
    app.run()
