"""

"""

# Interface:
#   Stuff that comes in: when I create the operation, I pass a variable number of args
#   Stuff that comes out: operate() returns the computed values of the numbers passed on initializatin operation.
#   Possible errors: Nothing

class Operation(object):
    def __init__(self, *args):
        self.args = args
    
    def operate(self):
        raise NotImplementedError()

class AddOperation(Operation):
    def operate(self):
        return sum(self.args)


class SubtractOperation(Operate):
    def operate(self):
        return sum([self.args[0]] + [x * -1 for x in self.args[1:]])


class MultiplyOperation(Operation):

    def operate(self):
        result = 1
        for i in self.args:
            result *= i
        return result

"""
add = AddOperation(1,3,2)
add.operate()
"""

class Calculator(object):
    def __init__(self, operation):
        # self.operation == AddOperation
        self.operation = operation

    def calculate(self, *args):
        op = self.operation(*args)
        return op.operate()


from brandons_code import DivideOperation

calc_add = Calculator(DivideOperation)
calc_mul = Calculator(MultiplyOperation)

calc_add.calculate(3, 4, 1)


