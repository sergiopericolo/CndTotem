from flask import Blueprint, render_template,  redirect, url_for

auth_bp = Blueprint('auth', __name__ , template_folder='templates') 

@auth_bp.route('/')
def login():
    return render_template('auth/auth.html')


