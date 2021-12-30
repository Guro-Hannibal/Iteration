with open('some_text_file_for_L05_ex2.txt', 'r') as f:
    count = len(f.readlines())
    print(f'Количество строк {count}')
    f.seek(0)
    i = 1
    for el in f.readlines():
        print(f'{len(el.split())} слов в строке {i}')
        i += 1
