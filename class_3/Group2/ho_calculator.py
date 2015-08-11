class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    def operate(self):
        return sum(self.args)


class SubtractOperation(Operation):
    def operate(self):
        return sum([self.args[0]] + [x * -1 for x in self.args[1:]])


op = AddOperation(1, 2, 3)
result = op.operate()
print(result)


class Calculator(object):

    def __init__(self, operation):
        # AddOperation
        self.operation = operation
        
    def calculate(self, *args):
        # args = (4, 3)
        # op = AddOperation(4, 3)
        # op.operate()

        # Same thing than line 19
        op = self.operation(*args)
        result =  op.operate()
        
        return result


calc = Calculator(operation=AddOperation)

res = calc.calculate(4, 3)
print(res)


"""
calc1 = Calculator(operations={
    'add': AddOperation,
    'subtract': SubtractOperation})

calc2 = Calculator(operations={
    'add': AddOperation})


p = Person(name='Alf')
"""

"""
class Ship(object):
    pass

patrol = Ship()
patrol.place()
"""