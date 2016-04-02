# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2
import time, datetime, string

link = 'http://wiadomosci.onet.pl'

""" Read the main gazeta wiadomosci page """
r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

Onet_Urls = []
for article in soup.find_all('article'):
    Onet_Urls.append(article.a.get('href'))
    
print Onet_Urls[8]

r = urllib2.urlopen(Onet_Urls[8]).read()
soup = BeautifulSoup(r, 'lxml')

title = soup.find(id = 'mainTitle').h1.text.strip()
print title

bold = soup.find("meta", {"name":"description"})['content']
#print bold

body = ''
paragraphs = soup.find(id = 'detail').find_all('p')
for par in paragraphs:
    body += par.text

#print body