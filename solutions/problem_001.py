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

def find_multiples_up_to(factors, upper_limit):
    """
    Given a list of factors generate an array of multiples for those values. up
    to and including the upper limit value.  Multiple factors will result in an
    array that is the union of the individual sets.
    @example:
        call:    find_multiples_up_to([3,5], 15)
        returns: array([3, 5, 6, 9, 10, 12, 15])
    
    @param factors: list of factors to generate multiples from, if multiples
                    provided, the returned array is a union of the individual sets
    @type  factors: list
    
    @param upper_limit: The higest value to include in the list of multiples
    @type  upper_limit: int
    
    @return: Array of multiples
    @rtype: numpy.ndarray
    """
    from numpy import array, arange, unique, concatenate
    
    values = arange(1, upper_limit+1)
    multiples = array([])
    for factor in factors:
        multiples = unique(concatenate([multiples, values[values % factor == 0]]))
    
    return multiples

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
        from numpy import sum as np_sum
        
        multiples = find_multiples_up_to([3, 5], 999)
        
        return np_sum(multiples)

def main():
    """
    Run this if called directly versus imported
    """
    prob1 = Problem001()
    
    prob1.solve()
    
    print prob1.problem_statement()
    print prob1.results()
    
    

if __name__ == "__main__":
    main()

