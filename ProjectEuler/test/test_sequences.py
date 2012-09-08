"""
Confirm functionality of the Sequence classes
"""

from ProjectEuler import Sequence
import unittest

class TestTriangleNumbers(unittest.TestCase):
    def setUp(self):
        self.obj = Sequence.TriangleNumbers()
    
    def test_set_position(self):
        msg = 'Initial value is None'
        self.assertEqual(None, self.obj.value, msg)
        msg = 'Setting position returns correct value'
        self.assertEqual(6, self.obj.set_position(3), msg)
        msg = 'Value has been set correctly'
        self.assertEqual(6, self.obj.value, msg)
        
        msg = 'Moved to next value'
        self.assertEqual(10, self.obj.next(), msg)
        self.assertEqual(10, self.obj.value, msg)
        
        msg = 'Moved to previous value'
        self.assertEqual(6, self.obj.previous(), msg)
        self.assertEqual(6, self.obj.value, msg)
        
        self.assertEqual(3, self.obj.previous(), msg)
        self.assertEqual(3, self.obj.value, msg)
        

if __name__ == '__main__':
    unittest.main()
