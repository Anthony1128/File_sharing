from flask import Blueprint, request, send_from_directory, render_template, abort
from werkzeug.utils import secure_filename
import os

bp = Blueprint('download', __name__)


# downloads file by its name (name is hash from content of the file)
@bp.route('/download/', methods=['POST', 'GET'])
def download():
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            filename = secure_filename(filename)
            download_folder = '../store/'
            path = os.path.join(download_folder, filename[:2])
            return send_from_directory(path, filename, as_attachment=True)
    except FileNotFoundError:
        return abort(404)
    return render_template('app/download.html')



