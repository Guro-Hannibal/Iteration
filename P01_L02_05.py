demo = [7, 5, 3, 3, 2, 2]
new_item = float(input())
i = 0
for item in demo:
    if new_item <= item:
        i += 1
    elif new_item > item:
        break
demo.insert(i, new_item)
print(demo)
