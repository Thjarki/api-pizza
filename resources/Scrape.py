from flask import request
from flask_restful import Resource
from Model import db, Pizza, PizzaSchema
from marshmallow import ValidationError
from Scrapes.webscrapingPizzasmidjan import scrape_pizzamidjan
from Scrapes.webscrapingSpretturinn import scrape_spretturinn
from Scrapes.webscrapingGreifinn import scrape_greifinn

pizzas_schema = PizzaSchema(many=True)
pizza_schema = PizzaSchema()


class Scrape(Resource):
    def get(self):
        # TODO: return last scrape time
        return {"message": "Connected"}

    def put(self):
        scrape_pizzamidjan()
        scrape_spretturinn()
        scrape_greifinn()

        db.session.commit()

        return {"message": "successful scrape"}
