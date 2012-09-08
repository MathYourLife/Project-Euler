"""
Confirm functionality of the Arithmetic classes
"""

from ProjectEuler import Arithmetic
import unittest
import numpy as np

class TestPrimes(unittest.TestCase):
    
    def test_set_position(self):
        
        values = Arithmetic.primes_up_to(2)
        msg = 'Primes through 2'
        exp = np.array([2])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.primes_up_to(6)
        msg = 'Primes through 6'
        exp = np.array([2, 3, 5])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.primes_up_to(20)
        msg = 'Primes through 6'
        exp = np.array([2, 3, 5, 7, 11, 13, 17, 19])
        self.assertListEqual(list(exp), list(values), msg)

    def test_prime_factorization(self):
        values = Arithmetic.prime_factorization(1)
        msg = 'Prime factorization for 1'
        exp = np.array([])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.prime_factorization(3)
        msg = 'Prime factorization for 3'
        exp = np.array([3])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.prime_factorization(6)
        msg = 'Prime factorization for 3'
        exp = np.array([2, 3])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.prime_factorization(10)
        msg = 'Prime factorization for 3'
        exp = np.array([2, 5])
        self.assertListEqual(list(exp), list(values), msg)
        
        values = Arithmetic.prime_factorization(15)
        msg = 'Prime factorization for 3'
        exp = np.array([3, 5])
        self.assertListEqual(list(exp), list(values), msg)
        



if __name__ == '__main__':
    unittest.main()
