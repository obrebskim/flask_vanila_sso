from flask import Flask
from flask_session import Session
from config import Config

session = Session()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Konfiguracja sesji serwerowej
    app.config['SESSION_TYPE'] = 'filesystem'
    session.init_app(app)
    
    # Rejestracja blueprintów
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app 