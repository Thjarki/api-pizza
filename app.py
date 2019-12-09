from flask import Blueprint
from flask_restful import Api
from resources.Pizza import PizzaResource
from resources.Ping import Ping

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(PizzaResource, '/Pizza')

api.add_resource(Ping, '/')
