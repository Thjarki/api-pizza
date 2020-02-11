import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')


class Dev(Config):
    DEBUG = True


class Test(Config):
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


# TODO: set connection to online database
class Prod(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'


config = {
    'development': Dev,
    "dev": Dev,
    'testing': Test,
    'production': Prod,
    "prod": Prod,
    'config': Config,
    'default': Dev
}