from flask import Flask

# FIXME: config_object parameter does not work for some reason.
# Parameter for some reason is not a string, Turns into an object
from config import Config


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    # Fixme remove after test
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    # app.config['TESTING'] = True
    # app.config['WTF_CSRF_ENABLED'] = False

    from app.Model import db
    db.init_app(app)

    return app