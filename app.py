from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config
import os
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configuration
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
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
