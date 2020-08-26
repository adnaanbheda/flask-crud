from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import config
import os
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
ma = Marshmallow(app)
db.create_all()
from routes import customers


@app.route('/signup', methods=['POST'])
def signup():
    pass


@app.route('/login', methods=['POST'])
def login():
    pass


if __name__ == "__main__":
    app.run(debug == True)
