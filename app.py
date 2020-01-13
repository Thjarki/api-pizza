from flask import Blueprint
from flask_restful import Api
from resources.Pizza import PizzaResource
from resources.Ping import Ping
from resources.Scrape import Scrape
from resources.Topping import ToppingListResource, ToppingIDResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(PizzaResource, '/Pizza')

api.add_resource(ToppingListResource, '/Toppings')
api.add_resource(ToppingIDResource, '/Toppings/<int:id>', endpoint='task')
# TODO: /company, company/id/, /Pizza/id,/

api.add_resource(Ping, '/')

api.add_resource(Scrape, '/Admin/Scrape')