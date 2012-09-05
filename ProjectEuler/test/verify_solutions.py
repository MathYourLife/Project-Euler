"""
Once a problem is successfully solved, add to the test
suite to ensure future changes to modules do not 
corrupt the solution.
"""

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
import unittest

class myTestCase(unittest.TestCase):
    def test_prob_001(self):
        prob = ProjectEuler.solutions.problem_001.Problem001()
        self.assertEqual('233168', prob.find_solution())

    def test_prob_002(self):
        prob = ProjectEuler.solutions.problem_002.Problem002()
        self.assertEqual(4613732, prob.find_solution())

    def test_prob_003(self):
        prob = ProjectEuler.solutions.problem_003.Problem003()
        self.assertEqual('6857', prob.find_solution())

    def test_prob_004(self):
        prob = ProjectEuler.solutions.problem_004.Problem004()
        self.assertEqual('993 x 913 = 906609', prob.find_solution())

    def test_prob_005(self):
        prob = ProjectEuler.solutions.problem_005.Problem005()
        self.assertEqual(232792560, prob.find_solution())

    def test_prob_006(self):
        prob = ProjectEuler.solutions.problem_006.Problem006()
        self.assertEqual(25164150, prob.find_solution())

    def test_prob_007(self):
        prob = ProjectEuler.solutions.problem_007.Problem007()
        self.assertEqual(104743, prob.find_solution())

    def test_prob_008(self):
        prob = ProjectEuler.solutions.problem_008.Problem008()
        self.assertEqual(40824, prob.find_solution())

    def test_prob_009(self):
        prob = ProjectEuler.solutions.problem_009.Problem009()
        self.assertEqual('31875000', prob.find_solution())

    def test_prob_010(self):
        prob = ProjectEuler.solutions.problem_010.Problem010()
        self.assertEqual('142913828922', prob.find_solution())

    def test_prob_011(self):
        prob = ProjectEuler.solutions.problem_011.Problem011()
        self.assertEqual(70600674, prob.find_solution())

if __name__ == '__main__':
    unittest.main()
