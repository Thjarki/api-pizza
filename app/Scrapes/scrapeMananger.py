from app.Model import db, Pizza, Price, Topping, Company, WordFilter
from sqlalchemy import exists, and_

# Manager for inserting and reteving scraped data into and from database


# TODO: test
def get_pizza(pizza_name=None, company_id=None):
    if pizza_name and company_id is None:
        db.session.query(Pizza).all()
    if company_id is None:
        return db.session.query(Pizza).filter_by(name=pizza_name).first()
    else:
        return db.session.query(Pizza).filter_by(name=pizza_name, company_id=company_id).first()


def pizza_exists(name, company_id):
    return db.session.query(exists().where(and_(Pizza.name == name, Pizza.company_id == company_id))).scalar()


def update_pizza():
    pass


# TODO: refactor and create test
def add_scraped_pizza(name, scraped_toppings, company_id,  s_price=None, m_price=None, l_price=None, xl_price=None):
    # TODO: Update pizza
    if pizza_exists(name, company_id):
        return

    newToppings = []
    scraped_toppings = filter_toppings(company_id, scraped_toppings)
    for item in scraped_toppings:  # Check if the topping exist,
        newTopping = db.session.query(Topping).filter_by(name=item).first()
        if newTopping is None:
            newTopping = Topping(name=item)

        newToppings.append(newTopping)

    # TODO: Check if price of the pizza exists, and update if so.
    newPrice = Price(size_s=s_price, size_m=m_price, size_l=l_price, size_xl=xl_price)

    newPizza = Pizza(name=name, company_id=company_id, prices=newPrice, toppings=newToppings);
    db.session.add(newPizza)

    return newPizza


# TODO: create test
def get_company():
    pass


# TODO: create test
def insert_or_get_company(name, region, delivers=False):
    company = db.session.query(Company).filter_by(name=name).first()
    if company is None:
        company = Company(name=name, region=region, delivers=delivers)
        db.session.add(company)
        db.session.commit()

    return company


# TODO: create test
def filter_toppings(company_id, toppings_list):
    filtered = []
    if db.session.query(WordFilter).filter_by(company_id=company_id).first() is None:
        return toppings_list

    for item in toppings_list:
        word_filter = db.session.query(WordFilter).filter_by(company_id=company_id, filter_word=item).first()
        if word_filter is not None:
            filtered.append(word_filter.replacement)
        else:
            filtered.append(item)

    return filtered
