#!/usr/bin/env python
"""
Project Euler - Problem 9
http://projecteuler.net/problem=9

A Pythagorean triplet is a set of three 
natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean 
triplet for which a + b + c = 1000.
Find the product abc.

Author: Daniel Couture
User: MathYourLife
Date: Sep 1, 2012
"""

from sys import path
from os import getcwd

path.append('%s/../ProjectEuler' % getcwd())

import ProjectEuler
from Sequences import PerfectSquares

class Problem009(ProjectEuler.Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    A Pythagorean triplet is a set of three 
    natural numbers, a < b < c, for which,
    
    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
    
    There exists exactly one Pythagorean 
    triplet for which a + b + c = 1000.
    Find the product abc.
    """
    def __init__(self):
        super(Problem009, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        # Create a lookup table for all the perfect squares
        # from 1 to 997.  a can be as small as 1 and b as small
        # as 2, which makes a max for c of 1000 - 1 - 2 = 997
        psquares = PerfectSquares()
        c_max = 997
        squares = psquares.get_squares_up_to(c_max * c_max)
        # Don't need the PerfectSquares class anymore
        del psquares
        
        solved = False
        # Initialize the outer 'a' loop
        a = 1
        while (not solved) & (a <= 995):
            # Calculate the max c value for this a
            # c is maximized when b = a + 1
            b = a +1
            c = 1000 - (a + b)
            # Start with b = a + 1 and c maximized.  Walk
            # b and c in towards each other until they meet
            while (not solved) & (c > b):
                # Check for the Pythagorean triplet
                if squares[a-1] + squares[b-1] == squares[c-1]:
                    # FOUND IT. Mark as solved and 
                    solved = True
                    break
                # Decrement c and calculate the corresponding b
                c -= 1
                b = 1000 - (a + c)
            
            if solved:
                break
            a += 1
        
        # Return the solution the product abc
        return "%d" % (a * b * c)

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem009()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

