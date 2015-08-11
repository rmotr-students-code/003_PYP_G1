"""
Build a simple calculator using Object Oriented Programming.
This is the interface it should follow:

    calculator = Calculator()

    calculator.subtract(8, 1)  # 7
    calculator.multiply(3, 5)  # 15
    calculator.divide(5, 2)  # 2.5
"""

class Calculator(object):
    # def __init__(self):
    
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(2, 3, 5))