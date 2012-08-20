"""
Project Euler - Problem Base
http://projecteuler.net/


This establishes a base class with 
common methods for Project Euler problems

Author: Daniel Couture
User: MathYourLife
"""

import Tools

class Solution(object):
    """
    Base class for running Project Euler solutions.
    """
    def __init__(self):
        self.timer = Tools.Timer()
        self.solution = 42
        
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        from time import sleep
        sleep(2)
        return 42
        
    def solve(self):
        """
        Solve
        Manage the timer and run the find_solution script.
        """
        self.timer.start_timer()
        self.solution = self.find_solution()
        self.timer.stop_timer()
        
    def results(self):
        """
        Assemble the results of running the solve method.
        
        @return: String to print containing solution details.
        @rtype:  str
        """
        result = """
Solution of:
%s

Solution took %0.1f seconds

What's next?

""" % (self.solution, self.timer.duration())
        return result

