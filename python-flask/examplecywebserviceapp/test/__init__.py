import logging

from flask_testing import TestCase

from examplecywebserviceapp.__main__ import create_app


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        return create_app().app
