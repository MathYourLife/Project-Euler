"""
Project Euler - Problem 4
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest 
palindrome made from the product of two 2-digit numbers is 
9009 = 91 x 99.

Find the largest palindrome made from the product of two 
3-digit numbers.

Author: Daniel Couture
User: MathYourLife
Date: Aug 25, 2012
"""

from ProjectEuler.Problem import Solution
from Arithmetic import Primes
from Sequences import Palindrome
from numpy import array, append

class Problem004(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    A palindromic number reads the same both ways. The largest 
    palindrome made from the product of two 2-digit numbers is 
    9009 = 91 x 99.
    Find the largest palindrome made from the product of two 
    3-digit numbers.
    """
    def __init__(self):
        super(Problem004, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        # Initialize the palindrome instance with a palindrome just
        # above the largest possible and walk backwards.
        #
        # 999 * 999 = 998001  so 998899 is too large
        p_value = 998899
        p_seq = Palindrome(p_value)
        
        prime_seq = Primes()
        primes_list = prime_seq.primes_up_to(1000)
        while p_value >= 10000:
            p_value = p_seq.previous()
            factors = array([])
            value = p_value
            for prime in primes_list:
                # If the value is 1, we've got it all
                if value == 1:
                    break
                while value % prime == 0:
                    # this prime is a factor of value so pull it out
                    factors = append(factors, [prime])
                    value = value / prime
            if value != 1:
                # If the value is not 1 by now, a larger than 3 digit
                # prime factor exists so this is not a solution.
                continue
            
            # Try to construct two 3-digit factors.  Start at the highest
            # prime factor, and multiply it in to the lowest of the two 
            # factors as you go trying to keep them even so both end up
            # under the 1000 mark.
            factor_1 = 1
            factor_2 = 1
            for index in range(len(factors), 0, -1):
                factor = factors[index-1]
                if factor_1 <= factor_2:
                    factor_1 *= factor
                else:
                    factor_2 *= factor
            if factor_1 < 1000 and factor_2 < 1000:
                break
        
        return '%d x %d = %d' % (factor_1, factor_2, factor_1 * factor_2)
        

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem004()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

