demo = input('Выручка и издержки через пробел : ').split()
print(demo)
if int(demo[0]) - int(demo[1]) > 0:
    print(f'Прибыль : {int(demo[0]) - int(demo[1])}\nРентабельность : '
          f'{(int(demo[0]) - int(demo[1])) / int(demo[0]) * 100}%')
    employers_count = input('Введите число сотрудников : ')
    print(f'Прибыль на сотрудника : {(int(demo[0]) - int(demo[1])) / int(demo[0]) * 100 / int(employers_count)}%')
elif int(demo[0]) - int(demo[1]) == 0:
    print('0')
else:
    print(f'Убыток : {int(demo[0]) - int(demo[1])}')
