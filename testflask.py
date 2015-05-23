"""testflask.py"""

import sys
import os

from flask.ext.testing import TestCase


class TestFlask(TestCase):

    @staticmethod
    def configure_app(app):
#        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'postgresql://apps@localhost/testing'
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def login(self, uri='/login', username='admin', password='admin'):
        response = self.client.post(uri, data=dict(
            username=username,
            password=password
        ))
        self.assertStatus(response, 302)

    def logout(self, uri='/login'):
        return self.client.get('/logout')
