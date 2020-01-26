from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import app.Scrapes.scrapeMananger as ScrapeManager
# noinspection PyUnresolvedReferences
import chromedriver_binary
import time


def get_html():
    # this is slow, need to research faster methods, takes about 9 secondsprint('somthing')
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
    driver.implicitly_wait(20)
    driver.get('https://devitos.is/menu/')
    time.sleep(1)
    page = driver.page_source
    print('quit')
    driver.quit()
    return page


def scrape_devitos():
    soup = BeautifulSoup(get_html(), "html.parser")

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
            # pizzatoppingsList = [topping for topping in pizzatoppingsList if topping != 'ostur' and topping != 'devitos sósa']

            pizzaSmallPrice = len(pizzatoppingsList) * smallToppingBasePrice + smallBasePrice
            pizzaMidPrice = len(pizzatoppingsList) * medToppingBasePrice + medBasePrice
            pizzaBigPrice = len(pizzatoppingsList) * bigToppingBasePrice + bigBasePrice
            pizzaXLPrice = len(pizzatoppingsList) * XLToppingBasePrice + XLBasePrice

            if ScrapeManager.pizza_exists(pizzaName, company_id):
                continue
            ScrapeManager.add_scraped_pizza(name=pizzaName,
                                            scraped_toppings=pizzatoppingsList,
                                            company_id=company_id,
                                            s_price=pizzaSmallPrice,
                                            m_price=pizzaMidPrice,
                                            l_price=pizzaBigPrice,
                                            xl_price=pizzaXLPrice)
            # print(pizzaName)
            # print(pizzatoppingsList)
            # print(pizzaSmallPrice)
            # print(pizzaMidPrice)
            # print(pizzaBigPrice)
            # print(pizzaXLPrice)
