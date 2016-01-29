# Install and run locally #

## Prerequisites ##

* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [mysql](https://www.mysql.com)

## Initial setup: ##

```
git clone https://github.com/sendgrid/sendgrid-open-source-library-external-data.git
cd sendgrid-open-source-library-external-data
virtualenv venv
cp .env_sample .env
```
Update your settings in `.env`
```
mysql -u USERNAME -p -e "CREATE DATABASE IF NOT EXISTS open-source-external-library-data"; 
mysql -u USERNAME -p open-source-external-library-data < db/data_schema.sql
cp config_sample.yml config.yml
```
Update the settings in `config.yml`
```
source venv/bin/activate
pip install -r requirements.txt
```

## Execute: ##

```
source venv/bin/activate
python app.py
```

# Testing #

## Prequisites: ##

The above local "Initial setup" is complete

* [pyenv](https://github.com/yyuu/pyenv)
* [tox](https://pypi.python.org/pypi/tox)
* [pandoc](http://pandoc.org)
 
## Initial setup: ##

Add eval "$(pyenv init -)" to your .profile after installing tox, you only need to do this once.

```
pyenv install 2.6.9
pyenv install 2.7.8
pyenv install 3.2.6
pyenv install 3.3.6
pyenv install 3.4.3
pyenv install 3.5.0
python setup.py install
pyenv local 3.5.0 3.4.3 3.3.6 3.2.6 2.7.8 2.6.9
pyenv rehash
````

## Execute: ##

```
source venv/bin/activate
tox
```