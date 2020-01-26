import unittest
from app import create_app
from app.Model import db, Company, Pizza, Topping
from config import Test
import app.Scrapes.scrapeMananger as Sm


class TestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Test)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

        company = Company(name='SmalllComp', region='north')
        db.session.add(company)
        db.session.commit()

    def company_count(self):
        return db.session.query(Company).count()

    def pizza_count(self):
        return db.session.query(Pizza).count()

    def topping_count(self):
        return db.session.query(Topping).count()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_pizza(self):
        self.assertEqual(self.pizza_count(), 0)
        toppings = ['pepperoni', 'ham']
        Sm.add_scraped_pizza(name='pizza', scraped_toppings=toppings, company_id=1, m_price=1700)
        self.assertEqual(Pizza.query.count(), 1)
        self.assertEqual(self.pizza_count(), 1)

    def test_get_pizza(self):
        toppings = ['pepperoni', 'ham']
        newpizza = Sm.add_scraped_pizza(name='pizza', scraped_toppings=toppings, company_id=1, m_price=1700)

        pizza = Sm.get_pizza(pizza_name='pizza')
        self.assertIs(pizza, newpizza)

        newpizza = Sm.add_scraped_pizza(name='pizzus', scraped_toppings=toppings, company_id=1, m_price=1500)

        self.assertNotEqual(pizza, newpizza)

    def test_pizza_exists(self):
        toppings = ['pepperoni', 'ham']
        Sm.add_scraped_pizza(name='pizza', scraped_toppings=toppings, company_id=1, m_price=1700)


        self.assertTrue(Sm.pizza_exists('pizza', 1))
        self.assertFalse(Sm.pizza_exists('pizzus', 1))
        self.assertFalse(Sm.pizza_exists('pizza', 2))
        self.assertFalse(Sm.pizza_exists('pizzus', 2))

