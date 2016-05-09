# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:28:45 2016

@author: piotrgrudzien

Generic logger (abstract class)
"""

import datetime
import pickle
import time
import urllib2

from utils.Logger import Logger
from bs4 import BeautifulSoup

from utils import Utils


class Crawler:
    def __init__(self, base_link, name):
        self.baseLink = base_link
        self.name = name
        self.mainPage = None
        self.urls = []
        self.logger = None
        self.currentLink = None
        self.title = ''
        self.bold = ''
        self.body = ''
        self.timeline = None
        self.serwismap = None
        self.urlmap = None

    def crawl(self, logger):
        self.logger = logger # assign logger for this crawl
        self.logger.log(Logger.INFO, 'Starting ' + self.name + ' crawl') # log start of the crawl
        self.urls = [] # prepare empty url list
        self.load_maps() # load maps from disk
        self.load_main_page() # load main page
        self.scrape_urls() # get all article urls
        self.urls = list(set(self.urls)) # deduplicate article urls
        for self.currentLink in self.urls:
            print str(self.urls.index(self.currentLink) + 1), '/', str(len(self.urls)) # write out progress to console
            self.logger.log(Logger.INFO, 'Link: ' + self.currentLink) # log info about the article being read
            self.scrape_text(self.currentLink) # get text from the article
            self.clear_text() # remove punctuation, extra spaces, tabs, new-lines
            if self.checks_passed(): # check if article data is valid
                self.save_text() # write article data to file
        self.save_maps() # save the updated timeline to disk

    def load_maps(self):
        self.timeline = Utils.load_map('Timeline', self.logger)
        self.serwismap = Utils.load_map('SerwisMap', self.logger)
        self.urlmap = Utils.load_map('UrlMap', self.logger)

    """ Can sometimes be overriden in subclasses """
    def load_main_page(self):
        self.mainPage = self.read_page(self.baseLink)  # load main page

    def save_maps(self):
        pickle.dump(self.timeline, open('../Maps/Timeline.p', 'wb'))
        pickle.dump(self.serwismap, open('../Maps/SerwisMap.p', 'wb'))
        pickle.dump(self.urlmap, open('../Maps/UrlMap.p', 'wb'))

    def read_page(self, link):
        r = urllib2.urlopen(link).read()
        return BeautifulSoup(r, 'lxml')

    """ Can sometimes be overriden in subclasses """
    def checks_passed(self):
        self.logger.log(Logger.INFO, 'No of words: title - ' + str(len(self.title.split())) + ', bold - ' + str(
            len(self.bold.split())) + ', body - ' + str(len(self.body.split())))
        return str(len(self.title.split())) > 0

    def save_text(self):
        ID = len(self.timeline) + 1
        f = open('../' + self.name + '/Articles/' + str(ID) + '.txt', 'w')
        f.write('TITLE:' + self.title.encode('UTF8') + '\n')
        f.write('BOLD:' + self.bold.encode('UTF8') + '\n')
        f.write('BODY:' + self.body.encode('UTF8'))
        f.close()
        self.timeline[ID] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        self.serwismap[ID] = self.name
        self.urlmap[ID] = self.currentLink
        self.reset()  # reset title, bold and body holders

    def reset(self):
        self.title = ''
        self.bold = ''
        self.body = ''

    def clear_text(self):
        self.title = Utils.clear_text(self.title)
        self.bold = Utils.clear_text(self.bold)
        self.body = Utils.clear_text(self.body)

    """ 'Abstract' method """

    def scrape_urls(self):
        raise Exception('scrapeUrls method not overriden in class', type(self).__name__)

    """ 'Abstract' method """

    def scrape_text(self, link):
        raise Exception('scrapeUrls method not overrident in class', type(self).__name__)
