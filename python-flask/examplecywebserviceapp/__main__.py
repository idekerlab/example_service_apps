#!/usr/bin/env python3

import connexion
from flask import make_response
from flask import request

from examplecywebserviceapp import encoder

CORS_ALLOW_METHODS = 'DELETE, GET, PUT, POST, OPTIONS'
CORS_ALLOW_HEADERS = 'Content-Type, Authorization'


def create_app():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder

    # The API is mounted at /example and the metadata endpoint is defined as
    # path "/". Without this, Flask redirects /example to /example/, which
    # breaks browser CORS preflight requests with a 308 response.
    app.app.url_map.strict_slashes = False

    app.add_api('openapi.yaml',
                arguments={'title': 'Example Cytoscape Service-App API'},
                pythonic_params=True)

    @app.app.before_request
    def handle_options_request():
        if request.method == 'OPTIONS':
            response = make_response('', 204)
            response.headers['Allow'] = CORS_ALLOW_METHODS
            return response

    @app.app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = CORS_ALLOW_METHODS
        response.headers['Access-Control-Allow-Headers'] = request.headers.get(
            'Access-Control-Request-Headers',
            CORS_ALLOW_HEADERS)
        return response

    return app


def main():
    app = create_app()
    app.run(port=8080)


if __name__ == '__main__':
    main()
