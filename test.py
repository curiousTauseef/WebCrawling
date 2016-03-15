# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

from bs4 import BeautifulSoup
import urllib2

#link = 'http://wiadomosci.onet.pl/kraj/ludwik-dorn-o-zamieszaniu-wokol-tk-jaroslaw-kaczynski-sie-nie-cofnie/ty0w2h'

link = 'http://wiadomosci.wp.pl/kat,1342,title,Pawel-Lisicki-Moje-zycie-w-dyktaturze-PiS,wid,18215202,wiadomosc.html?ticaid=116a89'

r = urllib2.urlopen(link).read()
soup = BeautifulSoup(r, 'lxml')

#a = soup.find_all('p')
#
#for elem in a:
#    print elem.get_text()

print soup.prettify()