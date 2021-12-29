demo_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for el in demo_list if demo_list.index(el) != 0 and el > demo_list[demo_list.index(el)-1]]

print(new_list)
