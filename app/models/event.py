from flask import url_for
from .. import db
from ..exceptions import ValidationError

class Event(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    tool = db.Column(db.String, nullable=False)
    log = db.Column(db.String, nullable=False)

    def get_url(self):
        return url_for('api.get_event', self.id, _external=True)

    def from_json(self):
        try:
            self.tool = data['tool']
            self.log = data['log']
        except Exception as e:
            raise ValidationError('Invaid Event Data: {}'.format(e.args[0]))
    
    def to_json(self):
        return {
            'id': self.id,
            'tool': self.tool,
            'log': self.log
        }
