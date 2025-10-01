from flask import Blueprint, render_template,  redirect, url_for

voting_bp = Blueprint('voting', __name__ , template_folder='templates') 

@voting_bp.route('/voting')
def area_2():
    return render_template('voting/voting.html')