from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager
import re

URL = 'https://www.blackboxpizza.is/#Menu'


def scrape_blackbox():
    page = ScrapeManager.get_page_selenium(URL)
    soup = BeautifulSoup(page, "html.parser")
    company_id = ScrapeManager.insert_or_get_company(name='Blackbox', region='höfuðborgarsvæðið', delivers=False).id

    menu = soup.find('div', {'id': 'Menu'})
    pizza_elm = menu.find_all('div', {'class': 'salescloud-product'})

    for pizza in pizza_elm:
        pizzaName = pizza.find('h2', {'class': 'salescloud-menu-title'}).text
        if '60.' in pizzaName:  # skipping 'velja sjálfur'
            continue
        pizzaName = pizzaName[pizzaName.find(' '):].strip()  # removing numbers in front of name
        pizzaToppings = pizza.find('div',{'class': 'salescloud-default-variations-description'}).text.replace('Súrdeigsbotn, ', '').lower()  # maybe remove 'pizzasósa also
        listPizzaTopping = pizzaToppings.split(', ')
        pizzaMidPrice = re.sub(r"\D", "", pizza.p.text)

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        m_price=pizzaMidPrice)
        # print(pizzaName)
        # print(pizzaToppings)
        # print(listPizzaTopping)
        # print(pizzaMidPrice)
