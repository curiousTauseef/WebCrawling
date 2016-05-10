# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:32:13 2016

@author: piotrgrudzien
"""

from crawlers.InteriaCrawler import InteriaCrawler
from utils.Logger import Logger
from crawlers.NiezaleznaCrawler import NiezaleznaCrawler
from crawlers.WPCrawler import WPCrawler
from crawlers.wPolityceCrawler import wPolityceCrawler

from analysis.SimilarityFinder import SimilarityFinder
from analysis.LdaManager import LdaManager
from crawlers.GazetaCrawler import GazetaCrawler
from crawlers.OnetCrawler import OnetCrawler
from utils import Utils


class Runner:
    def __init__(self):
        self.logger = None
        self.sf = None
        self.lm = None
        self.crawlers = []
        self.crawlers.append(OnetCrawler())
        self.crawlers.append(WPCrawler())
        self.crawlers.append(InteriaCrawler())
        self.crawlers.append(GazetaCrawler())
        self.crawlers.append(NiezaleznaCrawler())
        self.crawlers.append(wPolityceCrawler())

    def run(self):
        self.logger = Logger(Utils.timestamp()) # initialise logger for this crawl
        self.sf = SimilarityFinder(self.logger)
        self.lm = LdaManager(self.logger)
        for crawler in self.crawlers:
            crawler.crawl(self.logger)

        # self.sf.get_similar()
        # self.lm.analyse()

r = Runner()
r.run()

#    time.sleep(3600)