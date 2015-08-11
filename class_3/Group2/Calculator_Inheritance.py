"""
You'll need to build a better version of your calculator using OOP and inheritance:
A calculator can be built with different operations. An Operation is an abstract class for which you'll define
subclasses.

Example:


The calculator has 1 magic method `calculate` that will receive the arguments
and the operation to perform. For example:


calc1 = Calculator(operations={'add': AddOperation, 'subtract': SubtractOperation})
calc1.calculate(2, 1, 5, 'add')  # Should return 2 + 1 + 5 = 8

calc2 = Calculator(operations={'add': AddOperation})
calc2.calculate(1, 5, 'add')  # Should return 1 + 5 = 6



*IMPORTANT: The number of arguments should be variable*

The Calculator will check if it has that computation present and
invoke the operation. Operations are initialized with the arguments to compute:

op = AddOperation([2, 1, 5])

Once you have an operation object created you should be able to invoke the `operate`
method PRESENT IN EVERY OPERATION.

op.operate()  # Should return 8

*Important notes:*
* The only method that you must implement for every operation is the `operate` method.
* If the operation is not supported by the calculator (for exampleinvoking `multiply` on calc1)
   the calculator should raise a custom exception (built by you) named `OperationInvalidException`.

This is a unittest class that might be useful for development:


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(operations={
            'add': AddOperation})
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)


if __name__ == '__main__':
    unittest.main()

"""

class Operation(object):
    def __init__(self, *args):
        self.args = args

op = XXXOperation(1,2,3)
op.operate()


class Calculator(object):
    
    def __init__(self, *calcvals):
        self.numbers = calcvals[0:-1]
        self.args = calcvals[-1]
        print  'Calculator'
        print self.numbers
        print 'Calculator' 
        print self.args

class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()

class AddOperation(Calculator):
    def __init__(self, numbers):
        self.numbers = numbers
    
    Calculator.__init__(self, *args)
    
    def operate(self):  
        def __init__(self, *numbers):
            print self.numbers
            return sum(self.numbers)

"""
class SubtractOperation(Operation):
    ''' Subtract Operation ''' 
    def __init__(self, *calcvals):
        Calculator.__init__(self, *calcvals)
    
    def operate(self):
"""        

'''
class Teacher(SchoolMember):

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "{:d}"'.format(self.salary)
'''

a = AddOperation(1,2,5,1)
a.operate()

