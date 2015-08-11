
class Calculator(object):    
    def __init__(self):
        pass
    
    def add(self, number1, number2):
        return number1 + number2
        
    def subtract(self, number1, number2):  
        return number1 - number2
        
	def multiply(self, number1, number2):
        return number1*number2
        
    def divide(self, number1, number2):
        return 1.0*number1/number2
        
mycalc = calculator()
print(mycalc.add(1,1)) 

class calculator_2(object):

    def __init__(self):
        pass
    
    @classmethod
    def add(cls,number1, number2):
        return number1 + number2
    
    @classmethod
    def subtract(cls,number1, number2):  
        return cls.add(number1, number2*-1)
    
    @classmethod
    def multiply(cls,number1, number2):
        return number1 * number2    
    
    @classmethod
    def divide(cls,number1, number2):
        return 1.0*number1/number2    
        
#print calculator_2.add(1,1)