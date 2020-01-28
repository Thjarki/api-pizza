from flask_restful import Resource


class CompanyResource(Resource):
    def get(self):
        return {"message": "Connected"}
