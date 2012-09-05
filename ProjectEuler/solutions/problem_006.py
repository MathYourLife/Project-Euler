"""
Project Euler - Problem 6
http://projecteuler.net/problem=6

The sum of the squares of the first ten 
natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten 
natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the 
squares of the first ten natural numbers and 
the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the 
squares of the first one hundred natural 
numbers and the square of the sum.

Author: Daniel Couture
User: MathYourLife
Date: Aug 25, 2012
"""

from ProjectEuler.Problem import Solution

class Problem006(Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    The sum of the squares of the first ten 
    natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten 
    natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the 
    squares of the first ten natural numbers and 
    the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the 
    squares of the first one hundred natural 
    numbers and the square of the sum.
    """
    def __init__(self):
        super(Problem006, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        top = 100
        
        # Example:
        # (1+2+3+4+5)^2 - (1^2+2^2+...+5^2)
        # 
        # A full square of edge length 15 taking
        # out the diagonal perfect squares.
        # 
        # Geometric View:
        # 
        #  5*1  5*2  5*3  5*4 (5*5)
        #  4*1  4*2  4*3 (4*4) 4*5
        #  3*1  3*2 (3*3) 3*4  3*5
        #  2*1 (2*2) 2*3  2*4  2*5
        # (1*1) 1*2  1*3  1*4  1*5
        # 
        # 2 * [
        #             4 (5)
        #         3 (4 + 5)
        #     2 (3 + 4 + 5)
        # 1 (2 + 3 + 4 + 5)
        # ]
        
        sum_value = 0
        total = 0
        for num in range(top, 1, -1):
            sum_value += num
            total += (num - 1) * sum_value
        
        return total * 2
        

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem006()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

