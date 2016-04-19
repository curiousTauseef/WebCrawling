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

link = 'http://niezalezna.pl/'

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
response = opener.open(link)

soup = BeautifulSoup(response, 'lxml')

Niezalezna_Urls = []

for l in soup.find_all('a'):
    newUrl = l.get('href')
    if(newUrl.startswith(link) & (newUrl != link)):
        Niezalezna_Urls.append(l.get('href'))
    elif((newUrl.startswith('/')) & (is_number(newUrl[1:3]))):
        Niezalezna_Urls.append(link + newUrl[1:])
        
Niezalezna_Urls = list(set(Niezalezna_Urls))
        
#for link in Niezalezna_Urls:
#    print link
    
#print Niezalezna_Urls[0]
    
print 'http://niezalezna.pl/79263-gwizdy-na-lecha'

response = opener.open('http://niezalezna.pl/79263-gwizdy-na-lecha')

soup = BeautifulSoup(response, 'lxml')

#print soup.prettify()

title = soup.find(id = 'content').h1.text
print title

#bold = soup.find(id = 'content').strong.text
#print bold
#
#body = soup.find("div", {"class":"node-content"})
#print 'TEXT'
#print ''.join(soup.find("div", {"class":"node-content"}).findAll(text = True, recursive = False)).encode('UTF8')
