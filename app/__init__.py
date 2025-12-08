from flask import Flask
from app.extenshions import *
from app.models import User
from flask_login import current_user
import os
from config import Config

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    from app.routes.auth import auth
    from app.routes.routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)


    with app.app_context():
        db.create_all()
    return app