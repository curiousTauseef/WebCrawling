# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

import urllib2
from bs4 import BeautifulSoup, Comment

link = 'http://wiadomosci.gazeta.pl/wiadomosci/7,114871,20044722,rzeczniczka-pis-do-piatku-spotkanie-liderow-partyjnych-zbiegnie.html'
# opener = urllib2.build_opener()
# opener.addheaders = [('User-agent', 'Mozilla/5.0')]
# soup = BeautifulSoup(opener.open(link), 'lxml')
r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

# print soup.prettify()
# print soup.find(id='content').h1.text

body = ''
id_article = soup.find(id='article_body')
for item in id_article.findAll(text=True, recursive=True):
    """ Ignore comments and empty strings """
    if (not isinstance(item, Comment)) or (not item):
        body += item

print body
