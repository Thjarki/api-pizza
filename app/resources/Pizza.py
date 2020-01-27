from flask import request
from flask_restful import Resource, reqparse
from app.Model import db, Pizza, PizzaSchema, Topping
from marshmallow import ValidationError

pizzas_schema = PizzaSchema(many=True)
pizza_schema = PizzaSchema()

parser = reqparse.RequestParser()
parser.add_argument('filter-topping', action='append')

class PizzaResource(Resource):
    def get(self):
        args = parser.parse_args()

        if args['filter-topping'] is not None:
            conditions = []
            for item in args['filter-topping']:
                topping = Topping.query.filter_by(name=item).first()
                conditions.append(Pizza.toppings.contains(topping))

            pizzas = Pizza.query.filter(*conditions)
        else:
            pizzas = Pizza.query.all()

        pizzas = pizzas_schema.dump(pizzas)
        return {'status': 'success', 'data': pizzas}, 200

    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        try:
            data = pizza_schema.load(json_data)
        except ValidationError as err:
            return err.messages, 422
        pizza = Pizza.query.filter_by(name=data['name']).first()
        if pizza:
            return {'message': 'pizza already exists'}, 400
        pizza = Pizza(
            name=json_data['name']
        )

        db.session.add(pizza)
        db.session.commit()

        result = pizza_schema.dump(pizza)

        return {"status": 'success', 'data': result}, 201
