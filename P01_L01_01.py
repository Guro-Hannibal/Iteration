time_in_seconds = int(input('Введите время в секундах : '))

h = time_in_seconds // 3600
m = time_in_seconds // 60 - h * 60
s = time_in_seconds % 60
print(f'{h:02} : {m:02} : {s:02}')
