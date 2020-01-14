import requests
from bs4 import BeautifulSoup
from Model import db, Pizza, Price, Topping, Company

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

        company_id = add_company(name='Pizza Smiðjan', region='norðuland')
        add_scraped_pizza(pizza_name, pizza_topping_list, company_id, m_price=pizza_mid_price)
    return


# TODO: test, with mock_data
def add_company(name, region, delivers=False):
    company = db.session.query(Company).filter_by(name=name).first()
    if company is None:
        company = Company(name=name, region=region, delivers=delivers)
        db.session.add(company)
        db.session.commit()

    return company.id


# TODO: test, with mock_data
def add_scraped_pizza(name, scraped_toppings, company_id,  s_price=None, m_price=None, l_price=None, xl_price=None):
    newToppings = []
    for item in scraped_toppings:  # Check if the topping exist,
        newTopping = db.session.query(Topping).filter_by(name=item).first()
        if newTopping is None:
            newTopping = Topping(name=item)

        newToppings.append(newTopping)

    # TODO: Check if price of the pizza exists, and update if so.
    newPrice = Price(size_s=s_price, size_m=m_price, size_l=l_price, size_xl=xl_price)

    newPizza = Pizza(name=name, company_id=company_id, prices=newPrice, toppings=newToppings);
    db.session.add(newPizza)