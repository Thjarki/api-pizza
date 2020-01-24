from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import Scrapes.scrapeMananger as ScrapeManager
import re
# noinspection PyUnresolvedReferences
import chromedriver_binary


def get_html():
    # this is slow, need to research faster methods, takes about 9 seconds
    chrome_options = Options()
    print('start')
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
    print('get')
    driver.get('https://www.flatbakan.is/baejarlind')
    page = driver.page_source
    print('quit')
    driver.quit()
    return page


def scrape_flatbakan():
    soup = BeautifulSoup(get_html(), "html.parser")
    company_id = ScrapeManager.insert_or_get_company(name='Flatbakan', region='höfuðborgarsvæðið', delivers=True).id
    menu_elm = soup.find('div', {'id': '1049564149'})
    print(soup.original_encoding)
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

        if ScrapeManager.pizza_exists(pizzaName, company_id):
           continue
        ScrapeManager.add_scraped_pizza(pizzaName, listPizzaTopping, company_id, m_price=pizzaMidPrice)