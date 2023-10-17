inp = 'www.google.com'
result = ''
for symb in range(len(inp)-1, -1, -1):
    if inp[symb] == '.':
        print(result[::-1])
        result = ''
        continue
    result += inp[symb]
print(result[::-1])
