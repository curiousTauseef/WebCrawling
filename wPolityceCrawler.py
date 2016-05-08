# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""


from Crawler import Crawler
from Logger import Logger

class wPolityceCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://wpolityce.pl', 'wPolityce')

    def scrape_urls(self):
        print 'Scraping', self.name
        for article in self.mainPage.find_all('article'):
            new_url = article.find('a')['href']
            if not new_url.startswith('http'):
                new_url = self.baseLink + article.find('a')['href']
            if new_url not in self.urlmap.values():
                self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.title.string
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.body = soup.find('div', {'class': 'article-body intext-ads'}).text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:' + self.currentLink)
