# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

from bs4 import BeautifulSoup
import urllib2

link = 'http://wpolityce.pl'

r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

wPolityce_Urls = []

for article in soup.find_all('article'):
    wPolityce_Urls.append(link + article.find('a')['href'])
    
print wPolityce_Urls[0]

r = urllib2.urlopen(wPolityce_Urls[0]).read()
soup = BeautifulSoup(r, 'lxml')

title = soup.title.string

print title

body = soup.find('div', {'class':'article-body intext-ads'}).text

print body