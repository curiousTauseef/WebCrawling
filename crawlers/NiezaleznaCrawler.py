# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

import urllib2

from bs4 import BeautifulSoup

from crawlers.Crawler import Crawler
from utils.Logger import Logger


class NiezaleznaCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://niezalezna.pl/', 'Niezalezna')
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-agent', 'Mozilla/46.0')]

    def load_main_page(self):
        self.mainPage = self.read_page(self.baseLink)

    def scrape_urls(self):
        print 'Scraping', self.name
        for l in self.mainPage.find_all('a'):
            new_url = l.get('href')
            if new_url.startswith(self.baseLink) and (new_url != self.baseLink):
                if new_url not in self.urlmap.values():
                    self.urls.append(new_url)
            elif(new_url.startswith('/')) & (self.is_number(new_url[1:3])):
                new_url = self.baseLink + new_url[1:]
                if new_url not in self.urlmap.values():
                    self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.find(id='content').h1.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.bold = soup.find(id='content').strong.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting bold for link:' + self.currentLink)

        try:
            """ Text is added 'luzem' inside the div """
            self.body = ''.join(soup.find("div", {"class": "node-content"}).findAll(text=True, recursive=False)) + ' '
            """ Except for occasionally bolded text - that needs to be added separately """
            for bolded_text in soup.find("div", {"class": "node-content"}).findAll('strong'):
                self.body += bolded_text.text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:' + self.currentLink)

    def read_page(self, link):
        return BeautifulSoup(self.opener.open(link), 'lxml')

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
