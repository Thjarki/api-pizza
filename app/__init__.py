from flask import Flask

# FIXME: config_object parameter does not work for some reason.
# Parameter for some reason is not a string, Turns into an object
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from app.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    # Fixme remove after test
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    # app.config['TESTING'] = True
    # app.config['WTF_CSRF_ENABLED'] = False

    from app.Model import db
    db.init_app(app)

    return app
