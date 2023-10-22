inp = int(input())
result = ', '.join([format(inp, i) for i in 'box'])
print('Неверный ввод' if inp < 0 else result)