"""
Once a problem is successfully solved, add to the test
suite to ensure future changes to modules do not 
corrupt the solution.
"""

from ProjectEuler.test.TestBase import BaseTest
import ProjectEuler.solutions.problem_001
import ProjectEuler.solutions.problem_002
import ProjectEuler.solutions.problem_003
import ProjectEuler.solutions.problem_004
import ProjectEuler.solutions.problem_005
import ProjectEuler.solutions.problem_006
import ProjectEuler.solutions.problem_007
import ProjectEuler.solutions.problem_008
import ProjectEuler.solutions.problem_009
import ProjectEuler.solutions.problem_010
import ProjectEuler.solutions.problem_011
import ProjectEuler.solutions.problem_012
import unittest

class VerifySolutions(BaseTest):
    """
    Keep track of all the solutions as we progress so any changes
    to shared libs will not affect the value of previous solutions.
    """
    def test_prob_001(self):
        """Test problem 1"""
        prob = ProjectEuler.solutions.problem_001.Problem001()
        self.assertEqual('233168', prob.find_solution())
    
        """Test problem 2"""
        prob = ProjectEuler.solutions.problem_002.Problem002()
        self.assertEqual(4613732, prob.find_solution())
    
    def test_prob_003(self):
        """Test problem 3"""
        prob = ProjectEuler.solutions.problem_003.Problem003()
        self.assertEqual('6857', prob.find_solution())
    
    def test_prob_004(self):
        """Test problem 4"""
        prob = ProjectEuler.solutions.problem_004.Problem004()
        self.assertEqual('993 x 913 = 906609', prob.find_solution())
    
    def test_prob_005(self):
        """Test problem 5"""
        prob = ProjectEuler.solutions.problem_005.Problem005()
        self.assertEqual(232792560, prob.find_solution())
    
    def test_prob_006(self):
        """Test problem 6"""
        prob = ProjectEuler.solutions.problem_006.Problem006()
        self.assertEqual(25164150, prob.find_solution())
    
    def test_prob_007(self):
        """Test problem 7"""
        prob = ProjectEuler.solutions.problem_007.Problem007()
        self.assertEqual(104743, prob.find_solution())
    
    def test_prob_008(self):
        """Test problem 8"""
        prob = ProjectEuler.solutions.problem_008.Problem008()
        self.assertEqual(40824, prob.find_solution())
    
    def test_prob_009(self):
        """Test problem 9"""
        prob = ProjectEuler.solutions.problem_009.Problem009()
        self.assertEqual('31875000', prob.find_solution())
    
    def test_prob_010(self):
        """Test problem 10"""
        prob = ProjectEuler.solutions.problem_010.Problem010()
        self.assertEqual('142913828922', prob.find_solution())
    
    def test_prob_011(self):
        """Test problem 11"""
        prob = ProjectEuler.solutions.problem_011.Problem011()
        self.assertEqual(70600674, prob.find_solution())
    
    def test_prob_012(self):
        """Test problem 12"""
        prob = ProjectEuler.solutions.problem_012.Problem012()
        self.assertEqual(76576500, prob.find_solution())

if __name__ == '__main__':
    unittest.main()
