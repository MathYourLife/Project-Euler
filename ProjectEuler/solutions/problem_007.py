"""
Project Euler - Problem 7
http://projecteuler.net/problem=7

By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?

Author: Daniel Couture
User: MathYourLife
Date: Aug 25, 2012
"""

from ProjectEuler.Problem import Solution
from ProjectEuler.Arithmetic import Primes

class Problem007(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    By listing the first six prime numbers:
    2, 3, 5, 7, 11, and 13, 
    we can see that the 6th prime is 13.
    
    What is the 10 001st prime number?
    """
    def __init__(self):
        super(Problem007, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        p_inst = Primes()
        
        up_to = 0
        delta = 5000
        while len(p_inst.primes_list) < 10002:
            up_to += delta
            p_inst.primes_up_to(up_to)
        
        return p_inst.primes_list[10000]
        

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem007()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

