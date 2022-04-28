import argparse
import pymongo
import os
from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
# from modules.auth import AUTH_REQUEST
from flask_pymongo import PyMongo
APP = Flask(__name__)
APP.SECRET_KEY = 'thisthesecret'

SWAGGER_URL = '/swagger'
API_URL2 = "/api/v1/"
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# APP.register_blueprint(AUTH_REQUEST, url_prefix=API_URL2+"auth")


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        APP.run(host='0.0.0.0', port=PORT, debug=False)
