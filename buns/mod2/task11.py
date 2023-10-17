inp = input()
str = ''
flag = False
for symb in inp:
    if symb == ' ':
        continue
    if symb in str:
        flag = True
        break
    str += symb
print(flag)