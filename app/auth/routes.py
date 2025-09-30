from flask import Blueprint, render_template, redirect, url_for

# Creiamo il Blueprint. Flask cercherà i template in app/auth/templates
auth_bp = Blueprint('auth', __name__ , template_folder='templates') 

@auth_bp.route('/login')
def login():
    # Specifichiamo il percorso RELATIVO alla cartella templates del blueprint.
    # Flask cerca in: app/auth/templates/auth/login.html
    return render_template('auth/auth.html')

@auth_bp.route('/logout')
def logout():
    # Reindirizziamo a un altro Blueprint
    return redirect(url_for('main')) 