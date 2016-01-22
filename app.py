import os
import datetime
import re

import github3
import requests
from bs4 import BeautifulSoup
import sendgrid
from db_connector import *

if os.path.exists('/Users/thinkingserious/Workspace/sendgrid-open-source-library-external-data/.env'):
    for line in open('/Users/thinkingserious/Workspace/sendgrid-open-source-library-external-data/.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

if (os.environ.get('ENV') != 'prod'):
    github_token = os.environ.get('GITHUB_TOKEN')
else:
    github_token = os.environ['GITHUB_TOKEN']

github = github3.login(token=github_token)
db = DBConnector()

def get_library_data(repo_name):
    sendgrid_library_data = github.repository("sendgrid", repo_name)
    lib_data = {}
    lib_data['num_pull_requests'] = sum(1 for i in sendgrid_library_data.iter_pulls())
    lib_data['num_issues'] = sum(1 for i in sendgrid_library_data.iter_issues())
    lib_data['num_commits'] = sum(1 for i in sendgrid_library_data.iter_commits())
    lib_data['num_branches'] = sum(1 for i in sendgrid_library_data.iter_branches())
    lib_data['num_releases'] = sum(1 for i in sendgrid_library_data.iter_releases())
    lib_data['num_contributors'] = sum(1 for i in sendgrid_library_data.iter_contributors())
    lib_data['num_watchers'] = sum(1 for i in sendgrid_library_data.iter_subscribers())
    lib_data['num_stargazers'] = sum(1 for i in sendgrid_library_data.iter_stargazers())
    lib_data['num_forks'] = sendgrid_library_data.forks_count
    githubdata = GitHubData(
                            date_updated=datetime.datetime.now(),
                            language=repo_name,
                            pull_requests=lib_data['num_pull_requests'],
                            open_issues=lib_data['num_issues'],
                            number_of_commits=lib_data['num_commits'],
                            number_of_branches=lib_data['num_branches'],
                            number_of_releases=lib_data['num_releases'],
                            number_of_contributors=lib_data['num_contributors'],
                            number_of_watchers=lib_data['num_watchers'],
                            number_of_stargazers=lib_data['num_stargazers'],
                            number_of_forks=lib_data['num_forks']
                            )
    db.add_data(githubdata)
    return
    
get_library_data("sendgrid-csharp")
get_library_data("smtpapi-csharp")
get_library_data("sendgrid-python")
get_library_data("smtpapi-python")
get_library_data("sendgrid-nodejs")
get_library_data("smtpapi-nodejs")
get_library_data("nodemailer-sendgrid-transport")
get_library_data("sendgrid-php")
get_library_data("smtpapi-php")
get_library_data("sendgrid-ruby")
get_library_data("smtpapi-ruby")
get_library_data("sendgrid-go")
get_library_data("smtpapi-go")
get_library_data("docs")

#### CSharp Downloads
url = "https://www.nuget.org/packages/SendGrid"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("p", { "class" : "stat-number" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_total_csharp_downloads = nodes[0].replace(',', '')
num_total_csharp_v_downloads = nodes[1].replace(',', '')

mydivs = soup.findAll("p", { "class" : "stat-label" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_v_downloads_label = nodes[1]

### Node.js Downloads
url = "https://www.npmjs.com/package/sendgrid"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("strong", { "class" : "pretty-number monthly-downloads" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_nodejs_monthly_downloads = nodes[0].replace(',', '')

### PHP Downloads
url = "https://packagist.org/packages/sendgrid/sendgrid"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("div", { "class" : "facts col-xs-12 col-sm-6 col-md-12" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_php_downloads = nodes[0][11:].replace(u'\u2009', '').split('\n')
num_php_downloads = str(num_php_downloads[0])

### Python Downloads
url = "https://pypi.python.org/pypi/sendgrid"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("ul", { "class" : "nodot" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_python_downloads = nodes[0].replace(u'\n', '').rpartition('week')[-1].rpartition('downloads')[0][2:].replace(u'\u2009', '')

### Ruby Downloads
url = "https://rubygems.org/gems/sendgrid-ruby"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("span", { "class" : "gem__downloads" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_ruby_downloads = nodes[0].replace(',', '')

### Java Downloads
url = "http://mvnrepository.com/artifact/com.sendgrid/sendgrid-java"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
mydivs = soup.findAll("a", { "class" : "im-usage" })
nodes = []
for node in mydivs:
   nodes.append(''.join(node.findAll(text=True)))
num_java_downloads = nodes[0].split(' ')[0]

packagedata = PackageManagerData(
                        date_updated=datetime.datetime.now(),
                        csharp_downloads=num_total_csharp_downloads,
                        nodejs_downloads=num_nodejs_monthly_downloads,
                        php_downloads=num_php_downloads,
                        python_downloads=num_python_downloads,
                        ruby_downloads=num_ruby_downloads
                        )
db.add_data(packagedata)

if (os.environ.get('ENV') != 'prod'):
    sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_API_KEY'))
else:
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_API_KEY'])

to_email = 'DX Team <dx@sendgrid.com>'
message = sendgrid.Mail()
message.add_to(to_email)
message.set_subject(str(datetime.date.today()) + ' - Package Manager Open Source Downloads and GitHub Data Updated [Automated]')
message.set_text('Data logged to DB on Heroku.')
message.set_html('Data logged to DB on Heroku.')
message.set_from('DX Team <dx@sendgrid.com>')
status, msg = sg.send(message)