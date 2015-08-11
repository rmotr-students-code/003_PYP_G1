def pretty_result(original_function):
    def modify(*args, **kwargs):
        original_result = original_function(*args, **kwargs)
        return "The result of the sum is: {}".format(original_result)
    return modify

@pretty_result
def my_sum(a, b):
    return a + b


res = my_sum(2, 3)
print(res)