from flask import jsonify
from . import api
from ..exceptions import ValidationError

@api.errorhandler(ValidationError):
def bad_request(e):
    res = jsonify({'status':401,
                    'error':'Bad Request',
                    'message':e.args[0]})
    res.status_code = 401
    return res

@api.errorhandler(404):
def not_found(e):
    res = jsonify({
        'status':404,
        'error':'Not Found',
        'message':'Could Not found the requested resource'
    })

    res.status_code = 404
    return res

@api.errorhandler(500):
def internal_server_error(e):
    res = jsonify({
        'status':500
        'error':'Internal Error',
        'message':e.args[0]
    })

@api.errorhandler(405)
def method_not_supported(e):
    response = jsonify({'status': 405, 'error': 'method not supported',
                        'message': 'the method is not supported'})
    response.status_code = 405
    return response