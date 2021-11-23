def foo(a, b):
    z = a
    for i in range(-b+1):
        a /= z
    return a


print(foo(5, -4))

print(5 ** -4)
