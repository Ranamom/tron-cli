"""The setup.py file for Tron CLI."""

import sys

from setuptools import setup, find_packages

PKG_NAME = 'troncli'
PKG_AUTHOR = ', '.join(['Weiyu X'])
PKG_SCRIPTS = ['tron-cli']
PKG_REQUIRES = [
    'cbox==0.5.0',
    'certifi==2018.10.15',
    'chardet==3.0.4',
    'idna==2.7',
    'psutil==5.4.7',
    'requests==2.20.0',
    'six==1.11.0',
    'urllib3==1.24'
]

PKG_DESC = 'A command line tool to monitor and manage tron nodes.'

with open("README.md", "r") as fh:
    PKG_LONG_DESC = fh.read()

# get the version
version = {}
with open('{}/version.py'.format(PKG_NAME)) as fp:
    exec(fp.read(), version)

setup(
    name=PKG_NAME,
    version=version['__version__'],
    author=PKG_AUTHOR,
    author_email='weiyu@tron.network',
    description=PKG_DESC,
    long_description=PKG_LONG_DESC,
    long_description_content_type='text/markdown',
    url='https://github.com/tronprotocol/tron-cli',
    packages=find_packages(),
    zip_safe=False,
    scripts=PKG_SCRIPTS,
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=PKG_REQUIRES,
)
