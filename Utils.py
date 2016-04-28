# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:22:05 2016

@author: piotrgrudzien
"""
import string, datetime, time, re, pickle
from Logger import Logger


def remove_punct(text):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    return text


def timestamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%dT%H-%M-%S")


def clear_text(text):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    # text = re.sub(r'[\W_]+^ ', '', text, flags=re.UNICODE)
    return ' '.join(text.split())


def load_map(map, logger):
    myMaps = ['Timeline', 'SerwisMap', 'UrlMap']
    if map not in myMaps:
        raise AttributeError(map, 'is not one of the available maps: ', str(myMaps))
    try:
        return pickle.load(open('../Maps/' + map + '.p', 'rb'))
    except IOError:
        logger.log(Logger.WARN, 'Loading empty ' + map)
        return {}


def read(ID, serwis):
    with (open('../' + serwis + '/Articles/' + str(ID) + '.txt', 'r')) as f:
        article = f.readlines()
    if len(article) != 3:
        raise AttributeError('Article', str(ID), ', serwis', serwis, 'has', str(len(article)), 'lines')
    article = [line[line.find(':') + 1:] for line in article]
    return article
