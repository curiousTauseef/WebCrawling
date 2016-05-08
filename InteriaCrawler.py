# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup
from Crawler import Crawler
from Logger import Logger
import urllib2, pickle
import time, datetime


class InteriaCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://fakty.interia.pl', 'Interia')

    def scrape_urls(self):
        print 'Scraping', self.name
        for article in self.mainPage.find_all('a'):
            if ',nId,' in article.get('href'):
                new_url = article.get('href')
                if not new_url.startswith(self.baseLink) and not new_url.startswith('http'):
                    new_url = self.baseLink + new_url
                    if new_url not in self.urlmap:
                        self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.find(id='articleSingle1').h1.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.bold = soup.find("div", {"class": "lead textContent fontSize-medium"}).p.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting bold for link:' + self.currentLink)

        try:
            paragraphs = soup.find('div', {'class':'text textContent fontSize-medium'}).find_all('p')
            for par in paragraphs:
                self.body += par.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:', self.currentLink)
