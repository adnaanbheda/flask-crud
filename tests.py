from flask_testing import TestCase
from flask import Flask
from app import app, db
from models.user import User
import unittest


class DBTest(TestCase):
    TESTING = True

    def create_app(self):
        db.init_app(app)
        db.create_all()
        app.config['TESTING']
        return app

    def setUp(self):
        db.create_all()

    def test_add_user(self):
        user = User('adnaan', 'adnaan')
        db.session.add(user)
        db.session.commit()
        record = User.query.get(user.id)
        assert record.username == user.username

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()
