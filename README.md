# Install and run locally #

## Prerequisites ##

* [Homebrew](http://brew.sh/)
* [Python 2.7.10](https://www.python.org/)
* [virtualenv](https://pypi.python.org/pypi/virtualenv)

## Initial setup: ##

```
brew install pip
pip install virtualenv
git clone https://github.com/sendgrid/sendgrid-open-source-library-external-data.git
cd sendgrid-open-source-library-external-data
virtualenv venv
cp .env_sample .env
```
Update your settings in `.env` and create your database for this project (the table name is defined in the .env_sample)
```
mysql -u USERNAME -p DBNAME < db/data_schema.sql
source venv/bin/activate
pip install -r requirements.txt
```

## Execute: ##

```
source venv/bin/activate
python app.py
```

