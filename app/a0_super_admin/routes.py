from flask import Blueprint, render_template,  redirect, url_for

super_admin_bp = Blueprint('super_admin', __name__ , template_folder='templates') 

@super_admin_bp.route('/super_admin')
def area_0():
    return render_template('super_admin/super_admin.html')