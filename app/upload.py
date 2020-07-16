import os
from flask import current_app, render_template, request, redirect, url_for, Blueprint
from werkzeug.utils import secure_filename

bp = Blueprint('upload', __name__)


@bp.route('/upload/', methods=['POST', 'GET'])
def upload():
    upload_folder = '/uploaded_files'
    current_app.config['UPLOAD_FOLDER'] = upload_folder
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(filename))
            return 'Success'
    return render_template('app/upload.html')


@bp.route('/hello/')
def hello():
    return 'hello'




