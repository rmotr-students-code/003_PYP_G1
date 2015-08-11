"""
def my_func():
    print("Hello")
    return 1

other_func = my_func
print(other_func)
"""

def my_func(*args, **kwargs):
    # args = (2, 3, [8, 3])
    # kwargs = {
    #   'boy': 10,
    #   'tom': 13
    # }
    pass

my_func(2, 3, [8, 3], boy=10, tom=13)

def pretty_result(original_function):
    # original_funcion = my_sum
    #print("First line")
    def fake_it(*args, **kwargs):
        #print("Hey, I just intercepted this func.")
        original_result = original_function(*args, **kwargs)
        return "The result of the sum is {}".format(original_result)
    #print("Returning function")
    return fake_it


@pretty_result
def my_sum(a, b):
    return a + b

def squared(x):
    pass

res = my_sum(2, 3)
print(res)

#res = pretty_result(my_sum(2, 3))
