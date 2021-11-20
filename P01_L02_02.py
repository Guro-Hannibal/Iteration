demo = input('Через пробел : ').split()
print(demo)
new_demo = []
for i in range(1, len(demo), 2):
    demo[i], demo[i-1] = demo[i-1], demo[i]
print(demo)
