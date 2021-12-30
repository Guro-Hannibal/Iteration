import random

with open('ex_5.txt', 'w') as f:
    for i in range(10):
        f.write(str(random.randint(0, 100)))

with open('ex_5.txt', 'r') as f:
    demo_list = [int(el) for el in f.read()]

print(f'Общая сумма - {sum(demo_list)}')
