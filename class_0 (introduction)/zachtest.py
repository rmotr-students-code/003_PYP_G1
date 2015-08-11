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

def calculator(firstNum, secondNum, operation):
    if (operation == 'add'):
        print (firstNum + secondNum)
    elif (operation == 'subtract'):
        print (firstNum - secondNum)
    elif (operation == 'multiply'):
        print (firstNum * secondNum)
    elif (operation == 'divide'):
        print (firstNum / secondNum)
        
calculator(2, 3, 'add')
calculator(7, 3, 'subtract')
calculator(2, 7, 'multiply')
calculator(8, 4, 'divide')
calculator(5, 2, 'divide')