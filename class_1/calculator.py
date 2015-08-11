"""
Write a function that receives 2 numbers and performs simple calculations
(additions, subtractions, multiplications and divisions)
based on a string parameter.
Example:
    calculator(2, 3, 'add')       # Should return 5
    calculator(7, 3, 'subtract')  # Should return 4
    calculator(2, 7, 'multiply')  # Should return 14
    calculator(8, 4, 'divide')    # Should return 2
    calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""

def add(a_list_of_numbers):
    return a_list_of_numbers[0] + sum([x for x in a_list_of_numbers[1:]])
    

def subtract(a_list):
    return a_list[0]  + sum([x * -1 for x in a_list[1:]])


def calculator(*args):
    # args = [1, 2, 5, 7, 8, 'add']
    if args[-1] == 'subtract':
        return subtract(args[:-1])
    elif args[-1] == 'add':
        return add(args[:-1])


assert calculator(1, 2, 5, 7, 8, 'add') == 23, "Calculator broken :("
assert calculator(9, 2, 1, 'subtract') == 6, "Calculator broken again :("


"""
OPERATION_MAPPING = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / float(y)
}


def calculator(param1, param2, operation):
    return OPERATION_MAPPING[operation](param1, param2)


print calculator(2, 3, 'add')       # Should return 5
print calculator(7, 3, 'subtract')  # Should return 4
print calculator(2, 7, 'multiply')  # Should return 14
print calculator(8, 4, 'divide')    # Should return 2
print calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!
"""