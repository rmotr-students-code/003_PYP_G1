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

def calculator(param1, param2, operation):
    if operation == 'add':
        #add
        param1 += param2
        print param1
    elif operation == 'subtract':
        #subtract
        param1 -= param2
        print param1
    elif operation == 'multiply':
        #multiply
        param1 *= param2
        print param1
    elif operation == 'divide':
        #divide
        if param1%param2 != 0:
            param1 = param1/float(param2)
        else:
            param1 = param1/param2
        print param1
    else:
        print 'Not valid operation'
        
calculator(2, 3, 'add')       # Should return 5
calculator(7, 3, 'subtract')  # Should return 4
calculator(2, 7, 'multiply')  # Should return 14
calculator(8, 4, 'divide')    # Should return 2
calculator(5, 2, 'divide')    # Should return 2.5 ATTENTION!