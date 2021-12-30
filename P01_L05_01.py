with open('text.txt', 'x') as f:
    while True:
        var = input()
        if var == '':
            break
        f.writelines(var + '\n')

with open('text.txt', 'r') as f:
    some_text = f.read()

print(some_text)