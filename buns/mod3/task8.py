inp = input()
result = [i for i in inp if i.isdigit() or i =='+']
print(''.join(result))