inp = input()
sum_even_numbers = 0
sum_odd_numbers = 0
for i in range(1, len(inp)+1):
    if i % 2 == 0:
        sum_even_numbers += int(inp[i-1])
    else:
        sum_odd_numbers += int(inp[i-1])
if (sum_even_numbers * 3 + sum_odd_numbers) % 10 == 0:
    print('yes')
else:
    print('no')