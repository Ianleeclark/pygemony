import os
from setuptools import setup

# 
CLASSIFIERS = [
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"
] 
#

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygemony',
    install_requires=read('requirements.txt'),
    version='0.1.1b',
    description=('Parse long-forgotten TODO messages from Github Repos and create Issues to resolve.'),
    license=read("LICENSE"),
    author='Ian Lee Clark',
    author_email='ian@ianleeclark.com',
    packages=['pyg'],
    url='https://github.com/GrappigPanda/pygemony',
    classifiers=CLASSIFIERS,
    scripts=['pygemony.py']
)
