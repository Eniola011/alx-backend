#!/usr/bin/python3
"""

Basic Flask_Babel App

"""


from flask import Flask, render_template, request
from flask_babel import Babel
from os import getenv


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Configuring Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages. """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """ index page """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
