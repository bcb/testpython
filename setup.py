"""setup.py"""

from setuptools import setup

setup(
    name='testingpython',
    description='My own classes for testing python.',
    author='Beau Barker',
    author_email='beauinmelbourne@gmail.com',
    py_modules=['testflask'],
    tests_require=['tox'],
    )
