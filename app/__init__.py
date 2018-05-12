from flask import Flask, g, request,jsonify 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config):
    app = Flask(__name__)

    app.config.from_mapping(config)

    db.init_app(app)


    from .routes import api as api_blueprints
    
    app.register_blueprint(api_blueprints,url_prefix='/api/v1')
    
    from .models.user import User
    from .auth import auth
    @app.route('/auth/signup/',methods=['POST'])
    def signup():
        user = User()
        user.from_json(request.json)
        db.session.add(user)
        db.session.commit()
        return jsonify({'result':user.to_josn()}), 201

    @app.route('/auth/login/', methods=['GET'])
    @auth.login_required
    def login():
        return jsonify({
            'token':g.user.generate_token()
        }), 200
    return app


