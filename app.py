from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config['ENV'] == 'testing':
    app.config.from_object('config.TestingConfig')
else:
    app.config.from_object("config.DevelopmentConfig")

# ORM setup
db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()

# Routes setup
import routes.customers
import routes.auth

if __name__ == "__main__":
    app.run(debug=True)
