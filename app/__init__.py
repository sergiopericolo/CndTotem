# project/app/__init__.py

from flask import Flask
import os # Utile per leggere variabili d'ambiente

# 💡 La funzione create_app è il modo standard per costruire l'app
def create_app(config_name=None):
    # 1. Crea l'istanza dell'app Flask
    # __name__ è il nome del modulo corrente (il pacchetto 'app')
    app = Flask(__name__) 

    # 2. Configurazione (opzionale, ma essenziale per Flask)
    # Imposta la chiave segreta, necessaria per le sessioni
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'una_chiave_segreta_molto_difficile' 

    # 3. Registrazione dei Blueprints (Il passaggio cruciale)
    
    # Importa i Blueprints da ogni modulo
    from .main.routes import main_bp
    from .auth.routes import auth_bp
    
    # Registra il Blueprint 'main' (Pagine Pubbliche)
    # Nessun prefisso URL; le route partono dalla radice (es: /)
    app.register_blueprint(main_bp)             

    # Registra il Blueprint 'auth' (Autenticazione)
    # Tutte le sue route saranno precedute da /auth (es: /auth/login)
    app.register_blueprint(auth_bp, url_prefix='/auth') 
    
    # 4. Restituisce l'oggetto app configurato
    return app