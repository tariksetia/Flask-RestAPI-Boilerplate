import os
from configs.config import Configuration
from app import create_app, db
from app.models.user import User

if __name__ == '__main__':
    env = os.environ.get('FLASK_ENV','development')
    env_config = Configuration.data[env]
    app = create_app(env_config)

    with app.app_context():
        db.create_all()
        if User.query.get(1) is None:
            user = User()
            user.username = 'admin'
            user.set_password('admin')
            db.session.add(user)
            db.session.commit()

    app.run()