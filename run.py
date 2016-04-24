# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:32:13 2016

@author: piotrgrudzien
"""

from OnetCrawler import OnetCrawler
from WPCrawler import WPCrawler
import time

onet_crawler = OnetCrawler()
onet_crawler.crawl()

wp_crawler = WPCrawler()
wp_crawler.crawl()

#    time.sleep(3600)