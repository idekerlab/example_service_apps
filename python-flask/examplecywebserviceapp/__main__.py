#!/usr/bin/env python3

import connexion

from examplecywebserviceapp import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Example Cytoscape Service-App API'},
                pythonic_params=True)


    @app.app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, PUT, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response


    app.run(port=8080)


if __name__ == '__main__':
    main()
