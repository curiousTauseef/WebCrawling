# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2, pickle
import time, datetime

def onetCrawl():
    print 'ONET CRAWL'

    link = 'http://wiadomosci.onet.pl'
    
    """ Read the main gazeta wiadomosci page """
    r = urllib2.urlopen(link).read()
    soup = BeautifulSoup(r, 'lxml')
    
    """ Load the timeline from file """
    try:
        Onet_Timeline = pickle.load(open('../Onet/Onet_Timeline.p', 'rb'))
    except IOError:
        print 'Loading empty Onet_Timeline'
        Onet_Timeline = {}
        
    Onet_Urls = []
    
    """ Get the links of the articles you haven't seen before """
    for article in soup.find_all('article'):
        newUrl = article.a.get('href')
        if(newUrl not in Onet_Timeline):
            Onet_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            Onet_Urls.append(newUrl)
            
    """ Pickle the updated timeline """
    pickle.dump(Onet_Timeline, open("../Onet/Onet_Timeline.p", "wb"))
       
    """ Get text of each article and write to file """
    print 'Adding', len(Onet_Urls), 'articles'
    for url in Onet_Urls:
        r = urllib2.urlopen(url).read()
        soup = BeautifulSoup(r, 'lxml')
        print 'Link:', url
        title = soup.find(id = 'mainTitle').h1.text.strip()
        
        f = open('../Onet/Articles/' + title + '.txt', 'w')
    
        f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
        
        bold = soup.find("meta", {"name":"description"})['content']
        f.write('BOLD:' + removePunct(bold.encode('UTF8')) + '\n')
        
        body = ''
        try:
            paragraphs = soup.find(id = 'detail').find_all('p')
            for par in paragraphs:
                body += par.text
            
            f.write('BODY:' + body.encode('UTF8'))
        except AttributeError:
            print 'Article with no body'
            pass
        f.close()