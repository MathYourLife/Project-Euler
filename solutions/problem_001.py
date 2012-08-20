#!/usr/bin/env python
"""
Project Euler - Problem 1
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Author: Daniel Couture
User: MathYourLife
Date: Aug 19, 2012
"""

from sys import path
from os import getcwd

path.append('%s/../ProjectEuler' % getcwd())

import ProjectEuler

PROBLEM_STATEMENT = """
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples_up_to(factor, upper_limit):
    """
    Given a factor and an upper limit, return a list of the
    multiple of that factor up to and including the upper 
    limit value.
    
    @param factor: The value to find multiples of
    @type  factor: int
    
    @param upper_limit: The higest value to include in the list of multiples
    @type  upper_limit: int
    
    @return: Array of multiples
    @rtype: numpy.ndarray
    """
    from numpy import array
    from math import floor
    
    multiples = array(range(1, int(floor(upper_limit / factor) + 1)))
    return multiples * factor

class Problem001(ProjectEuler.Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    If we list all the natural numbers below 10 that are multiples 
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    def __init__(self):
        super(Problem001, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        # Should probably do something sleaker here, but this works
        
        m_of_3 = find_multiples_up_to(3, 1000-1)
        m_of_5 = find_multiples_up_to(5, 1000-1)
        
        total = sum(m_of_3)
        for multiple in m_of_5:
            if multiple not in m_of_3:
                total += multiple
        return total

def main():
    """
    Run this if called directly versus imported
    """
    prob1 = Problem001()
    
    prob1.solve()
    
    print PROBLEM_STATEMENT
    print prob1.results()

if __name__ == "__main__":
    main()

