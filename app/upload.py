from flask import current_app, render_template, request, Blueprint
from flask import g
import hashlib
import os

bp = Blueprint('upload', __name__)


# upload function
@bp.route('/upload/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            contents = file.read()
            hash_name = hashlib.md5(contents)  # making hash from content of a file
            filename = str(hash_name.hexdigest())

            # creating a folder if there is no one yet
            if not os.path.isdir('store/{}'.format(filename[:2])):
                os.mkdir('store/{}'.format(filename[:2]))

            # saving file with new name in exact folder
            upload_folder = 'store/{}'.format(filename[:2])
            current_app.config['UPLOAD_FOLDER'] = upload_folder
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            g.filename = filename
            return render_template('app/upload_result.html')
    return render_template('app/upload.html')



