import os
from flask import current_app, render_template, request, Blueprint
from flask import g
from werkzeug.utils import secure_filename

bp = Blueprint('upload', __name__)


@bp.route('/upload/', methods=['POST', 'GET'])
def upload():
    upload_folder = 'app/uploads/'
    current_app.config['UPLOAD_FOLDER'] = upload_folder
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            g.filename = filename
            return render_template('app/upload_result.html')
    return render_template('app/upload.html')


@bp.route('/hello/')
def hello():
    return 'hello'




