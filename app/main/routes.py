# app/main/routes.py
from flask import Blueprint, render_template

# 1. Creiamo il Blueprint. Flask cercherà i template in app/main/templates
main_bp = Blueprint('main', __name__ , template_folder='templates')

@main_bp.route('/')
def index():
    # 2. Specifichiamo il percorso RELATIVO alla cartella templates del blueprint.
    # Flask cerca in: app/main/templates/main/index.html
    return render_template('main.html')