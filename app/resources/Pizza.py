from flask import request
from flask_restful import Resource, reqparse
from app.Model import db, Pizza, PizzaSchema, Topping, Company
from sqlalchemy import or_
from marshmallow import ValidationError

pizzas_schema = PizzaSchema(many=True)
pizza_schema = PizzaSchema()


class PizzaResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('filter-topping', type=str, action='append')
        self.reqparse.add_argument('filter-company', type=str, action='append')
        self.reqparse.add_argument('filter-delivers', type=bool)
        super(PizzaResource, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()

        conditions = []

        if args['filter-delivers'] is not None:
            conditions.append(Pizza.company.has(Company.delivers == args['filter-delivers']))

        if args['filter-company'] is not None:
            con = []
            for item in args['filter-company']:
                company = Company.query.filter_by(name=item).first()
                if company is None:
                    return {'status': 'error', 'message': 'Company: "{}" does not exist'.format(item)}, 400
                con.append(Pizza.company_id == company.id)
            conditions.append(or_(*con))

        if args['filter-topping'] is not None:
            for item in args['filter-topping']:
                topping = Topping.query.filter_by(name=item).first()
                if topping is None:
                    return {'status': 'error', 'message': 'Topping: "{}" does not exist'.format(item)}, 400
                conditions.append(Pizza.toppings.contains(topping))

        if len(conditions) == 0:
            pizzas = Pizza.query.all()
        else:
            pizzas = Pizza.query.filter(*conditions)

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
