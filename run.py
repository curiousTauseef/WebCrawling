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
import time

class Runner:
    def __init__(self):
        self.logger = None
        self.onet_crawler = OnetCrawler()
        self.wp_crawler = WPCrawler()
        self.interia_crawler = InteriaCrawler()
        self.gazeta_crawler = GazetaCrawler()
        self.niezalezna_crawler = NiezaleznaCrawler()
        self.wpolityce_crawler = wPolityceCrawler()

    def run(self):
        self.logger = Logger(Utils.timestamp()) # initialise logger for this crawl
        # self.onet_crawler.crawl(self.logger)
        # self.wp_crawler.crawl(self.logger)
        # self.interia_crawler.crawl(self.logger)
        # self.gazeta_crawler.crawl(self.logger)
        # self.niezalezna_crawler.crawl(self.logger)
        self.wpolityce_crawler.crawl(self.logger)

r = Runner()
r.run()

#    time.sleep(3600)