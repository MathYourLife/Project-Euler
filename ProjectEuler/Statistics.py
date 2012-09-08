"""
ARITHMETIC class

classes and methods contained are targeted to basic number
theory and number facts.
"""

import numpy as np
from scipy import factorial

def C(n, r):
    if n - r > r:
        num = np.prod(np.arange(n - r + 1, n+1))
        den = factorial(r)
        return num / den
    else:
        num = np.prod(np.arange(r + 1, n+1))
        den = factorial(n - r)
        return num / den

def P(n, r):
    return factorial(n) / factorial(n - r)

class Combination(object):
    def __init__(self, items):
        self.items = items
    
    

