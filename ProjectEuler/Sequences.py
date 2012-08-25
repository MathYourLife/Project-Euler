"""
ProjectEuler.Sequences

Collection of classes for various type of sequences.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012
"""

class Fibonacci:
    def __init__(self, current = 1, previous = 0):
        self.current = current
        self.previous = previous
    
    def next(self):
        next_value = self.current + self.previous
        self.previous = self.current
        self.current = next_value
        return next_value

