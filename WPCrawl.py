# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:20:48 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2
import time, datetime, string, pickle

def wpCrawl():
    print 'WP CRAWL'
    link = 'http://wiadomosci.wp.pl'
    
    """ Read the main wp wiadomosci page """
    r = urllib2.urlopen(link).read()
    soup = BeautifulSoup(r, 'lxml')
    
    """ Load the timeline from file """
    try:
        WP_Timeline = pickle.load(open('../WP/WP_Timeline.p', 'rb'))
    except IOError:
        print 'Loading empty WP_Timeline'
        WP_Timeline = {}
        
    WP_Urls = []
    
    """ Get the links of the articles you haven't seen before """
    
    """ Najnowsze wiadomosci """
    #print 'NAJNOWSZE WIADOMOSCI'
    outerDiv = soup.find(id = 'bxNajnowszeWiad')
    for innerDiv in outerDiv.find_all('div'):
        try:
            newUrl = innerDiv.find('a', {'class' : 'lnk_nw'})['href']
            if(newUrl not in WP_Timeline):
                WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
        
    """ Najwazniejsze wiadomosci """
    #print 'NAJWAZNIEJSZE WIADOMOSCI'
    outerDiv = soup.find(id = 'bxNajwazniejszeWiad')
    contentDiv = outerDiv.find('div', {'class' : 'content'})
    for linkDiv in contentDiv.find_all('a'):
        try:
            newUrl = linkDiv['href']
            if(newUrl not in WP_Timeline):
                WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
        
    """ Trzy newsy """
    #print 'TRZY NEWSY'
    outerDiv = soup.find(id = 'bxTrzyNewsy')
    for linkDiv in outerDiv.find_all('a'):
        try:
            newUrl = linkDiv['href']
            if(newUrl not in WP_Timeline):
                WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Wiadomosci Polska """
    #print 'WIADOMOSCI POLSKA'
    outerDiv = soup.find(id = 'bxWiadPolska')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Wiadomosci lokalne """
    #print 'WIADOMOSCI LOKALNE'
    outerDiv = soup.find(id = 'bxWiadLokalne')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Wiadomosci swiat """
    #print 'WIADOMOSCI SWIAT'
    outerDiv = soup.find(id = 'bxWiadSwiat')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Tylko w WP """
    #print 'TYLKO W WP'
    outerDiv = soup.find(id = 'bxTylkowWP')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Ciekawostki """
    #print 'CIEKAWOSTKI'
    outerDiv = soup.find(id = 'bxCiekawostki')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Nauka """
    #print 'NAUKA'
    outerDiv = soup.find(id = 'bxNauka')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    #print 'Number of URLs:', len(WP_Urls)
    
    """ Przestepczosc """
    #print 'PRZESTEPCZOSC'
    outerDiv = soup.find(id = 'bxPrzestepczosc')
    for linkDiv in outerDiv.find_all('a'):
        try:
            if(linkDiv['href'].endswith('wiadomosc.html')):
                newUrl = linkDiv['href']
                if(newUrl not in WP_Timeline):
                    WP_Timeline[newUrl] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    WP_Urls.append(newUrl)
        except TypeError:
            pass
    WP_Urls = list(set(WP_Urls))
    
    """ Append wiadomosci.wp.pl in front """
    WP_Urls = [link + x for x in WP_Urls]
            
    """ Pickle the updated timeline """
    pickle.dump(WP_Timeline, open("../WP/WP_Timeline.p", "wb")) 
       
    """ Get text of each article and write to file """
    print 'Adding', len(WP_Urls), 'articles'
    for url in WP_Urls:
        r = urllib2.urlopen(url).read()
        soup = BeautifulSoup(r, 'lxml')
        print 'Link:', url
        
        title = soup.find('header', {'class' : 'narrow'}).find('div', {'class' : 'h1'}).text
        f = open('../WP/Articles/' + title + '.txt', 'w')
    
        f.write('TITLE:' + removePunct(title.encode('UTF8')) + '\n')
        
        try:
            bold = soup.find("main", {"class":"ST-Artykul"}).find('div', {'class' : 'lead'}).text.strip()
            f.write('BOLD:' + removePunct(bold.encode('UTF8')) + '\n')
        except AttributeError:
            pass
        
        body = soup.find(id = 'intertext1').text.rstrip()
        f.write('BODY:' + body.encode('UTF8'))
        f.close()