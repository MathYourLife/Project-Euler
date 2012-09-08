"""
Project Euler - Problem 5
http://projecteuler.net/problem=5

2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?

Author: Daniel Couture
User: MathYourLife
Date: Aug 25, 2012
"""

from ProjectEuler.Problem import Solution
from ProjectEuler import Arithmetic
import numpy as np

class Problem005(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    2520 is the smallest number that can be divided by 
    each of the numbers from 1 to 10 without any remainder.
    
    What is the smallest positive number that is evenly 
    divisible by all of the numbers from 1 to 20?
    """
    def __init__(self):
        super(Problem005, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        #  What number to we want to include up to.
        up_to = 20
        # Initialize the prime factors for the solution
        factors = np.array([])
        
        # Starting at 1 and going up to the up_to limit,
        # Calculate the prime factorization for each item
        # If the facotrs have already been accounted for, we're
        # all set.
        #  
        #  Ex:  from 2 to 7 the factors array would include
        #       [ 2, 2, 3, 5, 7 ]
        #       The prime factorization for 8 is 2 * 2 * 2.
        #       The factors array already has 2's but not three
        #       of them so add one more.
        #       [ 2, 2, 2, 3, 5, 7 ]
        
        for item in range(2, up_to + 1):
            # Get the prime factorization for "item"
            primes = Arithmetic.prime_factorization(item)
            for factor in primes:
                # if the factor is not present or there are not enough 
                # of them append another one on
                if sum(factors == factor) < sum(primes == factor):
                    factors = np.append(factors, factor)
        
        # Final answer is the product of the accumulated primes
        return np.prod(factors)
        

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem005()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

