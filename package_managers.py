import requests
import datetime
from bs4 import BeautifulSoup
from db_connector import DBConnector, PackageManagerData
import sys
if (3, 1) < sys.version_info < (3, 6):
    def u(x):
        return x
else:
    import codecs

    def u(x):
        return codecs.unicode_escape_decode(x)[0]


class PackageManagers(object):
    """Collect time stamped package manager data from various package managers
       and store in a DB"""
    def __init__(self):
        self.db = DBConnector()

    def update_package_manager_data(self, package_manager_urls):
        """Gets data given package manager urls and adds it to the DB

        :param package_manager_urls: URL(s) to the package you want to obtain
                                     download data from
        :type package_manager_urls:  Array of strings

        :returns: Returns the data object that was added to the DB
        :rtype:   Data object
        """
        num_total_csharp_downloads = None
        num_nodejs_monthly_downloads = None
        num_php_downloads = None
        num_python_downloads = None
        num_ruby_downloads = None
        num_python_http_client_downloads = None
        num_python_open_source_library_data_collector_downloads = None
        num_ruby_http_client_downloads = None
        num_csharp_http_client_downloads = None
        num_php_http_client_downloads = None
        for url in package_manager_urls:
            if 'https://www.nuget.org/packages/SendGrid' == url:
                num_total_csharp_downloads = self.csharp_downloads(url)
            if 'https://www.nuget.org/packages/SendGrid.CSharp.HTTP.Client' == url:
                num_csharp_http_client_downloads = self.csharp_downloads(url)
            if 'npmjs' in url:
                num_nodejs_monthly_downloads = self.nodejs_downloads(url)
            if 'https://packagist.org/packages/sendgrid/sendgrid' == url:
                num_php_downloads = self.php_downloads(url)
            if 'https://packagist.org/packages/sendgrid/php-http-client' == url:
                num_php_http_client_downloads = self.php_downloads(url)
            if 'pypi' in url and 'sendgrid' in url:
                num_python_downloads = self.python_downloads(url)
            if 'pypi' in url and 'python_http_client' in url:
                num_python_http_client_downloads = self.python_downloads(url)
            if 'pypi' in url and 'open_source_library_data_collector' in url:
                num_python_open_source_library_data_collector_downloads = self.python_downloads(url)
            if 'rubygems' in url and 'sendgrid' in url:
                num_ruby_downloads = self.ruby_downloads(url)
            if 'rubygems' in url and 'http' in url:
                num_ruby_http_client_downloads = self.ruby_downloads(url)

        return self.update_db(num_total_csharp_downloads,
                              num_nodejs_monthly_downloads,
                              num_php_downloads,
                              num_python_downloads,
                              num_ruby_downloads,
                              num_python_http_client_downloads,
                              num_python_open_source_library_data_collector_downloads,
                              num_ruby_http_client_downloads,
                              num_csharp_http_client_downloads,
                              num_php_http_client_downloads)

    def csharp_downloads(self, url):
        """Gets library download data from nuget.org

        :param url: the URL of the package
        :type url:  string

        :returns: The number of total library downloads
        :rtype:   Integer
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("p", {"class": "stat-number"})
        nodes = []
        for node in mydivs:
            nodes.append(''.join(node.findAll(text=True)))
        num_total_csharp_downloads = nodes[0].replace(',', '')
        return num_total_csharp_downloads

    def nodejs_downloads(self, url):
        """Gets library download data from npmjs.org

        :param url: the URL of the package
        :type url:  string

        :returns: The number of library downloads in the last month
        :rtype:   Integer
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("strong",
                              {"class": "pretty-number monthly-downloads"})
        nodes = []
        for node in mydivs:
            nodes.append(''.join(node.findAll(text=True)))
        num_nodejs_monthly_downloads = nodes[0].replace(',', '')
        return num_nodejs_monthly_downloads

    def php_downloads(self, url):
        """Gets library download data from packagist.org

        :param url: the URL of the package
        :type url:  string

        :returns: The number of total library downloads
        :rtype:   Integer
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("div",
                              {"class": "facts col-xs-12 col-sm-6 col-md-12"})
        nodes = []
        for node in mydivs:
            nodes.append(''.join(node.findAll(text=True)))
        num_php_downloads = nodes[0][11:].replace(u('\u2009'), '').split('\n')
        num_php_downloads = str(num_php_downloads[0])
        return num_php_downloads

    def python_downloads(self, url):
        """Gets library download data from pypi.python.org

        :param url: the URL of the package
        :type url:  string

        :returns: The number of library downloads in the last month
        :rtype:   Integer
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("ul", {"class": "nodot"})
        nodes = []
        for node in mydivs:
            nodes.append(''.join(node.findAll(text=True)))
        num_python_downloads = \
            nodes[0].replace(u('\n'), '') \
            .rpartition('week')[-1] \
            .rpartition('downloads')[0][2:] \
            .replace(u('\u2009'), '')
        return num_python_downloads

    def ruby_downloads(self, url):
        """Gets library download data from rubygems.org

        :param url: the URL of the package
        :type url:  string

        :returns: The number of total library downloads
        :rtype:   Integer
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("span", {"class": "gem__downloads"})
        nodes = []
        for node in mydivs:
            nodes.append(''.join(node.findAll(text=True)))
        num_ruby_downloads = nodes[0].replace(',', '')
        return num_ruby_downloads

    def update_db(
            self,
            num_total_csharp_downloads,
            num_nodejs_monthly_downloads,
            num_php_downloads,
            num_python_downloads,
            num_ruby_downloads,
            num_python_http_client_downloads,
            num_python_open_source_library_data_collector_downloads,
            num_ruby_http_client_downloads,
            num_csharp_http_client_downloads,
            num_php_http_client_downloads
            ):
        """Update the DB with the package manager data

        :param num_total_csharp_downloads:   # of total downloads
        :param num_nodejs_monthly_downloads: # of downloads in the last month
        :param num_php_downloads:            # of total downloads
        :param num_python_downloads:         # of downloads in the last month
        :param num_ruby_downloads:           # of total downloads
        :type  num_total_csharp_downloads:   Integer
        :type  num_nodejs_monthly_downloads: Integer
        :type  num_php_downloads:            Integer
        :type  num_python_downloads:         Integer
        :type  num_ruby_downloads:           Integer

        :returns: Returns the data object that was added to the DB
        :rtype:   Data object
        """
        packagedata = PackageManagerData(
            date_updated=datetime.datetime.now(),
            csharp_downloads=num_total_csharp_downloads,
            nodejs_downloads=num_nodejs_monthly_downloads,
            php_downloads=num_php_downloads,
            python_downloads=num_python_downloads,
            ruby_downloads=num_ruby_downloads,
            python_http_client_downloads=num_python_http_client_downloads,
            csharp_http_client_downloads=num_csharp_http_client_downloads,
            ruby_http_client_downloads=num_ruby_http_client_downloads,
            php_http_client_downloads=num_php_http_client_downloads,
            open_source_library_data_collector_downloads=num_python_open_source_library_data_collector_downloads
            )
        return self.db.add_data(packagedata)
