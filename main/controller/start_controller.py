from flask import Blueprint

start_route = Blueprint('start_route', __name__)


@start_route.route('/')
def index():
    return 'Welcome to Sauron Warehouse API, read documentation in /docs ' \
           'for further questions.', 200
