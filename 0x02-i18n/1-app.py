#!/usr/bin/env python3
"""A Basic Flask app.
"""

from flask_babel import Babel
from flask import Flask, render_template

class Config:
    """Represent the flask babel config.
    """
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index():
    """The home/index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
