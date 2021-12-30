import json

with open('ex_7.txt', 'r') as f:
    demo_list = [line.split() for line in f]
    profit = [int(el[2]) for el in demo_list if int(el[2])-int(el[3]) > 0]
    result_list = [{el[0]: (int(el[2]) - int(el[3])) for el in demo_list},
                   {'average profit': sum(profit) / len(profit)}]

print(result_list)

with open('ex_7.json', 'w') as f:
    json.dump(result_list, f)
