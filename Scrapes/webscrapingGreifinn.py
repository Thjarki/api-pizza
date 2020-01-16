import requests
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeMananger
import re

URL = 'https://www.greifinn.is/pizza/index/pizza#center'


def scrape_greifinn():
    page = requests.get(URL)
    page_soup = BeautifulSoup(page.content, "html.parser")

    pizzas = page_soup.find(id="pizzaMenu").findAll("li")
    company_id = ScrapeMananger.insert_or_get_company(name='greifinn', region='norðuland').id

    iterPizzas = iter(pizzas)
    next(iterPizzas)

    for pizza in iterPizzas:
        pizzaName = pizza.h4.text.lower()
        pizzaTopping = pizza.div.text
        listPizzaTopping = pizzaTopping.split(", ")
        temp = pizza.find("div", {"class": "price"}).findAll("div")[0].text
        pizzaSmallPrice = re.sub(r"\D", "", temp)
        temp = pizza.find("div", {"class": "price"}).findAll("div")[1].text
        pizzaMidPrice = re.sub(r"\D", "", temp)
        temp = pizza.find("div", {"class": "price"}).findAll("div")[2].text
        pizzaBigPrice = re.sub(r"\D", "", temp)

        # Don't add when pizza exists, TODO: Update pizza
        if ScrapeMananger.pizza_exists(pizzaName, company_id):
            continue

        ScrapeMananger.add_scraped_pizza(name=pizzaName,
                                         scraped_toppings=listPizzaTopping,
                                         company_id=company_id,
                                         s_price=pizzaSmallPrice,
                                         m_price=pizzaMidPrice,
                                         l_price=pizzaBigPrice)
