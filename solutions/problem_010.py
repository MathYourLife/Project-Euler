#!/usr/bin/env python
"""
Project Euler - Problem 10
http://projecteuler.net/problem=10

The sum of the primes below 10 is 
2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Author: Daniel Couture
User: MathYourLife
Date: Sep 1, 2012
"""

from sys import path
from os import getcwd

path.append('%s/../ProjectEuler' % getcwd())

import ProjectEuler
from Arithmetic import Primes
from numpy import sum

class Problem010(ProjectEuler.Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    The sum of the primes below 10 is 
    2 + 3 + 5 + 7 = 17.
    
    Find the sum of all the primes below two million.
    """
    def __init__(self):
        super(Problem010, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        p_inst = Primes()
        
        up_to = 0
        delta = 50000
        while up_to < 2000000:
            up_to += delta
            p_inst.primes_up_to(up_to)
        
        p_list = p_inst.primes_up_to(2000000)
        return "%d" % sum(p_list)

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem010()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

