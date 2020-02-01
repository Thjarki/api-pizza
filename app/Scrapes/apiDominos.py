import requests
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'https://api.dominos.is/api/menu'


# create Test
def scrape_dominos():
    response = requests.get("https://api.dominos.is/api/menu")
    company_id = ScrapeManager.insert_or_get_company(name='Dominos', region='höfuðborgarsvæðið', delivers=True).id
    pizzas = response.json()
    topping = ""
    for pizza in pizzas['menu']['menuPizzas']:
        pizzaName = pizza['name']

        for i, top in enumerate(pizza['toppings']):
            if i == 0:
                topping += top['name']
            else:
                topping += ", " + top['name']
        pizzaTopping = topping.lower()
        listPizzaTopping = pizzaTopping.split(", ")
        pizzaSmallPrice = pizza['sizes'][0]['pickupPrice']
        pizzaMidPrice = pizza['sizes'][1]['pickupPrice']
        pizzaBigPrice = pizza['sizes'][2]['pickupPrice']

        topping = ""

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice,
                                        l_price=pizzaBigPrice)
    # print("Nafn : " + pizzaName )
    # print("alegg : " + pizzaTopping)
    # print(listPizzaTopping)
    # print(pizzaSmallPrice)
    # print(pizzaMidPrice)
    # print(pizzaBigPrice)
