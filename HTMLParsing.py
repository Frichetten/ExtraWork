import urllib2
from bs4 import BeautifulSoup

page = urllib2.urlopen('https://illinoisstate.edu').read()
soup = BeautifulSoup(page, "html.parser")
#soup.prettify()
for anchor in soup.findAll('a', href=True):
    print anchor['href']
