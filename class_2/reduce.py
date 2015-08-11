# reduce(lambda x, y: x + y, [1, 2, 3, 4], 0) == 10

# [apple, apples] > [orange, orange]
# [apple, apple] > pie (thing)

def multiply_partial(acc, new_value):
    return acc * new_value  # 3

a_list = [1, 2, 3, 4]
acc = 1

for elem in a_list:
    # elem 2
    # acc 1
    acc = multiply_partial(acc, elem) # 1

print(acc)