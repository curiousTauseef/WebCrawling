# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:29:22 2016

@author: piotrgrudzien
"""

from bs4 import Comment

from crawlers.Crawler import Crawler
from utils.Logger import Logger


class GazetaCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://wiadomosci.gazeta.pl/wiadomosci/0,0.html', 'Gazeta')

    def scrape_urls(self):
        print 'Scraping', self.name
        section = self.mainPage.find(id='holder_201')
        for link in section.find_all('a'):
            new_url = link.get('href')
            if (new_url.startswith('http://wiadomosci.gazeta.pl/wiadomosci/') and (new_url.endswith('.html')) and (
                    new_url not in self.urlmap.values()) and ('-' in new_url)):
                self.urls.append(new_url)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.title.string
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.bold = soup.find(id='gazeta_article_lead').get_text()
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting bold for link:' + self.currentLink)

        try:
            if soup.find(id='artykul') is not None:
                id_article = soup.find(id='artykul')
                rec = False
            elif soup.find(id='article_body') is not None:
                id_article = soup.find(id='article_body')
                rec = True
                self.logger.log(Logger.WARN, 'Using id=article_body')
            else:
                self.logger.log(Logger.ERROR, 'Nor id=artykul nor id=article_body found')
                return
            for item in id_article.findAll(text=True, recursive=rec):
                """ Ignore comments and empty strings """
                if(not isinstance(item, Comment)) or (not item):
                    self.body += item
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:' + self.currentLink)
