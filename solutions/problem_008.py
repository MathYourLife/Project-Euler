#!/usr/bin/env python
"""
Project Euler - Problem 8
http://projecteuler.net/problem=8

Find the greatest product of five consecutive 
digits in the 1000-digit number.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Author: Daniel Couture
User: MathYourLife
Date: Aug 27, 2012
"""

from sys import path
from os import getcwd

path.append('%s/../ProjectEuler' % getcwd())

import ProjectEuler

class Problem008(ProjectEuler.Solution):
    """
    Extension of the ProjectEuler.Solution class that solves the problem:
    
    Find the greatest product of five consecutive 
    digits in the 1000-digit number.

    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
    """
    def __init__(self):
        super(Problem008, self).__init__()
    
    def find_solution(self):
        """
        This method contains the guts of finding the solution.
        The timer starts just prior to calling this method
        and stops just after returning the solution's value.
        """
        
        large_number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
        from numpy import array, prod
        
        # Read the string into a numpy integer array
        large_number = large_number.replace("\n", "")
        large_list = array(list(large_number), int)
        
        # Solution method:
        #  Keep track of the position in the string and
        #  the product of the 5 values at that position.
        #  To shift to the next set of 5 values, divide
        #  out the number shifting off the trailing
        #  edge and multiply in the next value.  If we
        #  hit a zero, skip over that section.
        
        # Initialize the values for the loop
        max_product = prod(large_list[0:5])
        current_product = max_product
        pos = 5
        while pos < len(large_list):
        	# Get the next value to multiply in
            in_val = large_list[pos]
            if in_val == 0:
            	# The next value is a zero so skip ahead
            	# until we see 5 nonzero values.
                pos += 5
                current_product = prod(large_list[pos - 4:pos + 1])
                while current_product == 0:
                    pos += 1
                    current_product = prod(large_list[pos - 4:pos + 1])
                
            else:
            	# Find the value being shifted off the trailing edge
                out_val = large_list[pos - 5]
                
                # Remove the trailing factor and include the new one
                current_product /= out_val
                current_product *= in_val
            
            # Track the max
            if current_product > max_product:
                max_product = current_product
            
            # Shift
            pos += 1
        
        return max_product
        

def main():
    """
    Run this if called directly versus imported
    """
    prob = Problem008()
    
    prob.solve()
    
    print prob.problem_statement()
    print prob.results()

if __name__ == "__main__":
    main()

