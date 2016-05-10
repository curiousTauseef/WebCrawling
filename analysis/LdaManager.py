import numpy as np
import pandas as pd
import lda
from nltk.tokenize import RegexpTokenizer
from utils import Utils
import textmining


class LdaManager:
    def __init__(self, logger):
        self.logger = logger
        self.timeline = None
        self.serwismap = None
        self.titles = []
        self.texts = []
        self.docs = []
        self.tokenizer = RegexpTokenizer(r'\w+')

        self.model = lda.LDA(n_topics=20, n_iter=500, random_state=1)

        self.load_maps()
        self.load_articles()

        self.tdm = textmining.TermDocumentMatrix()

        for text in self.texts:
            self.tdm.add_doc(text)

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
        # TODO prepare data properly here
        self.model.fit(pd.DataFrame(self.tdm.rows()))  # model.fit_transform(X) is also available
        self.topic_word = self.model.topic_word_  # model.components_ also works
        self.n_top_words = 8

        for i, topic_dist in enumerate(self.topic_word):
            topic_words = np.array(self.tdm.rows().next())[np.argsort(topic_dist)][:-(self.n_top_words+1):-1]
            print('Topic {}: {}'.format(i, ' '.join(topic_words)))

        pass
