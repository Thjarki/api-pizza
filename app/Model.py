from marshmallow import fields, Schema, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

pizza_topping = db.Table('pizza_topping',
    db.Column('pizza_id', db.Integer, db.ForeignKey('pizza.id')),
    db.Column('topping', db.Integer, db.ForeignKey('topping.id')))


class Pizza(db.Model):
    __tablename__ = 'pizza'
    __table_args__ = (
        db.UniqueConstraint('name', 'company_id', name='unique_component_commit'),
    )
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    price_id = db.Column(db.Integer, db.ForeignKey('price.id'))
    name = db.Column(db.String(250), nullable=False)
    prices = db.relationship('Price', uselist=False, backref='pizza', lazy=True)
    toppings = db.relationship('Topping', secondary=pizza_topping, lazy='subquery')
    company = db.relationship('Company', uselist=False, backref='pizza', lazy=True)

    def __str__(self):
        return "%s,\n%s" % (self.name, self.toppings)


class Price(db.Model):
    __tablename__ = 'price'
    id = db.Column(db.Integer, primary_key=True)
    size_s = db.Column(db.Integer, nullable=True)
    size_m = db.Column(db.Integer, nullable=True)
    size_l = db.Column(db.Integer, nullable=True)
    size_xl = db.Column(db.Integer, nullable=True)

    def __init__(self, size_s=None, size_m=None, size_l=None, size_xl= None):
        self.size_s = size_s
        self.size_m = size_m
        self.size_l = size_l
        self.size_xl = size_xl


class Topping(db.Model):
    __tablename__ = 'topping'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    type = db.Column(db.String(40), nullable=True)


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    region = db.Column(db.String(50), nullable=False,)
    delivers = db.Column(db.Boolean(), default=False, nullable=False,)
    description = db.Column(db.Text(), nullable=False, default='Description missing')


class WordFilter(db.Model):
    __tableName__ = 'word_filter'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False,)
    filter_word = db.Column(db.String(50), nullable=False,)
    replacement = db.Column(db.String(50), nullable=False,)


# Schemas
class PizzaSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    prices = fields.Nested('PriceSchema', exclude=('pizza_id',), many=False)
    toppings = fields.Nested('ToppingSchema', many=True)
    company = fields.Nested('ComputerSchema', exclude=('id',), many=False)

class ToppingSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String()
    type = fields.String()


class PriceSchema(ma.Schema):
    id = fields.Integer()
    size_s = fields.String(allow_none=True)
    size_m = fields.String(allow_none=True)
    size_l = fields.String(allow_none=True)
    size_xl = fields.String(allow_none=True)
    pizza_id = fields.Integer(required=True)


class ComputerSchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    region = fields.String(required=True)
    delivers = fields.Boolean()
    description = fields.String()

