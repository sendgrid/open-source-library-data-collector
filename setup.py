import os
import sys
from setuptools import setup, find_packages


def getRequires():
    deps = ['github3.py',
            'requests',
            'beautifulsoup4',
            'sendgrid',
            'python-dateutil',
            'sqlalchemy',
            'datetime',
            'pyyaml']
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
        deps.append('pymysql')
        deps.append('pyopenssl')
        deps.append('ndg-httpsclient')
        deps.append('pyasn1')
    elif (2, 7) <= sys.version_info < (3, 0):
        deps.append('pymysql')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('pymysql3')
    elif (3, 3) <= sys.version_info < (3, 6):
        deps.append('pymysql')
    return deps

base_url = 'https://github.com/sendgrid/'
setup(
    name='open-source-library-data',
    version='1.0.0',
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url=base_url + 'sendgrid-open-source-library-external-data',
    packages=find_packages(),
    license='MIT',
    description='GitHub and Package Manager data retrieval',
    long_description='Check out the README at GitHub',
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
