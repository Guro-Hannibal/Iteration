def foo(item):
    i = ''
    for char in item:
        if char.isdigit():
            i += char
    if i == '':
        i = 0
    return int(i)


demo_dict = {}
with open('ex_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, lec, practice, lab = line.split()
        demo_dict[name] = foo(lec) + foo(practice) + foo(lab)

print(demo_dict)
