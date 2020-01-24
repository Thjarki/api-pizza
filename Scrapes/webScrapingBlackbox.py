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
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-proxy-server')
    chrome_options.add_argument("--proxy-server='direct://'");
    chrome_options.add_argument("--proxy-bypass-list=*");
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.blackboxpizza.is/#Menu')
    page = driver.page_source
    driver.quit()
    return page


def scrape_blackbox():
    soup = BeautifulSoup(get_html(), "html.parser")
    company_id = ScrapeManager.insert_or_get_company(name='Blackbox', region='höfuðborgarsvæðið', delivers=False).id

    menu = soup.find('div', {'id': 'Menu'})
    pizza_elm = menu.find_all('div', {'class': 'salescloud-product'})

    for pizza in pizza_elm:
        pizzaName = pizza.find('h2', {'class': 'salescloud-menu-title'}).text
        if '60.' in pizzaName: # skiping 'velja sjálfur
            continue
        pizzaName = pizzaName[pizzaName.find(' '):].strip()  # removing numbers in front of name
        pizzaToppings = pizza.find('div',{'class': 'salescloud-default-variations-description'}).text.replace('Súrdeigsbotn, ', '').lower()  # maybe remove 'pizzasósa also
        listPizzaTopping = pizzaToppings.split(', ')
        pizzaMidPrice = re.sub(r"\D", "", pizza.p.text)

        if ScrapeManager.pizza_exists(pizzaName, company_id):
            continue
        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        m_price=pizzaMidPrice)
        # print(pizzaName)
        # print(pizzaToppings)
        # print(listPizzaTopping)
        # print(pizzaMidPrice)
