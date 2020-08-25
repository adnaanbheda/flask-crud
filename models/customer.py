from app import db


class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(Date)
    updated_at = Column(DateTime)

    def __repr__(self):
        return "<Customer(%s,%s,%s,%s)" % (self.name, self.dob, self.updated_at)
