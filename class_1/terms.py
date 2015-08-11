"""
def divisible_numbers(a_list, a_list_of_terms):
    results = []
    finalanswer= []
    length = len(a_list_of_terms)
    for term in a_list_of_terms:
        for i in a_list:
            if (i % term) == 0:
                results.append(i)
    results.sort()
    for i in range(0,len(results)-1):
        if results[i] == results[i+1]:
            finalanswer.append(results[i])
            finalanswer.reverse
    return finalanswer


print(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4]))
"""


def is_divisible_by(a_number, terms):
    for x in terms:
       if a_number % x != 0:
           return False
    return True
            
            

print(is_divisible_by(4, [2])) # True
print(is_divisible_by(4, [2, 4])) # True
print(is_divisible_by(4, [2, 3])) # False! 4 is not divisible by 3
print(is_divisible_by(12, [2])) # True
print(is_divisible_by(12, [2, 4, 3, 6])) # True
print(is_divisible_by(12, [2, 4, 3, 6, 7])) # False! 12 is not divisible by 7


# We'll use this one here:

def divisible_numbers(a_list, terms):
    results = []
    for elem in a_list:
        if is_divisible_by(elem, terms):  # Here's the magic
            results.append(elem)
    return results
    
print(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3]))


## FORGET ABOUT THIS:
"""
def divisible_just_by_2_and_3(a_list):
    # In this case `terms` is hardcoded
    # to be [2, 3]
    # How can you make it generic to accept different
    # terms?
    # I know we need to iterate over terms right?
    
    # Yes. because you don't know how many you'll get. You might get [2, 3], or just [2], or nothing, or a thousand. so 
    results = []
    for terms in term:
    for element in a_list:
        if element % element == 0 and element % 3 == 0:
            results.append(element)
    return results


def divisible_numbers(a_list, terms):
    # Generic one
    pass


print(divisible_just_by_2_and_3([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

print(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4])) # This should be [12]

 # This should be [12, 6]
"""