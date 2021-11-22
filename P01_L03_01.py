from math import inf


def foo(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return f'from {-inf} to {inf}'


print(foo(5, 0))
