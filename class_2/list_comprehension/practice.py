#a_list = [1, 0, 1, 0, 0, 0, 1] # > [True, False, True, False, False, False]


[((elem == 1 and True) or (elem == 0 and False)) for elem in a_list]

#[ elem for elem in a_list if elem in a_list == 1] 

a_list = ['abc', 'hello', 'world', 'Brandon'] # > [3, 5, 5, 7]

[len(elem) for elem in a_list]


# [{returned} for {elem} in {collection} if {condition}]

# 1) Whatever is going to be appended to the new list
# 2) is the element
# 3) collection


results = []

def boolean_equivalent(elem):
    if elem == 1:
        return True
    elif elem == 0:
        return False


for elem in a_list:
    results.append(boolean_equivalent(elem))

[boolean_equivalent(elem) for elem in a_list]


results = [elem for elem in list_two if elem in list_one]

#[]

#if 1 in list_one[:]



[elem for elem in my_list if False]
