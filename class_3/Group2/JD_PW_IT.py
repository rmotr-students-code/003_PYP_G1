#import string
import random

"""
Write a simple random password generator using iterators. The generator can accept two parameters:
* available_chars: The characters to use to generate the password. 

OPTIONAL. Default: A set of characters, digits and symbols. (hint, check the string module)
* length: The length of the password. OPTIONAL. Default: 8

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba'

"""

class SimplePasswordGenerator(object):
    
    def __init__(self, available_chars, length):
        self.available_chars = available_chars
        self.length = length
        self.password = ''
        
    def __iter__(self):
        return self
              
    def next(self):
        print "len of password = " + str(len(self.password))
        if len(self.password) < self.length:
            self.new_char = random.choice(self.available_chars)
            self.password = self.password + self.new_char
            print "password inside next if = " + self.password
            return self.password
            
        else:
            print "Exception"
            raise StopIteration
        print "password inside next else = " + self.password
       

pg = SimplePasswordGenerator(['a','b','c','d'], 8)
print pg.next()

