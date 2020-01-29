from flask import abort
from flask_restful import Resource, reqparse
from app.Model import db, ToppingSchema, Topping

toppings_schema = ToppingSchema(many=True)
topping_schema = ToppingSchema()


class ToppingListResource(Resource):
    def get(self):
        toppings = Topping.query.all()
        toppings = toppings_schema.dump(toppings)
        return {'status': 'success', 'data': toppings}, 200


class ToppingIDResource(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('type', choices=('ostur', 'kjöt', 'grænt', 'sósur og krydd', 'ýmislegt'), type=str, help='Bad choice: ostur, kjöt, grænt, sósur og krydd, ýmislegt')
        super(ToppingIDResource, self).__init__()

    def get(self, id):
        topping = Topping.query.filter(Topping.id == id).first()
        if topping is None:
            abort(404)
        else:
            return {'message': 'success', 'data': topping_schema.dump(topping)}, 200

    def put(self, id):
        args = self.reqparse.parse_args()
        topping = Topping.query.filter(Topping.id == id).first()
        if topping is None:
            abort(404)
        else:
            if args['type'] is not None:
                topping.type = args['type']
                db.session.commit()
                return {'message': 'success', 'data': topping_schema.dump(topping)}, 200
            else:
                abort(400)
            pass

    def delete(self, id):
        topping = Topping.query.filter(Topping.id == id).first()
        if topping is None:
            abort(404)
        else:
            abort(501)
