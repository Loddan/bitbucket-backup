# coding: utf8
import os
import sys
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = ''
try:
    README = open(os.path.join(here, 'README.rst')).read()
except:
    pass

REQUIREMENTS = []

if sys.version_info < (2, 7) or (3,) <= sys.version_info < (3, 2):
    # In the stdlib from 2.7:
    REQUIREMENTS.append('argparse')


setup(
    name='Bitbucket_backup',
    version='0.1',
    author='Sam Kuehn',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'bitbucket-backup = bitbucket_backup.__main__:main'
        ],
    },
)
