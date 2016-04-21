# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2, pickle
import time, datetime

def wPolityceCrawl():
    print 'WPOLITYCE CRAWL'

    link = 'http://wpolityce.pl'
    
    """ Read the main wPolityce page """
    r = urllib2.urlopen(link).read()
    soup = BeautifulSoup(r, 'lxml')
    
    """ Load the timeline from file """
    try:
        wPolityce_Timeline = pickle.load(open('../wPolityce/wPolityce_Timeline.p', 'rb'))
    except IOError:
        print 'Loading empty wPolityce_Timeline'
        wPolityce_Timeline = {}
        
    wPolityce_Urls = []
    
    """ Get the links of the articles you haven't seen before """
    for article in soup.find_all('article'):
        newUrl = link + article.find('a')['href']
        if(newUrl not in wPolityce_Urls):
            wPolityce_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            wPolityce_Urls.append(link + article.find('a')['href'])
            
    """ Pickle the updated timeline """
    pickle.dump(wPolityce_Timeline, open("../wPolityce/wPolityce_Timeline.p", "wb"))
       
    """ Get text of each article and write to file """
    print 'Adding', len(wPolityce_Urls), 'articles'
    for url in wPolityce_Urls:
        r = urllib2.urlopen(url).read()
        soup = BeautifulSoup(r, 'lxml')
        print 'Link:', url
        
        title = soup.title.string
        
        f = open('../wPolityce/Articles/' + title + '.txt', 'w')
    
        f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
        
        body = soup.find('div', {'class':'article-body intext-ads'}).text
            
        f.write('BODY:' + body.encode('UTF8'))

        f.close()