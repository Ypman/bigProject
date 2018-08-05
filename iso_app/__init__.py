# __init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utils/sqlalchemy_test.db'
db = SQLAlchemy(app)
db.session

from iso_app.utils import routes
