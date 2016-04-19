# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 23:32:13 2016

@author: piotrgrudzien
"""

from OnetCrawl import onetCrawl
from GazetaCrawl import gazetaCrawl
from WPCrawl import wpCrawl
from InteriaCrawl import interiaCrawl
from WyborczaCrawl import wyborczaCrawl
from NiezaleznaCrawl import niezaleznaCrawl
import time, datetime

#onetCrawl()
#gazetaCrawl()
#wpCrawl()
#interiaCrawl()
#wyborczaCrawl()
niezaleznaCrawl()
#while True:
#    print datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
#    onetCrawl()
#    gazetaCrawl()
#    wpCrawl()
#    time.sleep(3600)