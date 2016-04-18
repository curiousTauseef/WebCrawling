# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup
import urllib2

link = 'http://wyborcza.pl'

r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

Wyborcza_Urls = []

""" MT1 """
a_tags = soup.find_all(id = "LinkArea:MT1")
for link in a_tags:
    Wyborcza_Urls.append(link['href'])
    
""" MT2 """
a_tags = soup.find_all(id = "LinkArea:MT2")
for link in a_tags:
    Wyborcza_Urls.append(link['href'])
    
""" Wydarzenia """
a_tags = soup.find_all(id = "LinkArea:Wydarzenia")
for link in a_tags:
    if(link['title'] != 'Wydarzenia'):
        Wyborcza_Urls.append(link['href'])
        
""" Najnowsze """
a_tags = soup.find_all(id = "LinkArea:najnowsze")
for link in a_tags:
    try:
        if(link['title'] != 'Najnowsze'):
            Wyborcza_Urls.append(link['href'])
    except KeyError:
        pass
    
""" Remove duplicates """
Wyborcza_Urls = list(set(Wyborcza_Urls))

""" Only keep those ending in .html """
Wyborcza_Urls = [x for x in Wyborcza_Urls if x.endswith('html')]

#for url in Wyborcza_Urls:
#    print url
#print 'Number of links:', len(Wyborcza_Urls)

print 'Working with', Wyborcza_Urls[0]

r = urllib2.urlopen(Wyborcza_Urls[0]).read()
soup = BeautifulSoup(r, 'lxml')

title = soup.find(id = 'holder_101').h1.text

print title

body = soup.find('meta', {'property':'og:description'})['content'].strip()

print body