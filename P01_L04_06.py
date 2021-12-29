from itertools import count, cycle

for i in count(3):
    print(i)
    if i > 10:
        break


count = 0
for i in cycle('cycle'):
    if count > 10:
        break
    print(i)
    count += 1

