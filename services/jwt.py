from models.user import User
from functools import wraps
from flask import request, jsonify
from models.user import User
import jwt
from app import app
from utils.utils import success_response, error_response


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if request.headers.has_key('Authorization') or request.headers.has_key('x-access-token') or 'token' in request.json:
            token = request.headers.get(
                'x-access-token', None) or request.json.get('token', None) or request.headers.get('Authorization')
            token = token.replace('Bearer ', '')
        else:
            return jsonify(error_response('Token required'))
        try:
            decoded = jwt.decode(token, app.config['JWT_SECRET'])
            user = User.query.filter_by(id=decoded['id']).first()
            if not user:
                return jsonify(success_response('Invalid User'))
        except:
            return jsonify(error_response('Invalid Token'))
        return f(*args, **kwargs)
    return decorator
