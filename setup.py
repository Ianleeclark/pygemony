import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygemony',
    version='0.0.1a',
    description=('Parse TODO from github directory'),
    license="MIT",
    author='Ian Lee Clark',
    author_email='ian@ianleeclark.com',
    packages=['pyg'],
    url='https://github.com/GrappigPanda/pygemony',
    scripts=['pygemony.py']
)
