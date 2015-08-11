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
    
    def add(self, value1, value2):
        result= (value1 + value2)
        return result
        
    def subtract(self, value1, value2):
        result= (value1 - value2)
        return result
        
    def multiply(self,value1, value2):
        result= (value1 * value2)
        return result
        
    def divide(self, value1, value2):+
        result= (value1 - value2)
        return result
        
bjcalc= Calculator()
print bjcalc.add(2,4)
print bjcalc.subtract(2,4)
print bjcalc.multiply(4,4)
print bjcalc.divide(8,2)


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

    @classmethod
    def add(self, value1, value2):
        result= (value1 + value2)
        return result
    
    @classmethod    
    def subtract(self, value1, value2):
        result= (value1 - value2)
        return result
    
    @classmethod    
    def multiply(self,value1, value2):
        result= (value1 * value2)
        return result
    
    @classmethod    
    def divide(self, value1, value2):
        result= (value1 - value2)
        return result
        
#bjcalc= Calculator2()
print Calculator2.add(2,4)
print Calculator2.subtract(2,4)
print Calculator2.multiply(4,4)
print Calculator2.divide(8,2)