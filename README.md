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
Update your settings in `.env` and create your database for this project (the table name is open-source-external-library-data)
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

