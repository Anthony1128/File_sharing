from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('app/index.html')

    from . import upload
    app.register_blueprint(upload.bp)

    from . import download
    app.register_blueprint(download.bp)

    from . import delete
    app.register_blueprint(delete.bp)

    return app
