import os
import sys
from setuptools import setup, find_packages

def getRequires():
    deps = ['github3.py', 'requests', 'beautifulsoup4', 'sendgrid', 'python-dateutil',
            'sqlalchemy', 'datetime', 'pyyaml']
    if (2, 6) <= sys.version_info < (2, 7):
        deps.append('unittest2')
        deps.append('pymysql')
    elif (2, 7) <= sys.version_info < (3, 0):
        deps.append('pymysql')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('pymysql3')
    elif (3, 3) <= sys.version_info < (3, 6):
        deps.append('pymysql')
    return deps

"""
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()
"""

setup(
    name='open-source-library-data',
    version='1.0.0',
    author='Elmer Thomas',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-open-source-library-external-data',
    packages=find_packages(),
    license='MIT',
    description='GitHub and Package Manager data retrieval',
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

#long_description=read_md('./README.md'),