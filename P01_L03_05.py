demo = '5 10 4 11 3'

foo_sum = 0


def foo(main_sum):
    end = False
    item = input()
    item_demo = item.split()
    if 'Q' in item_demo:
        item_demo = item_demo[:item_demo.index('Q')]
        end = True
    for num in item_demo:
        main_sum += int(num)
    print(main_sum)
    if end:
        return
    foo(main_sum)


foo(0)
