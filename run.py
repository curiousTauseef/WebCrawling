# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:32:13 2016

@author: piotrgrudzien
"""

from OnetCrawl import onetCrawl
from GazetaCrawl import gazetaCrawl
from WPCrawl import wpCrawl
import time, datetime

onetCrawl()
gazetaCrawl()
wpCrawl()
#while True:
#    print datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
#    onetCrawl()
#    gazetaCrawl()
#    wpCrawl()
#    time.sleep(3600)