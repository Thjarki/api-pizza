
from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager


URL = 'https://devitos.is/menu/';


def scrape_devitos():
    page = ScrapeManager.get_page_selenium(URL, 1)
    soup = BeautifulSoup(page, "html.parser")

    company_id = ScrapeManager.insert_or_get_company(name='Devitos', region='höfuðborgarsvæðið', delivers=False).id

    price_container = soup.find('div', {'class': 'toppings-price-style'})
    menu_container = soup.find('div', {'id': 'main-menu'})

    smallBasePrice = int(price_container.find('div', {'id': 'basePrice10'}).text)
    medBasePrice = int(price_container.find('div', {'id': 'basePrice12'}).text)
    bigBasePrice = int(price_container.find('div', {'id': 'basePrice16'}).text)
    XLBasePrice = int(price_container.find('div', {'id': 'basePrice18'}).text)
    smallToppingBasePrice = int(price_container.find('div', {'id': 'price10'}).text)
    medToppingBasePrice = int(price_container.find('div', {'id': 'price12'}).text)
    bigToppingBasePrice = int(price_container.find('div', {'id': 'price16'}).text)
    XLToppingBasePrice = int(price_container.find('div', {'id': 'price18'}).text)

    pizza_elm = menu_container.find_all('div', {'class': 'menu-item'})

    for item in pizza_elm:
        pizzaName = item.find('p', {'class': 'menuItemName'}).text
        if 'tilboð' in pizzaName.lower():
            continue
        pizzatoppingsList = item.find('p', {'class': 'menuItemToppings'}).text.replace(" og ", ", ").lower().split(", ")
        if(len(pizzatoppingsList)) > 1:

            pizzaSmallPrice = len(pizzatoppingsList) * smallToppingBasePrice + smallBasePrice
            pizzaMidPrice = len(pizzatoppingsList) * medToppingBasePrice + medBasePrice
            pizzaBigPrice = len(pizzatoppingsList) * bigToppingBasePrice + bigBasePrice
            pizzaXLPrice = len(pizzatoppingsList) * XLToppingBasePrice + XLBasePrice

            # print(pizzaName)
            # print(pizzatoppingsList)
            # print(pizzaSmallPrice)
            # print(pizzaMidPrice)
            # print(pizzaBigPrice)
            # print(pizzaXLPrice)

            ScrapeManager.add_scraped_pizza(name=pizzaName,
                                            scraped_toppings=pizzatoppingsList,
                                            company_id=company_id,
                                            s_price=pizzaSmallPrice,
                                            m_price=pizzaMidPrice,
                                            l_price=pizzaBigPrice,
                                            xl_price=pizzaXLPrice)

