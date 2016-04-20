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

link = 'http://wpolityce.pl/'

r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

for article in soup.find_all('article'):
    print article.find('a')['href']