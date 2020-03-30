
__version__ = '0.0.1'

from pathlib import Path

import yaml
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint


def create_app():
    root_path, path = Path(__file__).parents[1], ''
    app = Flask(__name__)

    path = root_path / 'logging.yaml'
    # Creates API docs endpoint from swagger file.
    doc_path = str(root_path / 'doc/swagger.yaml')
    swagger_yml = yaml.safe_load(open(doc_path, 'r'))
    # Register Swagger UI.
    app.register_blueprint(get_swaggerui_blueprint('/docs', doc_path, config={
        'spec': swagger_yml}), url_prefix='/docs')

    # Start controller
    from main.controller.start_controller import start_route
    app.register_blueprint(start_route)
    return app
