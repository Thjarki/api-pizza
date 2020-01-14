import os

basedir = os.path.abspath(os.path.dirname(__file__))
# Database
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
JSON_AS_ASCII = False