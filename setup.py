import os
import sys
from setuptools import setup, find_packages

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

def getRequires():
    deps = ['github3.py',
            'requests',
            'beautifulsoup4',
            'sendgrid',
            'python-dateutil',
            'sqlalchemy',
            'datetime',
            'pyyaml',
            'six',
            'wheel',
            'zope.interface',
            'uritemplate',
            'uritemplate.py',
            'pytz',
            'python-http-client']
    if (3, 0) <= sys.version_info < (3, 2):
        deps.append('pymysql3')
    elif (3, 3) <= sys.version_info < (3, 6):
        deps.append('pymysql')
    return deps

base_url = 'https://github.com/sendgrid/'
setup(
    name='open_source_library_data_collector',
    version='1.1.0',
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url=base_url + 'open-source-library-data-collector',
    packages=find_packages(),
    license='MIT',
    description='Periodically capture external data relating to GitHub hosted Open Source libraries',
    long_description=long_description,
    install_requires=getRequires(),
    keywords=[
        'GitHub',
        'Open Source',
        'ROI',
        'Reporting',
        'Package Managers'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ]
)
