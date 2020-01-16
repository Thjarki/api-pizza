import requests
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeMananger

URL = 'https://www.pizzasmidjan.is/is/matsedlar/matsedill'


def scrape_pizzamidjan():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    pizza_elms = soup.findAll("div", {"class": "item"})
    company_id = ScrapeMananger.insert_or_get_company(name='Pizza Smiðjan', region='norðuland').id

    for pizza in pizza_elms:
        pizza_name = pizza.find("div", {"class", "item_title"}).text.strip()
        pizza_topping_Text = pizza.find("div", {"class", "item_desc"}).text.strip()
        pizza_topping_list = pizza_topping_Text.split(", ")
        pizza_mid_price = pizza.find("div", {"class", "item_price"}).text.strip()[5:10]


        # Don't add when pizza exists, TODO: Update pizza
        if ScrapeMananger.pizza_exists(pizza_name, company_id):
            continue
        ScrapeMananger.add_scraped_pizza(pizza_name, pizza_topping_list, company_id, m_price=pizza_mid_price)
    return
