from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager
import re

URL = 'https://www.flatbakan.is/baejarlind'


def scrape_flatbakan():
    page = ScrapeManager.get_page_selenium(URL)
    soup = BeautifulSoup(page, "html.parser")
    company_id = ScrapeManager.insert_or_get_company(name='Flatbakan', region='höfuðborgarsvæðið', delivers=True).id
    menu_elm = soup.find('div', {'id': '1049564149'})
    pizzas_elm = menu_elm.find_all('div', {'class': 'salescloud-product-inner'})

    for pizza in pizzas_elm:
        pizzaName = pizza.find('h2', {'class': 'salescloud-menu-title'}).text
        pizzaToppings = pizza.find('div', {'class': 'salescloud-menu-description'}).find('p').text.replace('.', '').replace(' og ', ', ').lower().strip()

        if 'hálfmáni' in pizzaToppings: # edge case: '(hálfmáni, ekki hægt að opna)'
            pizzaName += ' (hálfmáni)'
            pizzaToppings = pizzaToppings[:pizzaToppings.find('(')-1]
        if 'mozzarella' in pizzaToppings:  # edge case: 'mozzarella í stað pizzaost'
            pizzaToppings = pizzaToppings.replace(' í stað pizzaost', '')

        listPizzaTopping = [x.strip() for x in pizzaToppings.split(',')] # Edge case of some unicode messing up regular split
        if len(listPizzaTopping) <= 1: # edge case: non topping pizza
            continue
        pizzaMidPrice = re.sub(r"\D", "", pizza.find('p', {'class': 'salescloud-menu-price'}).text)

        # print(pizzaName)
        # print(pizzaToppings)
        # print(listPizzaTopping)
        # print(pizzaMidPrice)

        ScrapeManager.add_scraped_pizza(pizzaName, listPizzaTopping, company_id, m_price=pizzaMidPrice)