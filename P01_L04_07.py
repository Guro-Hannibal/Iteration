def fact(i):
    factor = 1
    for el in range(1, i+1):
        factor *= el
        yield factor
    return factor


demo = fact(4)


for elem in demo:
    print(elem)
