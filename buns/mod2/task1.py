str = input()
comma = str.find(',')
a = int(str[:comma])
b = int(str[comma + 2:])
print(a % b)