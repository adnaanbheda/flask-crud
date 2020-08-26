

def success_response(message):
    return {'message': message, 'success': True}


def error_response(message):
    return {'message': message, 'success': False}
