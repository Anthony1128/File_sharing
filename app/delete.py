from flask import Blueprint, request, send_file, render_template, g
from werkzeug.utils import secure_filename
import os

bp = Blueprint('delete', __name__)


@bp.route('/delete/', methods=['POST', 'GET'])
def download():
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            filename = secure_filename(filename)
            delete_folder = 'app/uploads/'
            os.remove(os.path.join(delete_folder, filename))
            g.filename = filename
            return render_template('app/delete_result.html')
    except FileNotFoundError:
        return 'No such File'
    return render_template('app/delete.html')