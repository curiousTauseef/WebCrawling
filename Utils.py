# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 19:22:05 2016

@author: piotrgrudzien
"""
import string, datetime, time, re


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
