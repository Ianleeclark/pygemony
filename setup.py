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
    install_requires=read('requirements/all.txt'),
    version='0.4.2',
    description=('Parse long-forgotten TODO messages from Github Repos and create Issues to resolve.'),
    license=read("LICENSE"),
    author='Ian Lee Clark',
    author_email='ian@ianleeclark.com',
    packages=['pyg'],
    url='https://github.com/GrappigPanda/pygemony',
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': [
            'pygemony = pyg.run:main',
        ],
    }
)
