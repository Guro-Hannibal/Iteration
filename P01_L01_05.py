count = int(input(''))
finish_count = int(input(''))
print(count)
days = 1
while count < finish_count:
    count *= 1.1
    days += 1
    print(count, days)
