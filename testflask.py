"""testflask.py"""

from flask.ext.testing import TestCase


class TestFlask(TestCase):

    def create_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config['TESTING'] = True
        app.config['LOGIN_DISABLED'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def login(self, username='admin', password='admin'):
        return self.client.post('/login', data=dict(
            username=username,
            password=password
        ))

    def logout(self):
        return self.client.get('/logout')
