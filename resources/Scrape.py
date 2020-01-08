from flask import request
from flask_restful import Resource
from Model import db, Pizza, PizzaSchema
from marshmallow import ValidationError
from ScrapingScripts.webscrapingPizzasmidjan import scrapePizzamiðjan

pizzas_schema = PizzaSchema(many=True)
pizza_schema = PizzaSchema()


class Scrape(Resource):
    def get(self):
        # TODO: return last scrape time
        return {"message": "Connected"}

    def put(self):
        scrapePizzamiðjan()

        db.session.commit()

        return {"message": "successful scrape"}
