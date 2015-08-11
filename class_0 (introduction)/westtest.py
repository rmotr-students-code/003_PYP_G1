"""
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print 'Hello, my name is', self.name
        
p = Person('West')

p.say_hi()
"""
"""
class MyClass(object):
    def the_static_method(x):
        print x
    the_static_method = staticmethod(the_static_method)

MyClass.the_static_method(2) # outputs 2
"""
class Operation(object):
    def __init__(self, *args):
       self.args = args

    def print_args(self):
        print args


test = Operation("this is an arg", "yep an arg as a string")

test.print_args