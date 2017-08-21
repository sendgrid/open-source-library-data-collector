import requests
import datetime
import re
from bs4 import BeautifulSoup

r = requests.get('https://www.nuget.org/packages/SendGrid')
soup = BeautifulSoup(r.text, "html.parser")
pattern = re.compile(r'total downloads')
lines = soup.find(text=pattern).__dict__['parent']
num_total_csharp_downloads = str(lines)[:-39]
num_total_csharp_downloads = num_total_csharp_downloads[-9:]
num_total_csharp_downloads = num_total_csharp_downloads.replace(',', '')
print(num_total_csharp_downloads)

