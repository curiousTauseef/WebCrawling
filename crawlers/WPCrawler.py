# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:20:48 2016

@author: piotrgrudzien
"""

from crawlers.Crawler import Crawler
from utils.Logger import Logger


class WPCrawler(Crawler):
    def __init__(self):
        Crawler.__init__(self, 'http://wiadomosci.wp.pl', 'WP')
        self.sections = ['bxNajnowszeWiad', 'bxNajwazniejszeWiad', 'bxTrzyNewsy', 'bxWiadPolska', 'bxWiadLokalne',
                'bxWiadSwiat', 'bxTylkowWP']

    def custom_scrape(self, section_id):
        outer_div = self.mainPage.find(id=section_id)

        if section_id is 'bxNajnowszeWiad':
            for innerDiv in outer_div.find_all('div'):
                try:
                    new_url = self.baseLink + innerDiv.find('a', {'class': 'lnk_nw'})['href']
                    if new_url not in self.urlmap.values():
                        self.urls.append(new_url)
                except TypeError:
                    pass

        elif section_id is 'bxNajwazniejszeWiad':
            content_div = outer_div.find('div', {'class': 'content'})
            for link_div in content_div.find_all('a'):
                try:
                    new_url = self.baseLink + link_div['href']
                    if new_url not in self.urlmap.values():
                        self.urls.append(new_url)
                except TypeError:
                    pass

        elif section_id is 'bxTrzyNewsy':
            for link_div in outer_div.find_all('a'):
                    try:
                        new_url = self.baseLink + link_div['href']
                        if new_url not in self.urlmap.values():
                            self.urls.append(new_url)
                    except TypeError:
                        pass

        elif section_id is 'bxWiadPolska':
            for link_div in outer_div.find_all('a'):
                    try:
                        if link_div['href'].endswith('wiadomosc.html'):
                            new_url = self.baseLink + link_div['href']
                            if new_url not in self.urlmap.values():
                                self.urls.append(new_url)
                    except TypeError:
                        pass

        elif section_id is 'bxWiadLokalne':
            for link_div in outer_div.find_all('a'):
                    try:
                        if link_div['href'].endswith('wiadomosc.html'):
                            new_url = self.baseLink + link_div['href']
                            if new_url not in self.urlmap.values():
                                self.urls.append(new_url)
                    except TypeError:
                        pass

        elif section_id is 'bxWiadSwiat':
            for link_div in outer_div.find_all('a'):
                try:
                    if link_div['href'].endswith('wiadomosc.html'):
                        new_url = self.baseLink + link_div['href']
                        if new_url not in self.urlmap.values():
                            self.urls.append(new_url)
                except TypeError:
                    pass

        elif section_id is 'bxTylkowWP':
            for link_div in outer_div.find_all('a'):
                try:
                    if link_div['href'].endswith('wiadomosc.html'):
                        new_url = self.baseLink + link_div['href']
                        if new_url not in self.urlmap.values():
                            self.urls.append(new_url)
                except TypeError:
                    pass

    def scrape_urls(self):
        print 'Scraping', self.name
        for section_id in self.sections:
            self.custom_scrape(section_id)

    def scrape_text(self, link):

        soup = self.read_page(link)

        try:
            self.title = soup.find('header', {'class': 'narrow'}).find('div', {'class': 'h1'}).text
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting title for link:' + self.currentLink)

        try:
            self.bold = soup.find("main", {"class": "ST-Artykul"}).find('div', {'class': 'lead'}).text.strip()
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting bold for link:' + self.currentLink)

        try:
            self.body = soup.find(id='intertext1').text.rstrip()
        except AttributeError:
            self.logger.log(Logger.ERROR, 'Error getting body for link:' + self.currentLink)