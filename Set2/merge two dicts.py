dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 15, 'c': 25, 'd': 35}

dict3 = dict1.copy()
for key, value in dict2.items():
    if key in dict3:
        dict3[key] += value
    else:
        dict3[key] = value

print(dict3)