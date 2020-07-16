from flask import Blueprint, request, send_file, render_template
from werkzeug.utils import secure_filename
import os

bp = Blueprint('download', __name__)


@bp.route('/download/', methods=['POST', 'GET'])
def download():
    try:
        if request.method == 'POST':
            filename = request.form['filename']
            filename = secure_filename(filename)
            download_folder = 'uploads/'
            path = os.path.join(download_folder, filename)
            return send_file(path, as_attachment=True)
    except FileNotFoundError:
            return 'No such File'
    return render_template('app/download.html')



