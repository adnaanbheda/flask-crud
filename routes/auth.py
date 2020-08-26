from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from flask import jsonify, request
import jwt
import datetime
import os
from utils.utils import success_response, error_response


@app.route('/login', methods=['POST'])
def login():
    username = None
    password = None
    auth = request.authorization or None
    if auth:
        username = auth.username
        password = auth.password
    else:
        username = request.json['username']
        password = request.json['password']
    if (username and password):
        user = User.query.filter_by(username=username).first()
        print(user.password)
        if check_password_hash(str(user.password), password):
            token = jwt.encode({'id': user.id,
                                'exp': datetime.datetime.now() + datetime.timedelta(hours=24)},
                               app.config['JWT_SECRET'])
            return jsonify({'token': token.decode('UTF-8')})
        return jsonify(error_response('Invalid credentials')), 401
    else:
        return jsonify(error_response('No credentials')), 400


@app.route('/signup', methods=['POST'])
def signup():
    try:
        if {'username', 'password'} <= request.json.keys():
            username = request.json['username']
            password = request.json['password']
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username, hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'message': "User successfully created"}), 200
        else:
            return jsonify(error_response('Please submi0t a username and a password')), 400
    except Exception as e:
        if os.environ.get('ENV', None) == 'production':
            return jsonify(error_response('Something went wrong')), 500
        else:
            return jsonify(error_response(str(e))), 500
