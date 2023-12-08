import os
# directory = input()

dir = input()
dict ={}
file = open(dir, 'r+', encoding='utf-8')
if os.path.exists(dir):
    for i in file.read():
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
else:
    print('Нет такой директории')

for i, j in dict.items():
    file.writelines(i + ': ' + str(j))