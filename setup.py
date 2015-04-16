"""setup.py"""

from setuptools import setup

setup(
    name='testpython',
    description='My own classes for testing python.',
    author='Beau Barker',
    author_email='beauinmelbourne@gmail.com',
    py_modules=['testflask', 'testsqlalchemy'],
    tests_require=['tox'],
    )
