# HEre?
"""
def add(x, y):
    return x + y

def compute(x, y, operation):
    return operation(x, y)

x = 2

compute(1, 2, add)
compute(2, 1, lambda x, y: x - y)

"""
"""
a_list = [1, 2, 3, 4]
square = lambda x: x * x
map(square, a_list)

result = []
for elem in a_list:
    squared_elem = square(elem)
    result.append(squared_elem)
return result
"""

# map
[apple, apple, apple] > [orange, orange, orange]

# reduce
[apple, apples, apples] > thing (pie)

# 1st
results = []
for elem in a_list:
    if is_even(elem):
        results.append(square(elem))

# 2nd
a_list = [1, 2, 3, 4]
map(
    lambda x: x * x,
    filter(lambda x % 2 == 0, a_list) # [2, 4]
)  # [4, 16]

# 3rd
[x * x for x in a_list if x % 2 == 0]

# 4th
[square(x) for x in a_list if is_even(x)]


