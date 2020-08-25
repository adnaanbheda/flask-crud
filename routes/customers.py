from app import app
from models import customers


@app.route('/')
def index():
    return 'Hello Customers'
