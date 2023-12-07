import os
# directory = input()

dir = input()
dict ={}
if os.path.exists(dir):
    file = open(dir, 'r', encoding='utf-8')
    for i in file.read():
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
else:
    print('Нет такой директории')

sort_data = sorted(dict.items(), key=lambda x: x[1])
for i, j in sort_data:
    print(i + ': ' + str(j))