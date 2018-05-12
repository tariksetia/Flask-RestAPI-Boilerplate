from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from .models.user import User

auth = HTTPBasicAuth()
auth_token = HTTPBasicAuth()

@auth.verify_password
def verify_password(username,password):
    g.user = User.query.filter_by(username=username).first()
    if g.user is None:
        return False
    return g.user.check_password(password)

@auth.error_handler
def unauthorizer():
    res =  jsonify({
        'status':401,
        'error':'Unauthorized Request',
        'message':'Please Authenticate'
    })
    res.status_code = 401
    return res 

@auth_token.verify_password
def verify_token(token,unused): # You Forget 'unsued'
    g.user = User.verify_token(token)
    return g.user is not None

@auth_token.error_handler
def unauthorized_token():
    response = jsonify({'status': 401, 'error': 'unauthorized',
                        'message': 'please send your authentication token'})
    response.status_code = 401
    return response
