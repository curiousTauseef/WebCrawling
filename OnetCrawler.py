# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from Crawler import Crawler
from Logger import Logger

class OnetCrawler(Crawler):

    def __init__(self):
        Crawler.__init__(self, 'http://wiadomosci.onet.pl', 'Onet')
        
    def scrapeUrls(self):
        print 'Scraping', self.name
        for article in self.mainPage.find_all('article'):
            newUrl = article.a.get('href')
            if(newUrl not in self.timeline):
                self.urls.append(newUrl)
        
    def scrapeText(self, link):
        
        soup = self.readPage(link)
        
#################################### TITLE ####################################
        self.title = soup.find(id = 'mainTitle').h1.text.strip()
        
#################################### BOLD #####################################
        self.bold = soup.find("meta", {"name":"description"})['content']
        
#################################### BODY #####################################
        self.body = ''
        try:
            paragraphs = soup.find(id = 'detail').find_all('p')
            for par in paragraphs:
                self.body += par.text
        except AttributeError:
            self.logger.log(Logger.WARN, 'Article with no body')