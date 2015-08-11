def divisible_numbers(a_list, a_list_of_terms):
    divisible = []
    for term in a_list_of_terms:
        for element in a_list:
            if element % term == 0:
                divisible.append(element)
    print divisible

a_list = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a_list_of_terms = [2, 3]

divisible_numbers(a_list, a_list_of_terms)

def divisible_numbers2(a_list, term):
   a_list = [x for x in a_list if all(x % term == 0 for x in a_list)]
   print a_list


a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
divisible_numbers2(a_list, 3)