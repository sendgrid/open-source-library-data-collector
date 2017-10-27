If you have a non-library SendGrid issue, please contact our [support team](https://support.sendgrid.com).

If you can't find a solution below, please open an [issue](https://github.com/sendgrid/sendgrid-python/issues).

## Table of Contents

* [Environment Variables and Your SendGrid API Key](#environment)
* [Error Messages](#error)
* [Version Convention](#versions)

<a name="environment"></a>
## Environment Variables and Your SendGrid API Key

All of our examples assume you are using [environment variables](https://github.com/sendgrid/sendgrid-python#setup-environment-variables) to hold your SendGrid API key.

If you choose to add your SendGrid API key directly (not recommended):

`apikey=os.environ.get('SENDGRID_API_KEY')`

becomes

`apikey='SENDGRID_API_KEY'`

In the first case SENDGRID_API_KEY is in reference to the name of the environment variable, while the second case references the actual SendGrid API Key.

<a name="error"></a>
## Error Messages

To read the error message returned by SendGrid's API in Python 2.X:

```python
import urllib2

try:
  response = sg.client.mail.send.post(request_body=mail.get())
except urllib2.HTTPError as e:
    print e.read()
```

To read the error message returned by SendGrid's API in Python 3.X:

```python
import urllib
try:
  response = sg.client.mail.send.post(request_body=mail.get())
except urllib.error.HTTPError as e:
    print e.read()
```

<a name="versions"></a>
## Versioning Convention

We follow the MAJOR.MINOR.PATCH versioning scheme as described by [SemVer.org](http://semver.org). Therefore, we recommend that you always pin (or vendor) the particular version you are working with to your code and never auto-update to the latest version. Especially when there is a MAJOR point release, since that is guaranteed to be a breaking change. Changes are documented in the [CHANGELOG](https://github.com/sendgrid/sendgrid-python/blob/master/CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-python/releases) section.
