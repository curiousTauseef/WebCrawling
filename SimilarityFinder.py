# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:10:45 2016

@author: piotrgrudzien

Class for finding similar articles (articles on the same topic)
"""

import Utils
from sklearn.feature_extraction.text import TfidfVectorizer

class SimilarityFinder:
    def __init__(self, logger):
        self.logger = logger
        self.timeline = None
        self.serwismap = None
        self.titles = []
        self.texts = []

    def get_similar(self):
        self.load_maps()
        self.load_articles()

    def load_maps(self):
        self.timeline = Utils.load_map('Timeline', self.logger)
        self.serwismap = Utils.load_map('SerwisMap', self.logger)

    def load_articles(self):
        sections = {'TITLE': 0, 'BOLD': 1, 'BODY': 2}
        for ID in self.timeline:
            article = Utils.read(ID, self.serwismap[ID])
            self.titles.insert(ID, article[sections['TITLE']])
            self.texts.insert(ID, ' '.join([article[sections['BOLD']], article[sections['BODY']]]))