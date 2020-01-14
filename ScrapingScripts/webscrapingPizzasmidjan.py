import requests
from bs4 import BeautifulSoup
from Model import Pizza, Price, Topping, db

URL = 'https://www.pizzasmidjan.is/is/matsedlar/matsedill'


def scrape_pizzamidjan():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    pizza_elms = soup.findAll("div", {"class": "item"})

    for pizza in pizza_elms:
        pizza_name = pizza.find("div", {"class", "item_title"}).text.strip()
        pizza_topping_Text = pizza.find("div", {"class", "item_desc"}).text.strip()
        pizza_topping_list = pizza_topping_Text.split(", ")
        pizza_mid_price = pizza.find("div", {"class", "item_price"}).text.strip()[5:10]

        add_scraped_pizza(pizza_name, pizza_topping_list, m_price=pizza_mid_price)
    return


# TODO: test, with mock_data and real_data
def add_scraped_pizza(name, scraped_toppings, s_price=None, m_price=None, l_price=None, xl_price=None):
    newToppings = []
    for item in scraped_toppings:  # Check if the topping exist,
        newTopping = db.session.query(Topping).filter_by(name=item).first()
        if newTopping is None:
            newTopping = Topping(name=item)

        newToppings.append(newTopping)

    # TODO: Check if price of the pizza exists, and update if so.
    newPrice = Price(size_s=s_price, size_m=m_price, size_l=l_price, size_xl=xl_price)

    newPizza = Pizza(name=name, prices=newPrice, toppings=newToppings);
    db.session.add(newPizza)