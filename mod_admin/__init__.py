from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin/')


@admin.route('/')
def admin_index():
    return 'Hello From admin_index'
