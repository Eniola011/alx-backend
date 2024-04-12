#!/usr/bin/python3
"""

Basic Flask_Babel App

"""


from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import gettext as _


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ Configuring Babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ index page """
    return render_template("5-index.html")

def get_locale():
    """
       >> Determine the best match with our supported languages.
       >> Does incoming request contains locale argument?
    """
    if request.args.get('locale'):
        usr_locale = request.args.get('locale')
        if usr_locale in app.config['LANGUAGES']:
            return usr_locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

# Initialize Flask-Babel with the application and the locale selector
babel.init_app(app, locale_selector=get_locale)

def get_user():
    """
        >> Function returns a user dictionary or None.
        >> if the ID cannot be found or if login_as was not passed.
    """
    try:
        usr_id = request.args.get('login_as')
        return users[int(usr_id)]
    except Exception:
        return None

@app.before_request
def before_request():
    """
        >> Decorator to make it be executed before all other functions.
    """
    get_usr = get_user()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
