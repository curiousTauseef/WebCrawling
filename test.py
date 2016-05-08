# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

import urllib2
from bs4 import BeautifulSoup

link = 'http://niezalezna.pl/80115-smierc-biegacza-podczas-zawodow'
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
soup = BeautifulSoup(opener.open(link), 'lxml')
# r = urllib2.urlopen(link).read()
# soup = BeautifulSoup(r, 'lxml')

# print soup.prettify()
print soup.find(id='content').h1.text
