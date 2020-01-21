import requests
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeManager
import re

URL = 'https://castello.is/matsedill/#pizza'


# TODO: Test and error handle
def scrape_castello():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    pizza_elms = soup.findAll("article", {"class": "wppizza_menu-pizza"})
    company_id = ScrapeManager.insert_or_get_company(name='Castello', region='höfuðborgarsvæðið').id

    for pizza in pizza_elms:
        pizzaName = pizza.h2.text.strip()

        if pizza.p.em is not None:
            pizza.p.em.replace_with('')
            pizzaTopping = pizza.p.text.strip().lower()
        else:  # edge cases of no english toppings.
            pizzaTopping = pizza.p.text.replace('\n', ' ').lower()
        # edge case of toppings string ending with a dot.
        if pizzaTopping[-1:] == '.':
            pizzaTopping = pizzaTopping[:-1]

        # edge case of 'og'
        pizzaTopping = pizzaTopping.replace(' og ', ', ')

        listPizzaTopping = pizzaTopping.split(", ")

        # loop needed since not all pizzas have 3 sizes
        pizzaSmallPrice = None
        pizzaMidPrice = None
        pizzaBigPrice = None
        prices = pizza.find_all("span", {"class": "wppizza-article-price"})

        for item in prices:
            size = item.div.text
            price = re.sub(r"\D", "", item.span.text)
            if size == '9"':
                pizzaSmallPrice = price
            elif size == '12"':
                pizzaMidPrice = price
            elif size == '15"':
                pizzaBigPrice = price

        # edge case of pizza with no price
        if pizzaSmallPrice == '0' and pizzaMidPrice == '0' and pizzaBigPrice == '0':
            continue

        # print("Nafn: {}".format(pizzaName))
        # print("alegg: {}".format(pizzaTopping))
        # print(listPizzaTopping)
        # print("litil verd: {}".format(pizzaSmallPrice))
        # print("midstared: {}".format(pizzaMidPrice))
        # print("stor verd: {}".format(pizzaBigPrice))

        # Don't add when pizza exists, TODO: Update pizza
        if ScrapeManager.pizza_exists(pizzaName, company_id):
            continue
        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice,
                                        l_price=pizzaBigPrice)

