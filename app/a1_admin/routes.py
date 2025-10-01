from flask import Blueprint, render_template,  redirect, url_for

admin_bp = Blueprint('admin', __name__ , template_folder='templates') 

@admin_bp.route('/admin')
def area_1():
    return render_template('admin/admin.html')