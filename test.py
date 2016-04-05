# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup, Comment
from Utils import removePunct
import urllib2
import time, datetime, string, pickle


link = 'http://wiadomosci.wp.pl/kat,1515,title,Mezczyzna-ktory-zrobil-sobie-selfie-z-porywaczem-trafil-teraz-na-inne-historyczne-zdjecia,wid,18245759,wiadomosc.html'

""" Read the main wp wiadomosci page """
r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')
    
print soup.prettify()