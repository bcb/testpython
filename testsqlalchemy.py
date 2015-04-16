"""testsqlalchemy.py"""

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
