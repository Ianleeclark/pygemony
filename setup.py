import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pygemony',
      version='0.0.1',
      description='Parse TODO from github directory',
      author='Ian Lee Clark',
      author_email='ian@ianleeclark.com',
      packages=['pyg'],
      url='https://github.com/GrappigPanda/pygemony',
      scripts=['pygemony.py'])