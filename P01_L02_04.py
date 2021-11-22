demo = input().split()

for i in demo:
    if len(i) < 10:
        print(i)
    else:
        print(i[:10])
