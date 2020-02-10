import requests
from bs4 import BeautifulSoup
import re
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'https://www.greifinn.is/pizza/index/pizza#center'


# TODO: Create test and error handling
def scrape_greifinn():
    try:
        page = requests.get(URL)
    except requests.Timeout:
        # TODO: notify of this error
        return
    page_soup = BeautifulSoup(page.content, "html.parser")

    menu = page_soup.find('div', id="pizzaMenu")

    if menu is None:  # Site is close, TODO: add more reliable check
        return

    pizza_elms = menu.find_all("li")[1:]
    company_id = ScrapeManager.insert_or_get_company(name='Greifinn', region='norðurland', delivers=True).id

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

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice,
                                        l_price=pizzaBigPrice)
