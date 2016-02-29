# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import os
from unidecode import unidecode
import re, string
import pandas as pd
with open('polishStopWords.txt') as f:
    stopWords = f.read().splitlines()
#r = urllib.urlopen('http://www.onet.pl/').read()
#soup = BeautifulSoup(r, 'lxml')
        
#Links = [link['href'] for link in soup(['a']) if link.has_attr('href')]

WordDepo = []

#for link in Links:
#    if('wiadomosci' in link):
link = 'http://wiadomosci.gazeta.pl/wiadomosci/1,114871,19604915,general-kuklinski-mon-prosi-prezydenta-o-posmiertny-awans.html#MTstream'
#link = 'http://www.onet.pl/'
r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

for script in soup(["script", "style"]):
    script.extract()    # rip it out

tekst = unidecode(soup.get_text().lower())

tekst = re.sub(r'([^\s\w]|_)+', '', tekst)
tekst = os.linesep.join([s for s in tekst.splitlines() if len(s) > 20])

words = tekst.split()
words = [x for x in words if (x not in stopWords) & (x.isalpha())]
WordDepo.extend(words)
        
print pd.Series(WordDepo).value_counts()

text_file = open("Output.txt", "w")
text_file.write(tekst)
text_file.close()