from itertools import count

demo = [[1, 30, 1, 3], [3, 10, 3, 1, 2, 8, 13131, 55], [1, 1, 3, 3], [3, 3, 1, 1]]
demo01 = [[1, -27, 1, 3, 5], [3, -7, 3, 1, 3], [1, 1, 3, 3], [5, 33, 1, 33, 11]]


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for num in row:
                print(str(num) + 5 * ' ', end='')
            print('\n')
        return ''

    def __add__(self, other):
        main_body = []
        for row in self.matrix:
            row_i = self.matrix.index(row)
            demo_row = []
            el_i = 0
            while True:
                if len(other[row_i]) - 1 < el_i > len(row) - 1:
                    break
                try:
                    demo_row.append(row[el_i] + other[row_i][el_i])
                except IndexError:
                    try:
                        demo_row.append(other[row_i][el_i])
                    except IndexError:
                        demo_row.append(row[el_i])
                el_i += 1
            main_body.append(demo_row)
        self.matrix = main_body
#
#
# # for num in row:
# # demo_m.append([(int(num)) + i for i in [el for el in other]])
#
#
matrix13 = Matrix(demo)

matrix31 = Matrix(demo01)

matrix13.__add__(demo01)

str(matrix13)

# something = [i for el in demo for i in [el]]
# anything = [i for i in something]

# print(anything)

# print(lambda x: num for num in [i for i in something] + [3])
# print([f'{i}:i{demo.index(el)}:l{len(el)}' for el in something for i in el] +
#       [f'{z}:i{demo01.index(elem)}:l{len(elem)}' for elem in demo01 for z in elem]
#       [for ]
#       )

# sigma = [num_01 + num_02 for num_01, num_02 in [f'{i}:i{demo.index(el)}:l{len(el):0}'
# for el in something for i in el] +
#       [f'{z}:i{demo01.index(elem)}:l{len(elem):0}' for elem in demo01 for z in elem] if ]

# list(map(lambda matrix_main, matrix_add: [sigma.append(int(matrix_main)+int(matrix_add))] if len([el for el in demo]) >= len([el for el in demo01]) else print(00),
#          [i for el in demo for i in el], [i for el in demo01 for i in el]))
#
# list(map(lambda matrix_main, matrix_add, count: demo_row.append([num for num in matrix_main] + [num_add for num_add in matrix_add]) if len([el for el in demo]) >= len([el for el in demo01]) else print(count),
#          [el for el in demo], [el for el in demo01])), [len(lgh) for lgh in demo]

sigma = []
demo_row_add = []
zed = -1
i = 0
# for element in map(lambda matrix_main, matrix_add: [matrix_main] + [matrix_add] if len([el for el in demo]) >=
#                    len([el for el in demo01]) else [matrix_add] + [matrix_main],
#                    [el for el in demo], [el for el in demo01]): print(element[zed+1].index(element[zed])) if element[zed+1].index(element[zed+1]) == element[zed].index(element[zed]) else print(element[zed+1].index(element[zed+1]))

for element in map(lambda matrix_main, matrix_add: [matrix_main] + [matrix_add],
                   [el for el in demo], [el for el in demo01]):
    sigma.append(list(map(lambda main, add: int(main) + int(add), element[zed], element[zed+1])))
for el in sigma: el.append(demo[sigma.index(el)][len(demo[sigma.index(el)])-1]) if \
    len(demo[sigma.index(el)]) > len(demo01[sigma.index(el)]) else \
    el.append(demo01[sigma.index(el)][len(demo01[sigma.index(el)])-1]) if \
    len(demo[sigma.index(el)]) < len(demo01[sigma.index(el)]) else \
    print(f'{demo[sigma.index(el)]} length of row_main is equal to length of row_add {demo01[sigma.index(el)]}')


print(sigma)

# print(element[zed], element[zed+1], element[zed].index(main), element[zed+1].index(add))