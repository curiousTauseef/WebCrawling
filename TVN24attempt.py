# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from urllib2 import urlopen
import urllib2

url = 'http://www.tvn24.pl'

driver = webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

TVN24Urls = []

for div in soup.find_all('div'):
    try:
        if(div['class'][0]) in ['col_1', 'miniNews', 'topSiteSubjects', 'mainLeftColumn', 'col-2-1 ', 'col-2-2 ', 'art-info', 'articleCommentContainer fr', 'content']:
            for link in div.find_all('a'):
                if(link['href'].endswith('.html')):
                    TVN24Urls.append(link['href'])
    except KeyError:
        pass
    
TVN24Urls = list(set(TVN24Urls))

TVN24Urls = [x if x.startswith('http') else url + x for x in TVN24Urls]
    
#for link in TVN24Urls:
#    print link
    
#print 'Total number:', len(TVN24Urls)

driver.quit()

r = urllib2.urlopen(TVN24Urls[0]).read()
soup = BeautifulSoup(r, 'lxml')

print TVN24Urls[0]
print soup.prettify()
