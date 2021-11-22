master = []
demo = {'name': '', 'price': '', 'amount': '', 'measure_unit': ''}
i = 0
while True:
    data = input().upper()
    if data == 'Q':
        break
    i += 1
    for key in demo.keys():
        item = input(f'{key}')
        demo[key] = item
    master.append((i, demo.copy()))
print(master)


