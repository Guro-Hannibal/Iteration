from functools import reduce

demo_list = [el for el in range(100, 1001) if el % 2 == 0]


def foo(a, b):
    return a * b


print(reduce(foo, demo_list))

