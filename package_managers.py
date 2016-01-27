import requests
from bs4 import BeautifulSoup
from db_connector import *

class PackageManagers(object):
    def __init__(self):
        self.db = DBConnector()
        
    def update_package_manager_data(self, package_manager_urls):
        num_total_csharp_downloads = None
        num_nodejs_monthly_downloads = None
        num_php_downloads = None
        num_python_downloads = None
        num_ruby_downloads = None
        for url in package_manager_urls:
            if 'nuget' in url: 
                num_total_csharp_downloads = self.csharp_downloads(url)
            if 'npmjs' in url:
                num_nodejs_monthly_downloads = self.nodejs_downloads(url)
            if 'packagist' in url:
                num_php_downloads = self.php_downloads(url)
            if 'pypi' in url:
                num_python_downloads = self.python_downloads(url)
            if 'rubygems' in url:
                num_ruby_downloads = self.ruby_downloads(url)

        self.update_db(num_total_csharp_downloads,
                  num_nodejs_monthly_downloads,
                  num_php_downloads,
                  num_python_downloads,
                  num_ruby_downloads)
    
    def csharp_downloads(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("p", { "class" : "stat-number" })
        nodes = []
        for node in mydivs:
           nodes.append(''.join(node.findAll(text=True)))
        num_total_csharp_downloads = nodes[0].replace(',', '')
        return num_total_csharp_downloads
        
    def nodejs_downloads(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("strong", { "class" : "pretty-number monthly-downloads" })
        nodes = []
        for node in mydivs:
           nodes.append(''.join(node.findAll(text=True)))
        num_nodejs_monthly_downloads = nodes[0].replace(',', '')
        return num_nodejs_monthly_downloads
        
    def php_downloads(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("div", { "class" : "facts col-xs-12 col-sm-6 col-md-12" })
        nodes = []
        for node in mydivs:
           nodes.append(''.join(node.findAll(text=True)))
        num_php_downloads = nodes[0][11:].replace(u'\u2009', '').split('\n')
        num_php_downloads = str(num_php_downloads[0])
        return num_php_downloads
        
    def python_downloads(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("ul", { "class" : "nodot" })
        nodes = []
        for node in mydivs:
           nodes.append(''.join(node.findAll(text=True)))
        num_python_downloads = nodes[0].replace(u'\n', '').rpartition('week')[-1].rpartition('downloads')[0][2:].replace(u'\u2009', '')
        return num_python_downloads
        
    def ruby_downloads(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        mydivs = soup.findAll("span", { "class" : "gem__downloads" })
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
            num_ruby_downloads
            ):
        packagedata = PackageManagerData(
                                date_updated=datetime.datetime.now(),
                                csharp_downloads=num_total_csharp_downloads,
                                nodejs_downloads=num_nodejs_monthly_downloads,
                                php_downloads=num_php_downloads,
                                python_downloads=num_python_downloads,
                                ruby_downloads=num_ruby_downloads
                                )
        self.db.add_data(packagedata)