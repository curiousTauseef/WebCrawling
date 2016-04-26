# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:32:13 2016

@author: piotrgrudzien
"""

import Utils
from Logger import Logger
from OnetCrawler import OnetCrawler
from WPCrawler import WPCrawler
from InteriaCrawler import InteriaCrawler
from GazetaCrawler import GazetaCrawler
from NiezaleznaCrawler import NiezaleznaCrawler
from wPolityceCrawler import wPolityceCrawler
from SimilarityFinder import SimilarityFinder
import time


class Runner:
    def __init__(self):
        self.logger = None
        self.crawlers = []
        self.crawlers.append(OnetCrawler())
        self.crawlers.append(WPCrawler())
        self.crawlers.append(InteriaCrawler())
        self.crawlers.append(GazetaCrawler())
        self.crawlers.append(NiezaleznaCrawler())
        self.crawlers.append(wPolityceCrawler())
        self.sf = SimilarityFinder()

    def run(self):
        self.logger = Logger(Utils.timestamp()) # initialise logger for this crawl

        for crawler in self.crawlers:
            crawler.crawl(self.logger)

        # self.sf.getSimilar()
r = Runner()
r.run()

#    time.sleep(3600)