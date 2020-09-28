from flask import Blueprint, request, render_template, g, abort
from werkzeug.utils import secure_filename
import os

bp = Blueprint('delete', __name__)


# deletes file by its name (name is hash from content of the file)
@bp.route('/delete/', methods=['POST', 'GET'])
def download():
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            filename = secure_filename(filename)
            delete_folder = 'store/{}'.format(filename[:2])
            os.remove(os.path.join(delete_folder, filename))
            g.filename = filename
            return render_template('app/delete_result.html')
    except FileNotFoundError:
        return abort(404)
    return render_template('app/delete.html')