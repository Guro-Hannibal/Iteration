with open('ex_3.txt', 'r') as f:
    employers_salary_list = [el.split() for el in f.readlines()]
    for el in employers_salary_list:
        if int(el[1]) < 200000:
            print(f'{el[0]} has salary less then 200000')
    medium = [int(el[1]) for el in employers_salary_list]
    print(f'Average salary - {sum(medium) / len(medium)}')

