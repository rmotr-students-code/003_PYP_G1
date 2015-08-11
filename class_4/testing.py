"""
Implement one unit tests for "sub(a, b)" function, that validates the resulting
value of its execution.
"""

def say_hello(a, b):
    return a + b

    

import unittest 

class AssignmentTestCase(unittest.TestCase):
  
    def test_sum(self):
        """Should return the sum of given arguments"""
        self.assertEquals(say_hello(3, 4), 7)
        
unittest.main()
