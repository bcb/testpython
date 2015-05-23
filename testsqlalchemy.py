"""testsqlalchemy.py"""

from flask_sqlalchemy import SQLAlchemy
from unittest import TestCase

def requires_db(db):
    """Decorator for setting up and tearing down the database"""
    def decorator(function_to_decorate):
        if not isinstance(db, SQLAlchemy):
            raise TypeError('No db passed to requires_db')
        def wrapper(self):
            db.create_all()
            db.session.begin_nested()
            try:
                ret = function_to_decorate(self)
            except:
                raise
            finally:
                db.session.rollback()
                db.session.remove()
                db.drop_all()
            return ret
        return wrapper
    return decorator
