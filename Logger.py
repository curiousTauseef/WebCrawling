# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 11:54:03 2016

@author: piotrgrudzien
"""

import Utils

class Logger:
    
    INFO = 'INFO'
    WARN = 'WARN'
    ERROR = 'ERROR'
    
    def __init__(self, timestamp):
        self.file = '../Logs/' + timestamp
        
    def log(self, level, message):
        out = Utils.timestamp() + ' [' + level + '] ' + message
        with(open(self.file, 'w')) as f:
            f.write(out + '/n')