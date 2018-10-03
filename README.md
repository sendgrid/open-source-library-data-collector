![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)

[![Travis Badge](https://travis-ci.org/sendgrid/open-source-library-data-collector.svg?branch=master)](https://travis-ci.org/sendgrid/open-source-library-data-collector)
[![BuildStatus](https://travis-ci.org/sendgrid/open-source-library-data-collector.svg?branch=master)](https://travis-ci.org/sendgrid/open-source-library-data-collector)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/python)](https://dx.sendgrid.com/newsletter/python)
[![Twitter Follow](https://img.shields.io/twitter/follow/sendgrid.svg?style=social&label=Follow)](https://twitter.com/sendgrid)
[![GitHub contributors](https://img.shields.io/github/contributors/sendgrid/open-source-library-data-collector.svg)](https://github.com/sendgrid/open-source-library-data-collector/graphs/contributors)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)

**Quickly and easily store data about your open source projects on GitHub and various Package Managers.**

# Announcements

All updates to this project are documented in our [CHANGELOG](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CHANGELOG.md).

# Table of Contents
- [Installation](#installation)
- [Heroku Deploy](#heroku-deploy)
- [Roadmap](#roadmap)
- [How to Contribute](#contribute)
- [About](#about)
- [License](#license)

<a name="installation"></a>
# Installation

## Environment Variables

First, get your free SendGrid account [here](https://sendgrid.com/free?source=open-source-data-collector).

Next, update your environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys).

## Initial Setup

[Library Usage Documentation](USAGE.md)

If you enabled CSV exports in your `config.yml`, those files will appear under the `csv/` directory in the project repository.

## Dependencies

- The SendGrid Service, starting at the [free level](https://sendgrid.com/free?source=open-source-data-collector)
- [virtualenv](https://pypi.python.org/pypi/virtualenv)
- [mysql](https://www.mysql.com)

<a name="heroku-deploy"></a>
# Heroku Deploy

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

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
Configure the scheduler add-on in your Heroku dashboard to run `python app.py` at your desired frequency.

Test by running `heroku run worker`

<a name="roadmap"></a>
# Roadmap

If you are interested in the future direction of this project, please take a look at our [milestones](https://github.com/sendgrid/open-source-library-data-collector/milestones). We would love to hear your feedback.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our projects, please see our [CONTRIBUTING](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md) guide for details.

Quick links:

- [Feature Request](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md#feature_request)
- [Bug Reports](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md#submit_a_bug_report)
- [Sign the CLA to Create a Pull Request](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md#cla)
- [Improvements to the Codebase](https://github.com/sendgrid/open-source-library-data-collector/blob/master/CONTRIBUTING.md#improvements_to_the_codebase)
- [License](#license)

<a name="about"></a>
# About

open-source-library-data-collector is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

open-source-library-data-collector is maintained and funded by SendGrid, Inc. The names and logos for open-source-library-data-collector are trademarks of SendGrid, Inc.

<a name="license"></a>
# License

[The MIT License (MIT)](LICENSE.txt)
