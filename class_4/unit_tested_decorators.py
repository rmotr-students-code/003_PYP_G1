def pretty_result(original_function):
    def fake_it(a, b):
        return original_function(a, b)
    
    return fake_it

@pretty_result
def my_sum(a, b):
    return a + b

import unittest

class PrettyPrintDecoratorTestCase(unittest.TestCase):
    def test_different_numbers_work_ok(self):
        "Should test that invoking my_sum with small numbers returns ok"
        self.assertEquals(my_sum(2, 3), "The result of the sum is 5")

unittest.main()

#assert my_sum(2, 3) == "The result of the sum is 5", "First assertion failed"
#assert my_sum(3, 3) == "The result of the sum is 6", "Second assertion failed"
#assert my_sum(90000000000000000000000, 3) == "The result of the sum is 90000000000000000000003", "Big number assertion failed"


