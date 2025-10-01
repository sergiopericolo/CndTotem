from flask import Flask
import os 

def create_app(config_name = None):

    app = Flask(__name__) 

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'una_chiave_segreta_molto_difficile' 

    from .auth.routes import auth_bp
    from .a0_super_admin.routes import super_admin_bp
    from .a1_admin.routes import admin_bp
    from .a2_voting.routes import voting_bp

    app.register_blueprint(auth_bp) 
    app.register_blueprint(super_admin_bp, url_prefix='/super_admin_area') 
    app.register_blueprint(admin_bp, url_prefix='/admin_area') 
    app.register_blueprint(voting_bp, url_prefix='/voting_area')

    return app