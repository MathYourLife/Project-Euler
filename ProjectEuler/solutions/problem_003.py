"""
Project Euler - Problem 3
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

Author: Daniel Couture
User: MathYourLife
Date: Aug 24, 2012
"""

from ProjectEuler.Problem import Solution
from Arithmetic import Primes
from numpy import prod

class Problem003(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
    """
    def __init__(self):
        super(Problem003, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        p_lib =  Primes()
        value = 600851475143
        factors = p_lib.prime_factorization(value)
        
        if not prod(factors) == value:
            print 'ERROR'
        return factors[-1]
        

def main():
    """
    Run this if called directly versus imported
    """
    prob3 = Problem003()
    
    prob3.solve()
    
    print prob3.problem_statement()
    print prob3.results()

if __name__ == "__main__":
    main()

