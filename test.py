# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:19:41 2016

@author: piotrgrudzien
"""

import numpy as np
import Utils

a = np.array(range(1, 27)).reshape([2, 13])
print a
print Utils.get_max_indices(a)
# print a[Utils.get_max_indices(a)[0], Utils.get_max_indices(a)[1]]
print a[Utils.get_max_indices(a)]