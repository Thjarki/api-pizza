from flask import request
from flask_restful import Resource
from Model import db, ToppingSchema, Topping
from marshmallow import ValidationError

toppings_schema = ToppingSchema(many=True)
topping_schema = ToppingSchema()


class ToppingListResource(Resource):
    def get(self):
        toppings = Topping.query.all()
        toppings = toppings_schema.dump(toppings)
        return {'status': 'success', 'data': toppings}, 200

class ToppingIDResource(Resource):
    def get(self, id):
        topping = Topping.query