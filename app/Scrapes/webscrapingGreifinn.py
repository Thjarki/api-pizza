import requests
from bs4 import BeautifulSoup
import re
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'https://www.greifinn.is/pizza/index/pizza#center'


# TODO: Create test and error handling
def scrape_greifinn():
    page = requests.get(URL)
    page_soup = BeautifulSoup(page.content, "html.parser")

    company_id = ScrapeManager.insert_or_get_company(name='Greifinn', region='norðuland', delivers=True).id

    menu = page_soup.find(id="pizzaMenu")

    if menu is None:  # Site is close, TODO: add more reliable check
        return

    pizza_elms = menu.find_All("li")[1:]
    company_id = ScrapeManager.insert_or_get_company(name='Greifinn', region='norðuland', delivers=True).id

    for pizza in pizza_elms:
        pizzaName = pizza.h4.text
        pizzaTopping = pizza.div.text.lower()
        listPizzaTopping = pizzaTopping.split(", ")
        temp = pizza.find("div", {"class": "price"}).findAll("div")[0].text
        pizzaSmallPrice = re.sub(r"\D", "", temp)
        temp = pizza.find("div", {"class": "price"}).findAll("div")[1].text
        pizzaMidPrice = re.sub(r"\D", "", temp)
        temp = pizza.find("div", {"class": "price"}).findAll("div")[2].text
        pizzaBigPrice = re.sub(r"\D", "", temp)

        # Don't add when pizza exists, TODO: Update pizza
        if ScrapeManager.pizza_exists(pizzaName, company_id):
            continue

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                         scraped_toppings=listPizzaTopping,
                                         company_id=company_id,
                                         s_price=pizzaSmallPrice,
                                         m_price=pizzaMidPrice,
                                         l_price=pizzaBigPrice)
