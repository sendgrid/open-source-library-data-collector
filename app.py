import os
import datetime
import re

import github3
import requests
from bs4 import BeautifulSoup
import sendgrid

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
    return lib_data
    
csharp_data = get_library_data("sendgrid-csharp")
csharp_smtpapi_data = get_library_data("smtpapi-csharp")
python_data = get_library_data("sendgrid-python")
python_smtpapi_data = get_library_data("smtpapi-python")
nodejs_data = get_library_data("sendgrid-nodejs")
nodejs_smtpapi_data = get_library_data("smtpapi-nodejs")
nodejs_mailer_data = get_library_data("nodemailer-sendgrid-transport")
php_data = get_library_data("sendgrid-php")
php_smtpapi_data = get_library_data("smtpapi-php")
ruby_data = get_library_data("sendgrid-ruby")
ruby_smtpapi_data = get_library_data("smtpapi-ruby")
go_data = get_library_data("sendgrid-go")
go_smtpapi_data = get_library_data("smtpapi-go")
docs_data = get_library_data("docs")

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

lib_header = "Date Updated, " + \
      "Language, " + \
      "Pull Requests, " + \
      "Open Issues, " + \
      "Number of Commits, " + \
      "Number of Branches, " + \
      "Number of Releases, " + \
      "Number of Contributors, " + \
      "Number of Watchers, " + \
      "Number of Stargazers, " + \
      "Number of Forks"

def get_lib_data(repo_name, lib_data):
    return str(datetime.date.today()) + \
      ", " + str(repo_name) + \
      ", " + str(lib_data['num_pull_requests']) + \
      ", " + str(lib_data['num_issues'] - lib_data['num_pull_requests']) + \
      ", " + str(lib_data['num_commits']) + \
      ", " + str(lib_data['num_branches']) + \
      ", " + str(lib_data['num_releases']) + \
      ", " + str(lib_data['num_contributors']) + \
      ", " + str(lib_data['num_watchers'] + 1) + \
      ", " + str(lib_data['num_stargazers']) + \
      ", " + str(lib_data['num_forks'])

package_header = "Date Updated, " + \
      "Total CSharp Downloads - Nuget, " + \
      num_v_downloads_label[13:] + " CSharp Downloads - Nuget, " + \
      "Total Node.js Monthly Downloads, " + \
      "Total PHP Monthly Downloads, " + \
      "Total Python Monthly Downloads, " + \
      "Total Ruby Downloads" + \
      "Totoal daily Java Downloads"

def get_package_data():
    return str(datetime.date.today()) + \
    ", " + str(num_total_csharp_downloads) + \
    ", " + str(num_total_csharp_v_downloads) + \
    ", " + str(num_nodejs_monthly_downloads) + \
    ", " + str(num_php_downloads) + \
    ", " + str(num_python_downloads) + \
    ", " + str(num_ruby_downloads) + \
    ", " + str(num_java_downloads)

package_data = package_header + "\n"
package_data += get_package_data()

lib_data = lib_header + "\n"
lib_data += get_lib_data("CSharp", csharp_data) + "\n"
lib_data += get_lib_data("CSharp SMTPAPI", csharp_smtpapi_data) + "\n"
lib_data += get_lib_data("Python", python_data) + "\n"
lib_data += get_lib_data("Python SMTPAPI", python_smtpapi_data) + "\n"
lib_data += get_lib_data("Nodejs", nodejs_data) + "\n"
lib_data += get_lib_data("Nodejs SMTPAPI", nodejs_smtpapi_data) + "\n"
lib_data += get_lib_data("Nodemailer SendGrid Transport", nodejs_mailer_data) + "\n"
lib_data += get_lib_data("PHP", php_data) + "\n"
lib_data += get_lib_data("PHP SMTPAPI", php_smtpapi_data) + "\n"
lib_data += get_lib_data("Ruby", ruby_data) + "\n"
lib_data += get_lib_data("Ruby SMTPAPI", ruby_smtpapi_data) + "\n"
lib_data += get_lib_data("Go", go_data) + "\n"
lib_data += get_lib_data("Go SMTPAPI", go_smtpapi_data) + "\n"
lib_data += get_lib_data("Documentation", docs_data)

if (os.environ.get('ENV') != 'prod'):
    sg = sendgrid.SendGridClient(os.environ.get('SENDGRID_API_KEY'))
else:
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_API_KEY'])

message = sendgrid.Mail()
message.add_to('DX Team <dx@sendgrid.com>')
message.set_subject(str(datetime.date.today()) + ' - Package Manager Open Source Download Data [Automated]')
message.set_text('Please see the attached .csv file.')
message.set_html('Please see the attached .csv file.')
message.add_attachment_stream(str(datetime.date.today()) + '_sendgrid_package_data.csv', package_data)
message.set_from('DX Team <dx@sendgrid.com>')
status, msg = sg.send(message)

message2 = sendgrid.Mail()
message2.add_to('DX Team <dx@sendgrid.com>')
message2.set_subject(str(datetime.date.today()) + ' - GitHub Open Source Data [Automated]')
message2.set_text('Please see the attached .csv file.')
message2.set_html('Please see the attached .csv file.')
message2.add_attachment_stream(str(datetime.date.today()) + '_sendgrid_github_data.csv', lib_data)
message2.set_from('DX Team <dx@sendgrid.com>')
status, msg = sg.send(message2)