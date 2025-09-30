from flask import Flask
import os 

def create_app(config_name=None):

    app = Flask(__name__) 

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'una_chiave_segreta_molto_difficile' 

    from .main.routes import main_bp
    from .auth.routes import auth_bp
    
    app.register_blueprint(main_bp)             
    app.register_blueprint(auth_bp, url_prefix='/auth') 

    return app