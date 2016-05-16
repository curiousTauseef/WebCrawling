import numpy as np
import pandas as pd
import lda
from nltk.tokenize import RegexpTokenizer
from utils import Utils
from sklearn.feature_extraction.text import CountVectorizer

class LdaManager:
    def __init__(self, logger):
        self.logger = logger
        self.timeline = None
        self.serwismap = None
        self.stop_words = Utils.load_stop_words()
        self.titles = []
        self.texts = []
        self.docs = []


        self.model = lda.LDA(n_topics=30, n_iter=1000, random_state=1)

        self.load_maps()
        self.load_articles()

        self.vectorizer = CountVectorizer(stop_words=self.stop_words, strip_accents='unicode')
        self.X = self.vectorizer.fit_transform(self.texts)


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

    def analyse(self):
        self.model.fit(self.X.toarray())  # model.fit_transform(X) is also available
        self.topic_word = self.model.topic_word_
        self.n_top_words = 8

        for i, topic_dist in enumerate(self.topic_word):
            topic_words = np.array(self.vectorizer.get_feature_names())[np.argsort(topic_dist)][:-(self.n_top_words+1):-1]
            # print('Topic {}: {}'.format(i, ' '.join(topic_words)))
            print 'Topic', i
            for word in topic_words:
                print word.encode('utf-8')

        pass
