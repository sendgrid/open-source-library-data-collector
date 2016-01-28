import os
import sys
import urlparse
from sqlalchemy import create_engine, MetaData, Table, exc
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime
from config import *

if (os.environ.get('ENV') != 'prod'):
    Config.init_environment()
    mysql_db = os.environ.get('MYSQL_DB')
    mysql_host = os.environ.get('MYSQL_HOST')
    mysql_username = os.environ.get('MYSQL_USERNAME')
    mysql_password = os.environ.get('MYSQL_PASSWORD')
    mysql_port = os.environ.get('MYSQL_PORT')
else:
    url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
    mysql_db = url.path[1:]
    mysql_host = url.hostname
    mysql_username = url.username
    mysql_password = url.password
    mysql_port = '3306'
    
connect_string = 'mysql+pymysql://' + mysql_username + ':' + mysql_password + '@' + mysql_host + ':' + mysql_port + '/' + mysql_db
engine = create_engine(connect_string)
Base = declarative_base(engine)

class GitHubData(Base):
    __tablename__ = 'github_data'
    __table_args__ = {'autoload':True}
    
class PackageManagerData(Base):
    __tablename__ = 'package_manager_data'
    __table_args__ = {'autoload':True}
    
def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    
class DBConnector(object):
    """CRUD for the sync email list database, focused on un/resubscribes"""    
    def __init__(self):
        self.session = loadSession()
        return
        
    def add_data(self, data_object):
        res = self.session.merge(data_object)
        self.session.commit()
        return res