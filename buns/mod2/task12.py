inp = input()
number = ''
for symb in inp:
    if symb not in '-() ':
        number += symb
print(number)