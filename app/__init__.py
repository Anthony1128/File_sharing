from flask import Flask, render_template
from . import upload
from . import download
from . import delete


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('app/index.html')

    app.register_blueprint(upload.bp)

    app.register_blueprint(download.bp)

    app.register_blueprint(delete.bp)

    return app



