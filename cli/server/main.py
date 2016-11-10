import os

from flask import Flask
from flask import send_file, send_from_directory, redirect
from flask_restful import abort

from server.api import load_api


def setup_routes(app):
    @app.route('/')
    def index():
        return redirect('/site/index.html')

    @app.route('/site/<path:path>')
    def send_js(path):
        return send_from_directory('../website/dist', path)

        # MEDIA_PATH = app.config.get('MEDIA_PATH')
        # if not os.path.isdir(MEDIA_PATH):
        #     os.mkdir(MEDIA_PATH)
        #
        # @app.route('/uploads/<path:filename>')
        # def base_static(filename):
        #     return send_from_directory(MEDIA_PATH, filename)


def create_app(name=None):
    app = Flask(name or 'app')
    app.config.from_pyfile('settings.py')
    load_api(app)
    setup_routes(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', 8000, True, use_reloader=True)
