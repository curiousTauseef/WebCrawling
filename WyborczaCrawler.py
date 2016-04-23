# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2, pickle
import time, datetime

def wyborczaCrawl():
    print 'WYBORCZA CRAWL'

    link = 'http://wyborcza.pl'
    
    """ Read the main wyborcza page """
    r = urllib2.urlopen(link).read()
    soup = BeautifulSoup(r, 'lxml')
    
    """ Load the timeline from file """
    try:
        Wyborcza_Timeline = pickle.load(open('../Wyborcza/Wyborcza_Timeline.p', 'rb'))
    except IOError:
        print 'Loading empty Wyborcza_Timeline'
        Wyborcza_Timeline = {}
        
    Wyborcza_Urls = []
        
    """ Get the links of the articles you haven't seen before """
    
    """ MT1 """
    a_tags = soup.find_all(id = "LinkArea:MT1")
    for link in a_tags:
        newUrl = link['href']
        if(newUrl not in Wyborcza_Timeline):
            Wyborcza_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            Wyborcza_Urls.append(newUrl)
        
    """ MT2 """
    a_tags = soup.find_all(id = "LinkArea:MT2")
    for link in a_tags:
        newUrl = link['href']
        if(newUrl not in Wyborcza_Timeline):
            Wyborcza_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            Wyborcza_Urls.append(newUrl)
            
    """ Wydarzenia """
    a_tags = soup.find_all(id = "LinkArea:Wydarzenia")
    for link in a_tags:
        if(link['title'] != 'Wydarzenia'):
            newUrl = link['href']
            if(newUrl not in Wyborcza_Timeline):
                Wyborcza_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                Wyborcza_Urls.append(newUrl)
            
    """ Najnowsze """
    a_tags = soup.find_all(id = "LinkArea:najnowsze")
    for link in a_tags:
        try:
            if(link['title'] != 'Najnowsze'):
                newUrl = link['href']
                if(newUrl not in Wyborcza_Timeline):
                    Wyborcza_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    Wyborcza_Urls.append(newUrl)        
        except KeyError:
            pass
        
    """ Remove duplicates """
    Wyborcza_Urls = list(set(Wyborcza_Urls))
    
    """ Only keep those ending in .html """
    Wyborcza_Urls = [x for x in Wyborcza_Urls if x.endswith('html')]
            
    """ Pickle the updated timeline """
    pickle.dump(Wyborcza_Timeline, open("../Wyborcza/Wyborcza_Timeline.p", "wb"))
       
    """ Get text of each article and write to file """
    print 'Adding', len(Wyborcza_Urls), 'articles'
    for url in Wyborcza_Urls:
        r = urllib2.urlopen(url).read()
        soup = BeautifulSoup(r, 'lxml')
        print 'Link:', url
        try:
            title = soup.html.head.title.string
        except AttributeError:
            print 'Ignoring article - doesnt have a proper title'
            continue
        
        f = open('../Wyborcza/Articles/' + title + '.txt', 'w')
    
        f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
        
        body = soup.find('meta', {'property':'og:description'})['content'].strip()

        try:
            f.write('BODY:' + body.encode('UTF8'))
        except AttributeError:
            print 'Article with no body'
            pass
        f.close()