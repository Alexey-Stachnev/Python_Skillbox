inp = input()
i = inp[0]
n = int(inp[3:])
ordinal_number = ord(i)
if ordinal_number + n > 122:
    print(chr(96 + ((ordinal_number+n) % 122)))
elif ordinal_number + n < 97:
    print(chr(123-((ordinal_number-n) % 97)))
else:
    print(chr(ordinal_number + n))