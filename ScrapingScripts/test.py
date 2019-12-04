from .Model import db, Pizza

pizza = Pizza(name="pizza69")

db.session.add(pizza)
db.session.commit()
