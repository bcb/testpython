"""flasktest.py"""

from flask.ext.testing import TestCase

class TestFlask(TestCase):

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    TESTING = True

    @staticmethod
    def setup_db(db):
        db.create_all()

    @staticmethod
    def teardown_db(db):
        db.session.remove()
        db.drop_all()
