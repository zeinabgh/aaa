import urllib.request
from bs4 import BeautifulSoup

z='http://stackoverflow.com/questions/34475051/need-to-install-urllib2-for-python-3-5-1'
page=urllib.request.urlopen(z)
soup=BeautifulSoup(page)

for i in soup.find_all('a'):
    print(i)
