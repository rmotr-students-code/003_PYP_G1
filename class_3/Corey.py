class Calculator(object):
    
    def __init__(self):
        pass
    
    def add(self, x, y):
        print(x + y)
        
    def subtract(self, x, y):
        print(x - y)
        
    def multiply(self, x, y):
        print(x*y)
        
    def divide(self, x, y):
        print(x / float(y))

c = Calculator()
c.add(2, 3)
c.subtract(10, 1)
c.multiply(2, 3)
c.divide(1, 1)