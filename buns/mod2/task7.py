inp = input()
zeros = 0
units = 0
for symb in inp:
    if symb == '0':
        zeros += 1
        continue
    units += 1
if zeros == units:
    print('yes')
else:
    print('no')