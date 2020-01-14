import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class Dev(Config):
    DEBUG = True


class Test(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# TODO: set connection to online database
class Prod(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'