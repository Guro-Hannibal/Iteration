with open('ex_4.txt', 'r') as f:
    demo_list = [el.split() for el in f.readlines()]
    print(demo_list)

for el in demo_list:
    if el[2] == '1':
        el[0] = "Один"
    elif el[2] == '2':
        el[0] = "Два"
    elif el[2] == '3':
        el[0] = "Три"
    elif el[2] == '4':
        el[0] = "Четыре"

with open('ex_4_2.txt', 'w') as f:
    for el in demo_list:
        f.write(' '.join(el) + '\n')

