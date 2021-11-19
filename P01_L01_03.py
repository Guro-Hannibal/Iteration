num = int(input())
i = 0
while num > 0:
    if i < num % 10:
        i = num % 10
        if i == 9:
            break
    num //= 10
print(i)
