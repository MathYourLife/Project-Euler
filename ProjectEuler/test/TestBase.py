"""
Base test class with additional testing functionality
"""

import unittest

class BaseTest(unittest.TestCase):
    def assertEqual(self, expected, test, msg=''):
        
        msg = "%s\n\texpected: %s\tvalue: %s" % (msg, expected, test)
        super(BaseTest, self).assertEqual(expected, test, msg)

