demo = '5 10 4 11 3'

#demo_2 = input()

#print(demo.split(' '))

foo_sum = 0


def foo(item):
    global foo_sum
    item_demo = item.split()
    for num in item_demo:
        foo_sum += int(num)
    print(foo_sum)


foo(demo)
