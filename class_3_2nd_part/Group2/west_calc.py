class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()

class AddOperation(Operation):
   def operate(self):
        return sum(self.args)

class MultiplyOperation(Operation):
    def operate(self):
        return reduce((lambda x, y: x * y))

class Calculator(object):
    def __init__(self, operations):
        self.operations = operations
        print 'Calculator Initialized'
        print operations

    def calculate(self, *args):
        numbers = list(args[0:-1])
        operation = args[-1]
        print numbers
        print operation

        if operation in self.operations:
            print 'The operation is in the dict'
            # I am having a problem here
            # I would think op would mean MultiplyOperation(2, 1, 5)
            print numbers
            op = self.operations[operation](numbers)
            print op.operate()

        else:
            print 'The operation is not in the dict'


calc1 = Calculator(operations={
    'add': AddOperation})

"""
calc2 = Calculator(operations={
    'add': 'AddOperation',
    'multiply': 'MultiplyOperation'})
"""
calc1.calculate(2, 1, 5, 'add')  # Should return 2 + 1 + 5 = 8
