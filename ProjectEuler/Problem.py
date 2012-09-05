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
        
    def problem_statement(self):
        """
        Grab the problem statement that for now is just the doc string.
        """
        return self.__doc__
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        from time import sleep
        sleep(2)
        return 42
        
    def reset(self):
        """
        Use to reset an existing class.  In the case of a time_solution
        call this can be used to clear our cached data on the object
        """
        pass
    
    def time_solution(self, loop_count = 10):
        """
        Use for optimization.  Run the solution multiple times
        clearing the object cache each time to get an adequate
        baseline for the time to create the solution.
        """
        loop_timer = Tools.Timer()
        loop_timer.start_timer()
        for count in range(0, loop_count):
            self.reset()
            self.solve()
        loop_timer.stop_timer()
        print self.results()
        print """
Ran the solution algorithm %d times at:
Total Time (sec): %0.1f
Seconds / Solve: %s
""" % (loop_count, loop_timer.duration(), loop_timer.duration()/loop_count)
        
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

Solution took %0.3f seconds

What's next?

""" % (self.solution, self.timer.duration())
        return result

