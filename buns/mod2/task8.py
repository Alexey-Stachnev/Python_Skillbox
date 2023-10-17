inp = input()
s = inp[:-2]
i = inp[-1]
count = 0
for symb in s:
    if symb != i:
        break
    count += 1
print(count)