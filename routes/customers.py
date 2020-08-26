from app import app, db
from models.customer import Customer, customer_schema, customers_schema
from sqlalchemy import desc
from flask import request, jsonify
import datetime
from services.jwt import auth_required
from utils.utils import success_response, error_response, parse_date


@app.route('/customer', methods=["POST"])
@auth_required
def add_customer():
    name = request.json['name']
    dob = request.json['dob']
    dob_object = parse_date(dob)
    if not dob_object:
        return jsonify(error_response("Invalid Date"))
    new_customer = Customer(name, dob_object)
    db.session.add(new_customer)
    db.session.commit()
    return customer_schema.dump(new_customer)


@app.route('/customer', methods=['GET'])
@auth_required
def get_all_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)


@app.route('/customer/<id>', methods=['GET'])
@auth_required
def get_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify(error_response("Customer doesn't exist"))
    return customer_schema.jsonify(customer)


@app.route('/customer/<id>', methods=['PUT'])
@auth_required
def update_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify(error_response("Customer doesn't exist"))
    name = request.json['name']
    dob = request.json['dob']
    dob_object = parse_date(dob)
    if not dob_object:
        return jsonify(error_response("Invalid Date"))
    updated_at = datetime.datetime.now()
    customer.name = name
    customer.dob = dob_object
    customer.updated_at = updated_at
    db.session.commit()
    return customer_schema.jsonify(customer)


@app.route('/customer/list/<limit>', methods=['GET'])
@auth_required
def list_customers(limit):
    customers = Customer.query.order_by(desc(Customer.dob)).limit(limit).all()
    return jsonify(customers_schema.dump(customers))


@app.route('/customer/<id>', methods=['DELETE'])
@auth_required
def delete_customer(id):
    try:
        customer = Customer.query.get(id)
        if not customer:
            return jsonify(error_response("Customer doesn't exist"))
        db.session.delete(customer)
        db.session.commit()
        return jsonify(success_response('Successfully Deleted.'))
    except:
        return jsonify(error_response('Something went wrong'))
