from app import app, db
from models.customer import Customer, customer_schema, customers_schema
from sqlalchemy import desc
from flask import request, jsonify
import datetime

date_format = '%d-%m-%Y'


@app.route('/customer', methods=["POST"])
def add_customer():
    name = request.json['name']
    dob = request.json['dob']
    dob_object = datetime.datetime.strptime(dob, date_format).date()
    new_customer = Customer(name, dob_object)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.dump(new_customer)


@app.route('/customer', methods=['GET'])
def get_all_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)


@app.route('/customer/<id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    return customer_schema.jsonify(customer)


@app.route('/customer/<id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    name = request.json['name']
    dob = request.json['dob']
    dob_object = datetime.datetime.strptime(dob, date_format)
    updated_at = datetime.datetime.now()
    customer.name = name
    customer.dob = dob_object
    customer.updated_at = updated_at

    db.session.commit()
    return customer_schema.jsonify(customer)


@app.route('/customer/list/<limit>', methods=['GET'])
def list_customers(limit):
    customers = Customer.query.order_by(desc(Customer.dob)).limit(limit).all()
    return jsonify(customers_schema.dump(customers))
