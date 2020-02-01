import requests
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'https://api.pizzan.is/api/v1/pizzas/menu/'


def scrape_pizzan():
    response = requests.get(URL)

    pizzas = response.json()

    company_id = ScrapeManager.insert_or_get_company(name='Pizzan', region='höfuðborgarsvæðið', delivers=True).id

    for pizza in pizzas:

        pizzaName = pizza['name']
        pizzaTopping = pizza['toppingsSummary'].lower()
        listPizzaTopping = pizzaTopping.split(", ")
        pizzaSmallPrice = pizza['minimumAmountSmall']
        pizzaMidPrice = pizza['minimumAmountMedium']
        pizzaBigPrice = pizza['minimumAmountLarge']

        ScrapeManager.add_scraped_pizza(name=pizzaName,
                                        scraped_toppings=listPizzaTopping,
                                        company_id=company_id,
                                        s_price=pizzaSmallPrice,
                                        m_price=pizzaMidPrice,
                                        l_price=pizzaBigPrice)

        # print("Nafn : " + pizzaName)
        # print("alegg : " + pizzaTopping)
        # print(listPizzaTopping)
        # print(pizzaSmallPrice)
        # print(pizzaMidPrice)
        # print(pizzaBigPrice)
