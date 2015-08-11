def first_n_integers(n):
    i = 0
    while i < n:
        yield i
        i += 1


gen = first_n_integers(3)

for number in gen:
    print(number)



#third_num = next(gen)

"""

def simple_generator():
    print("Created")
    yield 1
    print("Hello")
    yield 2
    print("World")

gen = simple_generator()

first_call = next(gen)

print(first_call)

second_call = next(gen)

print(second_call)

"""