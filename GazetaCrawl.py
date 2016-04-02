# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2
import time, datetime, string

link = 'http://wiadomosci.gazeta.pl/wiadomosci/0,0.html'

""" Read the main gazeta wiadomosci page """
r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

""" Find the sections where all the links are """
section = soup.find(id = 'holder_201')

""" Get the links of all the actual articles """
Gazeta_Timeline = {}
Gazeta_Urls = []
for link in section.find_all('a'):
    newUrl = link.get('href')
    if(newUrl.startswith('http://wiadomosci.gazeta.pl/wiadomosci/') and (newUrl.endswith('.html')) and (newUrl not in Gazeta_Timeline)):
        Gazeta_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        Gazeta_Urls.append(newUrl)
        
r = urllib2.urlopen(Gazeta_Urls[2]).read()
soup = BeautifulSoup(r, 'lxml')
print 'Working with link', Gazeta_Urls[2]

f = open('../Output.txt', 'w')
title = soup.title.string
f.write(removePunct(title.encode('UTF8')) + '\n')
print 'Title written to file'

bold = soup.find(id = 'gazeta_article_lead').get_text()
f.write(removePunct(bold.encode('UTF8')) + '\n')
print 'Bold paragraph written to file'

body = soup.find(id = 'artykul')

for item in body.findAll(text = True, recursive = False):
    """ Ignore comments and empty strings """
    if((not isinstance(item, Comment)) or (not item)):
        out = removePunct(item.encode('UTF8'))
        f.write(out)
print 'Article body written to file'
f.close()