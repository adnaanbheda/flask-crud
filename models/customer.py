from app import db, ma
import datetime


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    dob = db.Column(db.Date)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return "<Customer(%s,%s,%s,%s)" % (self.name, self.dob, self.updated_at)


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ["id", "name", "dob", "updated_at"]


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
