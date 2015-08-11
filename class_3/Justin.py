"""
Build a simple calculator using Object Oriented Programming.
This is the interface it should follow:

    calculator = Calculator()

    calculator.add(2, 4)  # 6
    calculator.subtract(8, 1)  # 7
    calculator.multiply(3, 5)  # 15
    calculator.divide(5, 2)  # 2.5
"""

class Calculator(object):
    
    def __init__(self):
        pass
    
    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result
    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result
    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result
    def divide(self, num1, num2):
        self.result = float(num1) / num2
        return self.result

mycal = Calculator()        
mycal.add(2, 4)  # 6
mycal.subtract(8, 1)  # 7
mycal.multiply(3, 5)  # 15
mycal.divide(5, 2)  # 2.5

"""
Build a calculator using only static and class methods. This is the way it should work:

    Calculator.add(2, 4)  # 6
    Calculator.subtract(8, 1)  # 7
    Calculator.multiply(3, 5)  # 15
    Calculator.divide(5, 2)  # 2.5

Note that I've never created an instance of the calculator. I'm using the regular class.

One final addition. The `subtract` method **must** be implemented using the `add` method. Something like this:

subtract = add(x, y * -1) 
"""

class Calculator2(object):
    
    def __init__(self):
        pass
    
    @classmethod
    def add(cls, num1, num2):
        result = num1 + num2
        return result
    
    @classmethod
    def subtract(cls, num1, num2):
        result = cls.add(num1, num2 * -1)
        return result
    
    @classmethod
    def multiply(cls, num1, num2):
        result = num1 * num2
        return result
    
    @classmethod
    def divide(cls, num1, num2):
        result = float(num1) / num2
        return result


print Calculator2.add(2, 4)  # 6
print Calculator2.subtract(8, 1)  # 7
print Calculator2.multiply(3, 5)  # 15
print Calculator2.divide(5, 2)  # 2.5