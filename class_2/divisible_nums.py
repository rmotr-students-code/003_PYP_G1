
[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (2) = 12, 10, 8, 6, 4, 2

[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (2, 3) = 12, 6

[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] (2, 3, 4) = 12

[is_divisible_by(return True for term in terms if elem % term = 0)]

def is_divisible_by(elem, terms):
    for term in terms:
        if elem % term != 0:
            return False
    return True

a_list = [1, 2, 3, 4]
results = 
for elem in a_list:
    pass

[elem for elem in a_list]  # [1, 2, 3, 4]

[elem for elem in a_list if is_divisible_by(elem, terms)]


def divisible_numbers(a_list, terms):
    results = []

    for elem in a_list:
        if is_divisible_by(elem, terms):
            results.append(elem)

    return a_list


def divisible_numbers(a_list, terms):
    return [elem for elem in a_list if is_divisible_by(elem, terms)]


# checking Michelle
# using reduce and lambda
# def divisible_numbers(a_list, term):
#     return reduce(lambda l1,l2: [i for i in l1 if i in l2],[[i for i in a_list if i%j ==0] for j in term]) 