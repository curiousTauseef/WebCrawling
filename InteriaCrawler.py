# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2, pickle
import time, datetime

def interiaCrawl():
    print 'INTERIA CRAWL'

    link = 'http://fakty.interia.pl'
    
    """ Read the main gazeta wiadomosci page """
    r = urllib2.urlopen(link).read()
    soup = BeautifulSoup(r, 'lxml')
    
    """ Load the timeline from file """
    try:
        Interia_Timeline = pickle.load(open('../Interia/Interia_Timeline.p', 'rb'))
    except IOError:
        print 'Loading empty Interia_Timeline'
        Interia_Timeline = {}
        
    Interia_Urls = []
        
    """ Get the links of the articles you haven't seen before """
    for l in soup.find_all('a'):
        if(',nId,' in l.get('href')):
            newUrl = l.get('href')
            if(newUrl not in Interia_Timeline):
                Interia_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                Interia_Urls.append(newUrl)
                
    """ Append fakty.interia.pl in front """
    Interia_Urls = [link + x for x in Interia_Urls]
            
    """ Pickle the updated timeline """
    pickle.dump(Interia_Timeline, open("../Interia/Interia_Timeline.p", "wb"))
       
    """ Get text of each article and write to file """
    print 'Adding', len(Interia_Urls), 'articles'
    for url in Interia_Urls:
        r = urllib2.urlopen(url).read()
        soup = BeautifulSoup(r, 'lxml')
        print 'Link:', url
        try:
            title = soup.find(id = 'articleSingle1').h1.text
        except AttributeError:
            print 'Ignoring article - doesnt have a proper title'
            continue
        
        f = open('../Interia/Articles/' + title + '.txt', 'w')
    
        f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
        
        bold = soup.find("div", {"class":"lead textContent fontSize-medium"}).p.text
        f.write('BOLD:' + removePunct(bold.encode('UTF8')) + '\n')
        
        body = ''
        try:
            paragraphs = soup.find('div', {'class':'text textContent fontSize-medium'}).find_all('p')
            for par in paragraphs:
                body += par.text
            
            f.write('BODY:' + body.encode('UTF8'))
        except AttributeError:
            print 'Article with no body'
            pass
        f.close()