# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 22:10:45 2016

@author: piotrgrudzien

Class for finding similar articles (articles on the same topic)
"""

import Utils
import numpy as np
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
        self.get_top(10)

    def load_maps(self):
        self.timeline = Utils.load_map('Timeline', self.logger)
        self.serwismap = Utils.load_map('SerwisMap', self.logger)
        self.urlmap = Utils.load_map('UrlMap', self.logger)

    def load_articles(self):
        sections = {'TITLE': 0, 'BOLD': 1, 'BODY': 2}
        for ID in self.timeline:
            article = Utils.read(ID, self.serwismap[ID])
            self.titles.insert(ID, article[sections['TITLE']])
            self.texts.insert(ID, ' '.join([article[sections['BOLD']], article[sections['BODY']]]))
        # self.titles = list(set(self.titles))
        # self.texts = list(set(self.texts))

    def get_top(self, n):
        vect = TfidfVectorizer()
        tfidf = vect.fit_transform(self.texts)
        sim = (tfidf * tfidf.T).A
        np.fill_diagonal(sim, 0)
        count = 0
        while count < n:
            indices = Utils.get_max_indices(sim)
            if sim[indices] < 0.99 and self.serwismap[indices[0]] == self.serwismap[indices[1]]:
                for i in [0, 1]:
                    # print self.serwismap[indices[i]], ':', self.titles[indices[i]]
                    print self.serwismap[indices[i]], ':', self.texts[indices[i]]
                print sim[indices], 'at index', indices
                count += 1
            sim[indices] = 0
