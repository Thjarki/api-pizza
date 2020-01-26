import unittest
from app import create_app
from app.Model import db
from config import Test


class TestClass(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Test)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_api_connection(self):
        rv = self.client.get('api/')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
