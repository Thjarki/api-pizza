import requests
from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager
import re

URL = 'http://www.spretturinn.is/is/pizzulisti'


def scrape_spretturinn():
    try:
        page = requests.get(URL)
    except requests.Timeout:
        # TODO: notify of this error
        return
    page_soup = BeautifulSoup(page.content, "html.parser")

    pizzas = page_soup.findAll("div", {"class": "tile product image"})
    company_id = ScrapeManager.insert_or_get_company(name='Spretturinn', region='norðurland', delivers=True).id

    for pizza in pizzas:
        pizzaName = pizza.h2.text
        pizzaTopping = pizza.findAll("div", {"class": "description"})[0].text.lower().\
            replace('.', '').replace(' og ', ', ')
        listPizzaTopping = pizzaTopping.split(", ")
        pizzaSmallPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[0].text)
        pizzaMidPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[1].text)
        pizzaBigPrice = re.sub(r"\D", "", pizza.findAll("span", {"class": "price"})[2].text)

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice,
                                        l_price=pizzaBigPrice)
