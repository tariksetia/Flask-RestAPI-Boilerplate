from flask import jsonify, request
from . import api
from .. import db
from ..models.event import Event

@api.route('/events/', methods=['GET'])
def get_events():
    events = [event.get_url for event in Event.query.all()]
    return jsonify({'events':events}),200

@api.route('/events/<int:id>', methods=['GET'])
def get_event(id):
    event =  Event.query.get_or_404(id).first()
    return jsonify({'result':event.to_json()}), 200

@api.route('/events/', methods=['POST'])
def post_event():    
    event = Event()
    event.from_json(request.data)
    db.session.add(event)
    db.session.commit()
    return jsonify({'result':event.to_json}), 201