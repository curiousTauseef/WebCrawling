# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:22:05 2016

@author: piotrgrudzien
"""
import string

def removePunct(text):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    return text