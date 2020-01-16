import requests
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeMananger
import re


URL = 'http://www.spretturinn.is/is/pizzulisti'


def scrape_spretturinn():
    page = requests.get(URL)
    page_soup = BeautifulSoup(page.content, "html.parser")

    pizzas = page_soup.findAll("div", {"class": "tile product image"})
    company_id = ScrapeMananger.insert_or_get_company(name='spretturinn', region='norðuland').id

    for pizza in pizzas:
        pizzaName = pizza.h2.text
        pizzaTopping = pizza.findAll("div", {"class": "description"})[0].text.lower().replace('.', '')
        listPizzaTopping = pizzaTopping.split(", ")
        pizzaSmallPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[0].text)
        pizzaMidPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[1].text)
        pizzaBigPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[2].text)

        # Don't add when pizza exists, TODO: Update pizza
        if ScrapeMananger.pizza_exists(pizzaName, company_id):
            continue
        print(pizzaName, listPizzaTopping, company_id, pizzaSmallPrice, pizzaMidPrice, pizzaBigPrice)
        ScrapeMananger.add_scraped_pizza(name=pizzaName,
                                         scraped_toppings=listPizzaTopping,
                                         company_id=company_id,
                                         s_price=pizzaSmallPrice,
                                         m_price=pizzaMidPrice,
                                         l_price=pizzaBigPrice)
