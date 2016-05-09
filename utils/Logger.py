# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:54:03 2016

@author: piotrgrudzien
"""

import utils.Utils as ut

class Logger:
    
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    
    def __init__(self, timestamp):
        self.file = '../Logs/' + timestamp
        
    def log(self, level, message):
        out = ut.timestamp() + ' [' + level + '] ' + message
        with(open(self.file, 'a')) as f:
            f.write(out + '\n')