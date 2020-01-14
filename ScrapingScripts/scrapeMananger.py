from Model import db, Pizza, Price, Topping, Company

# Manager for inserting and reteving scraped data into and from database


# TODO: test
def get_pizza(pizza_name, company_id):
    return db.session.query(Pizza).filter_by(name=pizza_name, company_id=company_id)


# TODO: test
def add_pizza(name, toppings, company_id,  s_price=None, m_price=None, l_price=None, xl_price=None):
    pizza = get_pizza(name, company_id)

    if pizza is None:
        newToppings = []
        for item in toppings:  # Check if the topping exist,
            newTopping = db.session.query(Topping).filter_by(name=item).first()
            if newTopping is None:
                newTopping = Topping(name=item)

            newToppings.append(newTopping)
        pass
    else: # update existing pizza
        pizza.toppings
        pass

    pass


# TODO: test
def get_company():
    pass


# TODO: test
def add_company():
    pass




