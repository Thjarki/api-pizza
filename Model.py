from marshmallow import fields, Schema, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

toppings = db.Table('toppings',
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id'), primary_key=True),
    db.Column('topping', db.Integer, db.ForeignKey('topping.id'), primary_key=True))


class Pizza(db.Model):
    __tablename__ = 'pizza'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    prices = db.relationship('Price', uselist=False ,backref='pizza', lazy=True)
    toppings = db.relationship('Topping', secondary=toppings, lazy='subquery')
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __str__(self):
        return "%s,\n%s" % (self.name, self.toppings)


class Price(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.Integer, primary_key=True)
    size_s = db.Column(db.String(), nullable=True)
    size_m = db.Column(db.Integer, nullable=True)
    size_l = db.Column(db.Integer, nullable=True)
    size_xl = db.Column(db.Integer, nullable=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'),
                         nullable=False)

    def __init__(self, size_s=None, size_m=None, size_l=None, size_xl= None):
        self.size_s = size_s
        self.size_m = size_m
        self.size_l = size_l
        self.size_xl = size_xl


class Topping(db.Model):
    __tablename__ = 'topping'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    pizzas = db.relationship('Pizza', secondary=toppings, lazy='subquery')


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    region = db.Column(db.String(50), nullable=False,)
    pizzas = db.relationship('Pizza')


# Schemas
class PizzaSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    prices = fields.Nested('PriceSchema', exclude=('pizza_id',), many=False)
    toppings = fields.Nested('ToppingSchema', exclude=('pizzas',), many=True)


class ToppingSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    pizzas = fields.Nested('PizzaSchema', exclude=('toppings',), many=True)


class PriceSchema(ma.Schema):
    id = fields.Integer()
    size_s = fields.String(allow_none=True)
    size_m = fields.String(allow_none=True)
    size_l = fields.String(allow_none=True)
    size_xl = fields.String(allow_none=True)
    pizza_id = fields.Integer(required=True)

