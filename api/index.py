from flask import Flask

from reactpy import component, html
from reactpy.backend.flask import configure


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = Flask(__name__)
configure(app, HelloWorld)

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'