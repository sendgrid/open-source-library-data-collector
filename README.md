Quickly and easily store data about your open source projects on GitHub and various Package Managers.

<<Travis Badge>> <<CodeClimate Badge>> <<Language Specific Badges>>

# Installation

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

# Usage

```
source venv/bin/activate
python app.py
```

# Announcements

<<Library Specific Announcements Here>>

## Roadmap

<<Use Milestones and Issues>>

<<Describe each Milestone>>

## How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](<<Link to Contributing Guide>>) guide for details.

## Usage

<<Endpoint Name (pull from docs)>>
<<Endpoint Description (pull from docs)>>
<<Link to Example Code>>

...

## Unsupported Libraries

<<Link to Community Contributed Libraries>>

## About

<<SendGrid Logo>>

<<Library Name>> is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

<<Library Name>> is maintained and funded by SendGrid, inc. The names and logos for <<Library Name>> are trademarks of SendGrid, inc.