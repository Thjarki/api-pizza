from flask_restful import Resource
from app.Model import db, PizzaSchema, Topping, Company, ComputerSchema

companies_schema = ComputerSchema(many=True)
company_schema = ComputerSchema()

class CompanyResource(Resource):
    def get(self):
        companies = Company.query.all()

        return {"message": "success", 'data': companies_schema.dump(companies)}
