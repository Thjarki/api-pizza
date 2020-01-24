import requests
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeManager

URL = 'http://wilsons.is/MenuSite.aspx?g=1200'


# TODO: Test
def scrape_wilsons():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    pizza_elms = soup.findAll("div", {"class": "bgWhite"})[1:]
    company_id = ScrapeManager.insert_or_get_company(name='Wilsons', region='höfuðborgarsvæðið', delivers=True).id

    for pizza in pizza_elms:
        pizzaName = pizza.span.text.replace(" m/20% afslætti", "").replace("Stór ", "").replace(" m/25% afslætti", "")
        # edge case of offer in menu
        if 'm/3' in pizzaName:
            continue

        pizzaTopping = pizza.find("span", {"class": "aleggslysingText"}).text.lower()
        listPizzaTopping = pizzaTopping.split(", ")
        try:
            temp = pizza.findAll("option")[0].text[2:].replace("m/3", "").replace("Rocky 2", "")
            pizzaBigPrice = ''.join(i for i in temp if i.isdigit())
        except:
            pizzaBigPrice = None
        try:
            temp = pizza.findAll("option")[1].text[2:].replace("Rocky 2", "")
            pizzaMidPrice = ''.join(i for i in temp if i.isdigit())
        except:
            pizzaMidPrice = None
        try:
            temp = pizza.findAll("option")[2].text[2:].replace("Rocky 2", "")
            pizzaSmallPrice = ''.join(i for i in temp if i.isdigit())
        except:
            pizzaSmallPrice = None

        if ScrapeManager.pizza_exists(pizzaName, company_id):
            continue
        ScrapeManager.add_scraped_pizza(pizzaName, listPizzaTopping, company_id, s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice, l_price=pizzaBigPrice)
