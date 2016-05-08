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

    def scrape_urls(self):
        print 'Scraping', self.name
        for article in self.mainPage.find_all('article'):
            new_url = article.a.get('href')
            if new_url not in self.urlmap:
                self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.find(id='mainTitle').h1.text.strip()
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.bold = soup.find("meta", {"name": "description"})['content']
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting bold for link:' + self.currentLink)

        try:
            self.body = ''
            paragraphs = soup.find(id='detail').find_all('p')
            for par in paragraphs:
                self.body += par.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:' + self.currentLink)
