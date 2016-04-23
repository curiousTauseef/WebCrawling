# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 10:28:45 2016

@author: piotrgrudzien

Generic logger (abstract class)
"""

import pickle
import Utils
from Logger import Logger

class Crawler:
    
    def __init__(self, baseLink, name):
        self.baseLink = baseLink
        self.name = name
        
    def crawl(self):
        self.logger = Logger(Utils.timestamp())
        self.logger.log(Logger.INFO, 'Starting ' + self.name + ' crawl')
        self.loadTimeline()
        self.scrapeUrls() # override in subclasses (perhaps not the whole method, only some bits)
        self.scrapeText() # override in subclasses (perhaps not the whole method, only some bits)
        self.saveTimeline()
        
        
    def loadTimeline(self):
        try:
            self.timeline = pickle.load(open('../' + self.name + '/' + self.name + '_Timeline.p', 'rb'))
        except IOError:
            self.logger.log(Logger.WARN, 'Loading empty ' + self.name + '_Timeline')
            self.timeline = {}
            
    def saveTimeline(self):
        pickle.dump(self.timeline, open('../' + self.name + '/' + self.name + '_Timeline.p', 'wb'))
        
    """ Abstract method """
    def scrapeUrls():
        pass
    
    """ Abstract method """
    def scrapeText():
        pass