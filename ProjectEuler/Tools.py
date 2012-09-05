"""
ProjectEuler.Tools

General utilities that may get pulled out to a 
dedicated class later if needed.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012
"""

from time import time

class Timer(object):
    """
    Timer
    
    Basic stopwatch functionality.
    """
    def __init__(self):
        self.start_time = 0
        self.stop_time = 0
    
    def start_timer(self):
        """
        Mark the start time.
        """
        self.start_time = time()
        self.stop_time = 0
    
    def stop_timer(self):
        """
        Mark the stop time.
        """
        self.stop_time = time()
    
    def duration(self):
        """
        Calculate the duration between start and stop times.
        
        @return: Seconds from start to stop calls
        @rtype: float
        """
        return self.stop_time - self.start_time

