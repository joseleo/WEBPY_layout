import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

config = {
    'description': 'My Project',
    'author': 'Jose León Barranco (@josejalen)',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'license': 'BSD',
    'keywords': 'example documentation tutorial',
    'author_email': 'joseleon.engineer@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project name'
}

setup(**config)
