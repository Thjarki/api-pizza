from flask import request
from flask_restful import Resource
from Model import db, Pizza, PizzaSchema
from marshmallow import ValidationError
from Scrapes.webscrapingPizzasmidjan import scrape_pizzamidjan
from Scrapes.webscrapingSpretturinn import scrape_spretturinn
from Scrapes.webscrapingGreifinn import scrape_greifinn
from Scrapes.webscrapingEldsmidjan import scrape_eldsmidjan
from Scrapes.webscrapingCastello import scrape_castello
from Scrapes.webscrapingWilson import scrape_wilsons
from Scrapes.apiDominos import scrape_dominos
from Scrapes.apiPizzan import scrape_pizzan


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

        scrape_eldsmidjan()
        scrape_castello()
        scrape_wilsons()
        scrape_dominos()
        scrape_pizzan()

        db.session.commit()

        return {"message": "successful scrape"}
