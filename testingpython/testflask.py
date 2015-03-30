"""flasktest.py"""

from flask.ext.testing import TestCase

def requires_db(db):
    """Decorator for setting up and tearing down the database"""
    def decorator(function_to_decorate):
        def wrapper(self):
            db.drop_all()
            db.create_all()
            ret = function_to_decorate(self)
            db.session.remove()
            db.drop_all()
            return ret
        return wrapper
    return decorator

class TestFlask(TestCase):

    def create_app(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
        app.config['TESTING'] = True
        return app
