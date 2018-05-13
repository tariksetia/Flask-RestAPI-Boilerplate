from flask import request
from . import api
from .. import db
from ..models.event import Event
from ..decorators.json import json
from ..decorators import paginate

@api.route('/events/', methods=['GET'])
@json
@paginate('events')
def get_events():
    return Event.query

@api.route('/events/<int:id>', methods=['GET'])
@json
def get_event(id):
    event =  Event.query.get_or_404(id)
    return {'result':event.to_dict()}, 200

@api.route('/events/', methods=['POST'])
@json
def post_event():    
    event = Event()
    event.from_dict(request.json)
    db.session.add(event)
    db.session.commit()
    return {'result':event.to_dict()}, 201