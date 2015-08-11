"""
Write a simple random password generator using iterators. The generator can accept two parameters:
* available_chars: The characters to use to generate the password. OPTIONAL. Default: A set of characters, digits and symbols. (hint, check the string module)
* length: The length of the password. OPTIONAL. Default: 8

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba'

"""

class SimplePasswordGenerator(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass