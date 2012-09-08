"""
Confirm functionality of the Arithmetic classes
"""

from ProjectEuler import Statistics
from ProjectEuler.test.TestBase import BaseTest
import numpy as np
import unittest

class TestC(BaseTest):
    
    def test_return(self):
        
        value = Statistics.C(3,1)
        self.assertEqual(3, value, 'Checking combination formula')
        
        value = Statistics.C(4,2)
        self.assertEqual(6, value, 'Checking combination formula')
        
        value = Statistics.C(5,2)
        self.assertEqual(10, value, 'Checking combination formula')
        
        value = Statistics.C(10,6)
        self.assertEqual(210, value, 'Checking combination formula')
        
        value = Statistics.C(15,3)
        self.assertEqual(455, value, 'Checking combination formula')
        
        value = Statistics.C(15,13)
        self.assertEqual(105, value, 'Checking combination formula')
        
        value = Statistics.C(30,28)
        self.assertEqual(435, value, 'Checking combination formula')
        

class TestR(BaseTest):
    def test_return(self):
        value = Statistics.P(3,3)
        self.assertEqual(6, value, 'Checking combination formula')
        
        value = Statistics.P(4,3)
        self.assertEqual(24, value, 'Checking combination formula')
        
        value = Statistics.P(13,3)
        self.assertEqual(1716, value, 'Checking combination formula')
        
        value = Statistics.P(13,9)
        self.assertEqual(259459200, value, 'Checking combination formula')
        

if __name__ == '__main__':
    unittest.main()
