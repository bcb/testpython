"""testflask.py"""

from flask.ext.testing import TestCase

class TestFlask(TestCase):
    @staticmethod
    def create_app(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config['TESTING'] = True
        return app
