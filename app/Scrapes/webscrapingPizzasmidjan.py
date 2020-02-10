import requests
from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager
import re

URL = 'https://www.pizzasmidjan.is/is/matsedlar/matsedill'


# TODO: error handling
def scrape_pizzamidjan():
    try:
        page = requests.get(URL)
    except requests.Timeout:
        # TODO: notify of this error
        return
    soup = BeautifulSoup(page.content, "html.parser")
    pizza_elms = soup.findAll("div", {"class": "item"})
    company_id = ScrapeManager.insert_or_get_company(name='Pizza Smiðjan', region='norðurland', delivers=False).id

    for pizza in pizza_elms:
        pizza_name = pizza.find("div", {"class", "item_title"}).text.strip()
        pizza_topping_Text = pizza.find("div", {"class", "item_desc"}).text.strip().lower()
        if pizza_topping_Text[-1:] == ',':
            pizza_topping_Text = pizza_topping_Text[:-1]
        pizza_topping_list = pizza_topping_Text.split(", ")
        pizza_mid_price = re.sub(r"\D", "", pizza.find("div", {"class", "item_price"}).text)

        ScrapeManager.add_scraped_pizza(pizza_name, pizza_topping_list, company_id, m_price=pizza_mid_price)

