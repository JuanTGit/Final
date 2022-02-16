from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My Secret Key123'

from . import routes

