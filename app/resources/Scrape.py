from flask_restful import Resource
from app.Model import db, PizzaSchema
from app.Scrapes.webscrapingPizzasmidjan import scrape_pizzamidjan
from app.Scrapes.webscrapingSpretturinn import scrape_spretturinn
from app.Scrapes.webscrapingGreifinn import scrape_greifinn
from app.Scrapes.webscrapingEldsmidjan import scrape_eldsmidjan
from app.Scrapes.webscrapingCastello import scrape_castello
from app.Scrapes.webscrapingWilson import scrape_wilsons
from app.Scrapes.apiDominos import scrape_dominos
from app.Scrapes.apiPizzan import scrape_pizzan
from app.Scrapes.webScrapeDevitos import scrape_devitos
from app.Scrapes.webScrapeFlatbakan import scrape_flatbakan
from app.Scrapes.webScrapingBlackbox import scrape_blackbox
from app.Scrapes.pdfScrapeBryggjan import scrape_bryggjan

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
        scrape_devitos()
        scrape_flatbakan()
        scrape_blackbox()
        scrape_bryggjan()
        db.session.commit()

        return {"message": "successful scrape"}
