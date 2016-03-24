Quickly and easily store data about your open source projects on GitHub and various Package Managers.

[![Travis Badge](https://travis-ci.org/sendgrid/open-source-library-data-collector.svg?branch=master)](https://travis-ci.org/sendgrid/open-source-library-data-collector)

# Local Installation

## Prerequisites ##

* [virtualenv](https://pypi.python.org/pypi/virtualenv)
* [mysql](https://www.mysql.com)

## Initial setup: ##

```
git clone https://github.com/sendgrid/open-source-library-data-collector.git
cd sendgrid-open-source-library-external-data
virtualenv venv
cp .env_sample .env
```

Update your settings in `.env`
```
mysql -u USERNAME -p -e "CREATE DATABASE IF NOT EXISTS open-source-library-data-collector"; 
mysql -u USERNAME -p open-source-external-library-data < db/data_schema.sql
cp config_sample.yml config.yml
```
Update the settings in `config.yml`
```
source venv/bin/activate
pip install -r requirements.txt
```
Update the code in `package_managers.py`. The functions `update_package_manager_data` and `update_db` was customized for our particular needs. You will want to either subclass those functions in your own application or modify it to suit your needs. We will remove these customizations in a future release. [Here is the GitHub issue](https://github.com/sendgrid/open-source-library-data-collector/issues/5) for reference.

## Usage ##

```
source venv/bin/activate
python app.py
```

# Heroku Deploy

```
heroku login
heroku create
heroku addons:create cleardb:ignite
```
Access the cleardb DB and create the tables in db/data_schema.sql
```
heroku config:add ENV=prod
heroku config:add GITHUB_TOKEN=<<your_github_token>>
heroku config:add SENDGRID_API_KEY=<<your_sendgrid_api_key>>
heroku addons:create scheduler:standard
```
Configure the schedular addon in your Heroku dashboard to run `python app.py` at your desired frequency.

Test by running `heroku run worker`

# Announcements

[2016.03.24] - We are live!

# Roadmap

[Milestones](https://github.com/sendgrid/open-source-library-data-collector/milestones)

# How to Contribute

We encourage contribution to our libraries, please see our [CONTRIBUTING](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md) guide for details.

# About

![SendGrid Logo]
(https://assets3.sendgrid.com/mkt/assets/logos_brands/small/sglogo_2015_blue-9c87423c2ff2ff393ebce1ab3bd018a4.png)

open-source-library-data-collector is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

open-source-library-data-collector is maintained and funded by SendGrid, inc. The names and logos for open-source-external-library-data are trademarks of SendGrid, inc.
